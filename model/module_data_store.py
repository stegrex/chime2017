import json

class ModuleDataStore:

    @staticmethod
    def getNextModulesForStudent(studentID):
        modules = []
        modules.append(ModuleDataStore.getModuleDictById('1'))
        return modules

    @staticmethod
    def dumpModules():
        modules = []
        modules.append(ModuleDataStore.getModuleDictById('1'))
        modules.append(ModuleDataStore.getModuleDictById('2'))
        modules.append(ModuleDataStore.getModuleDictById('3'))
        return modules

    @staticmethod
    def getModuleDictById(moduleID):
        fileHandler = open('model/modules/module-' + moduleID + '.json')
        moduleJSON = fileHandler.read()
        fileHandler.close()
        module = json.loads(moduleJSON)
        try:
            fileHandler = open('model/modules/module-' + moduleID + '.txt')
            moduleText = fileHandler.read()
            fileHandler.close()
        except:
            moduleText = ""
        module['text'] = moduleText
        return module

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