from HandlerClass.FileHandler import FileHandler

with FileHandler('trial.txt') as trialFile:
    print(trialFile.read())
