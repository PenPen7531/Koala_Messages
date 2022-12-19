import json

from logs import Data
class Logs:
    def __init__(self, company_name):
        if type(company_name) != str:
            raise TypeError
        self.name = company_name
        self.logs=[]
        try:
            with open("/data/admin.json") as file:
                self.logs = [
                    Data(
                        log["date"],
                        log["time"],
                       
                    ) for log in json.load(file)
                ]
                print("Sucess")
        except:
            self.logs = []
            print("Created New file")

    def add(self, data):
        if type(data) is not Data:
            raise TypeError
        self.logs.append(data)

    def save(self):
        with open(f"/data/admin.json", "w") as file:
            json.dump([log.to_dict()
                       for log in self.logs], file)