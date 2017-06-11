import json

class ModuleDataStore:

    @staticmethod
    def getNextModulesForStudent(moduleIDToResult):
        moduleIDs = []
        for moduleID in moduleIDToResult:
            moduleDict = ModuleDataStore._getModuleDictById(moduleID)
            if moduleIDToResult[moduleID] >= 75:
                currentModuleIDs = moduleDict['highScoreNextModules']
                for x in currentModuleIDs:
                    if x not in moduleIDToResult:
                        moduleIDs.append(x)
            else:
                currentModuleIDs = moduleDict['lowScoreNextModules']
                for x in currentModuleIDs:
                    if x not in moduleIDToResult:
                        moduleIDs.append(x)
        modules = ModuleDataStore._getModuleDictsByIds(moduleIDs)
        return modules

    @staticmethod
    def dumpModules():
        modules = []
        modules.append(ModuleDataStore._getModuleDictById('1'))
        modules.append(ModuleDataStore._getModuleDictById('2'))
        modules.append(ModuleDataStore._getModuleDictById('3'))
        return modules

    @staticmethod
    def _getModuleDictsByIds(moduleIDs):
        modules = []
        for moduleID in moduleIDs:
            modules.append(ModuleDataStore._getModuleDictById(moduleID))
        return modules

    @staticmethod
    def _getModuleDictById(moduleID):
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