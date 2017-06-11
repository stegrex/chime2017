class ModuleDataStore:

    @staticmethod
    def getNextModulesForStudent(studentID):
        modules = []
        module = Module()
        module.name = 'Algebra'
        module.age = 10
        module.language = 'Thai'
        module.locale = 'US'
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