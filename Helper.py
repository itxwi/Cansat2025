import json
import os

def getState():
    try:
        with open('state.json', 'r') as file:
            state = json.load(file)
    except FileNotFoundError:
        # Default coordinator is king_william
        state = {
            'cwd': os.getcwd(), #fix this later
            'coordinator': f'{os.getcwd()}/coordinators/king_william.py',
            'velocity': [0,0,0],
            'orientation':[0,0,0]
        }
        with open('state.json', 'w') as file:
            json.dump(state, file, indent=4)
    
    return state

def getLog():
    try:
        with open('log.json', 'r') as file:
            log = json.load(file)
    except FileNotFoundError:
        # Default coordinator is king_william
        log = {

        }
        with open('log.json', 'w') as file:
            json.dump(log, file, indent=4)
    
    return log

def writeLog(newLog): #not recommended
    with open('log.json','w') as file:
        json.dump(newLog,file,indent=4)
    
    return newLog