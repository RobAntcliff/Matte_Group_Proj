import time

def initLogFile(fileName):
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S")
        logFileName = fileName[:-4] + '_' + current_time + '.log'
        with open('log_folder/' + logFileName, 'w') as f:
                f.write(current_time + ': ' + fileName + ' was selected for use.\n')
        logs{path} = logFileName

def updateLogFile(filePath, entry):
        fileName = logs[filePath]
        with open('log_folder/' + fileName, 'w') as f:
                f.write(time.strftime("%Y-%m-%d-%H-%M-%S") + ': ' + entry)

