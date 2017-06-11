import json

class ModuleDataStore:

    @staticmethod
    def getNextModulesForStudent(studentID):
        modules = []
        fileHandler = open('model/modules/module-1.json')
        moduleJSON = fileHandler.read()
        fileHandler.close()
        module = json.loads(moduleJSON)
        fileHandler = open('model/modules/module-1.txt')
        moduleText = fileHandler.read()
        fileHandler.close()
        module['text'] = moduleText
        #moduleJSON = moduleJSON.replace('\r','\\r')
        #moduleJSON = moduleJSON.replace('\n','\\n')
        modules.append(module)
        return modules

class Module:

    def __init__(self):
        self.name = ''
        self.age = 0
        self.language = ''
        self.locale = ''
        self.pdfURL = ''
        self.textURL = ''
        self.videoURL = ''
        self.moduleMapping = []

    def to_dict(self):
        return {
            'name' : self.name,
            'age' : self.age,
            'language' : self.language,
            'locale' : self.locale,
            'pdfURL' : self.pdfURL,
            'textURL' : self.textURL,
            'videoURL' : self.videoURL,
            'moduleMapping' : self.moduleMapping
        }