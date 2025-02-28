import language_tool_python
import logging
import re

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class Validator:
    """
    Validates and formats call notes by correcting grammar and applying structured formatting.
    """
    def __init__(self, config):
        self.column_names = ["call note", "call notes", "callnotes"]
        self.language = config.get("language", "en-US")
        self.highlight_color = "yellow"
        try:
            self.tool = language_tool_python.LanguageTool(self.language)
        except Exception as e:
            logging.error(f"Error initializing LanguageTool: {e}")
            self.tool = None

    def correct_errors(self, text):
        """Corrects grammar and spelling using LanguageTool."""
        if self.tool:
            try:
                return self.tool.correct(text)
            except Exception as e:
                logging.error(f"Grammar correction error: {e}")
        return text

    def apply_formatting(self, text):
        """Formats text with proper line breaks and punctuation."""
        # Mask emails to avoid incorrect splits
        email_pattern = re.compile(r'\b[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}\b', re.IGNORECASE)
        replacements = []
        modified_text = text
        for match in reversed(list(email_pattern.finditer(text))):
            original = match.group()
            masked = original.replace('.', '__DOT__')
            modified_text = modified_text.replace(original, masked, 1)
            replacements.append((masked, original))
        
        sentences = [s.strip() for s in modified_text.split('.') if s.strip()]
        formatted_lines = []
        buffer = []
        keywords = ["contact number", "email", "address"]

        for sentence in sentences:
            if any(kw in sentence.lower() for kw in keywords):
                if buffer:
                    formatted_lines.append(' '.join([s + '.' for s in buffer]))
                    buffer = []
                parts = [p.strip() for p in sentence.split(',') if p.strip()]
                for part in parts:
                    for masked, original in replacements:
                        part = part.replace(masked, original)
                    formatted_lines.append(part)
            else:
                buffer.append(sentence)
        if buffer:
            formatted_lines.append(' '.join([s + '.' for s in buffer]))

        return '\n'.join(formatted_lines)

    def validate(self, data, valid_pins):
        """Processes data to validate and format call notes."""
        modified_cells = []
        if not data or not isinstance(data, list) or not data[0]:
            return modified_cells

        headers = data[0]
        col_idx = next((i for i, h in enumerate(headers) if h.strip().lower() in self.column_names), None)

        if col_idx is None:
            logging.error("Call Notes column missing.")
            return modified_cells

        for row_idx, row in enumerate(data[1:], start=1):
            if len(row) <= col_idx:
                continue
            original = row[col_idx].strip()
            if not original:
                continue

            corrected = self.correct_errors(original)
            formatted = self.apply_formatting(corrected)
            if original != formatted:
                row[col_idx] = formatted
                cell_ref = f"{chr(65 + col_idx)}{row_idx + 1}"
                modified_cells.append((cell_ref, self.highlight_color))

        return modified_cells

# Example Usage
if __name__ == "__main__":
    sample_data = [
        ["Name", "Call Note"],
        ["Alice", "Contact number 123, email alice@example.com. Meeting went well. Follow up required."],
        ["Bob", "Incorrect sentence. Another one here."]
    ]
    validator = Validator({"language": "en-US"})
    modified = validator.validate(sample_data, [])
    print(f"Modified cells: {modified}")