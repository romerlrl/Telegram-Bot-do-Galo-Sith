import json

class Rjson:
    def __init__(self, file):
        
        self.file = file
        with open(file, encoding='utf-8') as json_file:
            self.data = json.load(json_file)
        

    def __getitem__(self, key):
        return self.data.get(key)

    def __setitem__(self, key, value):
        self.data[key] = value
        self.commit()
    
    def commit(self):
        with open(self.file, 'w', encoding='utf-8') as json_file:
            json.dump(self.data, json_file, indent=4)
            print("Commitou")

    def __iter__(self):
        return iter(self.data)    
        
        