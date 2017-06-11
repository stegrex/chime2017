import json

class ModuleDataStore:

    @staticmethod
    def getNextModulesForStudent(moduleIDToResult, languageCode = None):
        moduleIDs = []
        for moduleID in moduleIDToResult:
            moduleDict = ModuleDataStore._getModuleDictById(
                moduleID,
                languageCode
            )
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
        modules = ModuleDataStore._getModuleDictsByIds(moduleIDs, languageCode)
        return modules

    @staticmethod
    def dumpModules(languageCode = None):
        modules = []
        modules.append(ModuleDataStore._getModuleDictById('1', languageCode))
        modules.append(ModuleDataStore._getModuleDictById('2', languageCode))
        modules.append(ModuleDataStore._getModuleDictById('3', languageCode))
        ''''''
        modules.append(ModuleDataStore._getModuleDictById('4', languageCode))
        modules.append(ModuleDataStore._getModuleDictById('5', languageCode))
        modules.append(ModuleDataStore._getModuleDictById('6', languageCode))
        modules.append(ModuleDataStore._getModuleDictById('7', languageCode))
        modules.append(ModuleDataStore._getModuleDictById('8', languageCode))
        modules.append(ModuleDataStore._getModuleDictById('9', languageCode))
        modules.append(ModuleDataStore._getModuleDictById('10', languageCode))
        ''''''
        return modules

    @staticmethod
    def _getModuleDictsByIds(moduleIDs, languageCode = None):
        modules = []
        for moduleID in moduleIDs:
            modules.append(ModuleDataStore._getModuleDictById(
                moduleID,
                languageCode
            ))
        return modules

    @staticmethod
    def _getModuleDictById(moduleID, languageCode = None):
        if languageCode == 'ar':
            languageCodeAppend = '-ar'
        elif languageCode == 'de':
            languageCodeAppend = '-de'
        else:
            languageCodeAppend = ''
        try:
            fileHandler = open(
                'model/modules/module-' + moduleID + languageCodeAppend + '.json'
            )
            moduleJSON = fileHandler.read()
            fileHandler.close()
        except:
            moduleJSON = '{}'
        module = json.loads(moduleJSON)
        try:
            fileHandler = open(
                'model/modules/module-' + moduleID + languageCodeAppend + '.txt'
            )
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