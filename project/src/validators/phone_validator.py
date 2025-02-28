import re
from .base_validator import BaseValidator

class Validator(BaseValidator):
    def __init__(self, config):
        super().__init__(config)

    def validate(self, data, valid_pins):
        invalid_cells = []
        headers = [h.lower() for h in data[0]]
        try:
            col_idx = headers.index(self.column_name.lower())
        except ValueError:
            return invalid_cells
        
        # Indian phone numbers: 10 digits starting with 6-9
        PHONE_REGEX = r'^(\+91)?[6-9]\d{9}$'  # Simplified regex
        
        for row_idx, row in enumerate(data[1:], start=2):
            if col_idx < len(row):
                phone = row[col_idx].strip()
                cleaned = re.sub(r'\D', '', phone)  # Remove non-digits
                
                # Validate ONLY if cleaned is non-empty
                if cleaned:
                    if not re.fullmatch(PHONE_REGEX, cleaned):
                        cell = f"{chr(65 + col_idx)}{row_idx}"
                        invalid_cells.append(cell)
                else:
                    # Flag empty/invalid cleaned numbers
                    cell = f"{chr(65 + col_idx)}{row_idx}"
                    invalid_cells.append(cell)
        return invalid_cells