import json

class PersonalData:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.country = ""
        self.post_code = ""
        self.pesel_number = ""

    def print_info(self):
        print("name: " + self.name)
        print("surname: " + self.surname)
        print("country: " + self.country)
        print("post_code: " + str(self.post_code))
        print("pesel number: " + str(self.pesel_number))

    def import_json_data(self, json_file_path):
        json_text = ""
        with open(json_file_path, 'r') as json_file:
            json_text = json_file.read()
            json_file.close()
        json_parsed = json.loads(json_text)
        self.name = json_parsed["name"]
        self.surname = json_parsed["surname"]
        self.country = json_parsed["country"]
        self.post_code = json_parsed["post_code"]
        self.pesel_number = json_parsed["pesel_number"]

    def export_json_data(self, file_json):
        try:
            data_to_export = {
                "name": self.name,
                "surname": self.surname,
                "country": self.country,
                "post_code": self.post_code,
                "pesel_number": self.pesel_number
            }
            with open(file_json, 'w') as json_file:
                json.dump(data_to_export, json_file, indent=4)  # Format JSON with indentation for readability
            print(f"Data successfully exported to '{file_json}'.")
        except Exception as e:
            print(f"Error: Failed to export data to '{file_json}'. {e}")

man1 = PersonalData()
man1.import_json_data("personal_data.json")
man1.export_json_data("export_data.json")
man1.print_info()
