import json

def load_exitsting_json_file(filename):
        with open(filename, 'r') as f:
            return json.load(f)

class POI_manager : 

    
    def __init__(self, filename):
        self.__filename = filename
    def get_poi_count(self):
        try :
            with open(self.__filename, 'r') as f:
                data = json.load(f)
                return len(data)
        except FileNotFoundError:
            print(f"File {self.__filename} not found.")
            return 0
    
    def get_poi(self):
        ch = ""
        try:
            with open(self.__filename, 'r') as f:
                data = json.load(f)
                for i in data:
                    ch += f"Name: {i['name']}\t" 
        except FileNotFoundError:
            print(f"File {self.__filename} not found.")
            return []

        if ch == "":
            return "No POI found."
        return ch
    def get_pos(self, name):
        try:
            with open(self.__filename, 'r') as f:
                data = json.load(f)
                for i in data:
                    if i['name'] == name:
                        return (i['pos']['lat'], i['pos']['long'])
        except FileNotFoundError:
            print(f"File {self.__filename} not found.")
        return None
    