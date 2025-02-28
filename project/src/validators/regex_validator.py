import re
from .base_validator import BaseValidator

class Validator(BaseValidator):
    """
    Validator that uses a custom regex pattern.
    Assumes that the column is determined by column_name.
    """
    def __init__(self, config):
        super().__init__(config)
        # Retrieve the regex pattern from parameters.
        self.pattern = self.params.get("pattern")
        if self.pattern:
            # Pre-compile the pattern for efficiency.
            self.regex = re.compile(self.pattern)
        else:
            self.regex = None

    def validate(self, data, valid_pins):
        invalid_cells = []
        if not self.regex:
            return invalid_cells
        
        headers = [h.lower() for h in data[0]]
        try:
            col_idx = headers.index(self.column_name.lower())
        except ValueError:
            return invalid_cells  # Column not found; skip validation.
        
        for row_idx, row in enumerate(data[1:], start=2):
            if col_idx < len(row):
                value = row[col_idx].strip()
                if value and not self.regex.fullmatch(value):
                    cell = f"{chr(65 + col_idx)}{row_idx}"
                    invalid_cells.append(cell)
        return invalid_cells
