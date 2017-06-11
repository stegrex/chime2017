import json
import lib.bottle.bottle as bottle
from model.student_data_store import StudentDataStore
from model.module_data_store import ModuleDataStore

mainApp = bottle.Bottle()

@mainApp.get('/api/student')
@mainApp.get('/api/student/')
def student():
    method = bottle.request.GET.get('method')
    inputJSON = bottle.request.GET.get('input')
    if inputJSON == None:
        inputJSON = '{}'
    inputDict = json.loads(inputJSON)
    data = []
    if method == 'getStudentsForTeacher':
        students = StudentDataStore.getStudentsForTeacher(inputDict)
        for student in students:
            data.append(student.to_dict())
    return json.dumps(data)

@mainApp.get('/api/module')
@mainApp.get('/api/module/')
def module():
    method = bottle.request.GET.get('method')
    inputJSON = bottle.request.GET.get('input')
    if inputJSON == None:
        inputJSON = '{}'
    inputDict = json.loads(inputJSON)
    data = []
    if method == 'getNextModulesForStudent':
        modules = ModuleDataStore.getNextModulesForStudent(inputDict)
        for module in modules:
            data.append(module)
    return json.dumps(data)

# Local dev machine only:
#bottle.run(mainApp, host = 'localhost', port = 8080)

# PRODUCTION:
bottle.run(mainApp, host = '0.0.0.0', port = 80)