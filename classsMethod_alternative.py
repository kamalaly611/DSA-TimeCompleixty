class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)  # Calls the class's main constructor

# Using the alternative constructor
date_obj = Date.from_string("2025-01-09")
print(f'{date_obj.year}/{date_obj.month}/{date_obj.day}')  # Output: 2025 1 9
