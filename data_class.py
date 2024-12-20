import json
from dataclasses import dataclass, asdict

@dataclass
class PersonalData:
    name: str = ""
    surname: str = ""
    country: str = ""
    post_code: str = ""
    pesel_number: str = ""

    def print_info(self):
        print(f"name: {self.name}")
        print(f"surname: {self.surname}")
        print(f"country: {self.country}")
        print(f"post_code: {self.post_code}")
        print(f"pesel number: {self.pesel_number}")

    def import_json_data(self, json_file_path):
        try:
            with open(json_file_path, 'r') as json_file:
                json_parsed = json.load(json_file)
                self.name = json_parsed.get("name", "")
                self.surname = json_parsed.get("surname", "")
                self.country = json_parsed.get("country", "")
                self.post_code = json_parsed.get("post_code", "")
                self.pesel_number = json_parsed.get("pesel_number", "")
        except FileNotFoundError:
            print(f"Error: File '{json_file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{json_file_path}' is not a valid JSON file.")

    def export_json_data(self, file_json):
        try:
            with open(file_json, 'w') as json_file:
                json.dump(asdict(self), json_file, indent=4)  # `asdict` konwertuje obiekt do słownika
            print(f"Data successfully exported to '{file_json}'.")
        except Exception as e:
            print(f"Error: Failed to export data to '{file_json}'. {e}")

# Użycie klasy
man1 = PersonalData()
man1.import_json_data("personal_data.json")
man1.export_json_data("export_data.json")
man1.print_info()
