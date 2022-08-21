import inspect
import sys
from time import time
import os

outputRow = {}


def getAllFiles(filePath):
    listOfFile = os.listdir(filePath)
    allFiles = list()

    for entry in listOfFile:
        if entry.endswith(".py"):
            fullPath = os.path.join(filePath, entry)
            if os.path.isdir(fullPath):
                allFiles = allFiles + getAllFiles(fullPath)
            else:
                allFiles.append(fullPath)
        else:
            continue

    return allFiles


def functionParser(filePath):
    filePath = os.getcwd() + filePath
    listOfFile = getAllFiles(filePath)

    for file in listOfFile:
        with open(file, "r") as f:
            contents = f.readlines()

        importStatements = "import sys\n" + 'sys.path.append(r"' + os.getcwd() + '")' + "\nimport time_profiler\n\n"

        for num, line in enumerate(contents, 1):
            if line.startswith("def"):
                num = num - 1
                if contents[num - 1] != "@time_profiler.profiler\n":
                    contents[num] = "@time_profiler.profiler\n" + contents[num]

        with open(file, "w") as f:
            contents = "".join(contents)
            finalContent = importStatements + contents

            if importStatements in contents:
                f.write(contents)
            else:
                f.write(finalContent)


def profiler(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        execTime = t2 - t1

        key = inspect.getfile(func) + ", " + func.__name__ + ", "

        if key in outputRow:
            outputRow[key] += execTime
        else:
            outputRow[key] = execTime

        try:
            with open("exec.log", "r") as f0:
                logContents = f0.readlines()
        except:
            f2 = open("exec.log", "a")
            f2.close()
            with open("exec.log", "r") as f0:
                logContents = f0.readlines()

        if len(logContents) == 0:
            logContents.append('path, method, time\n')

        for num, line in enumerate(logContents, 1):
            if line.startswith(key):
                num = num - 1
                logContents[num] = ""

        with open("exec.log", "w") as f1:
            logContents = "".join(logContents)
            f1.write(logContents)

        f2 = open("exec.log", "a")
        f2.write(key + str(float("{0:.3f}".format(outputRow[key]))) + "\n")

        return result

    return wrap_func


if __name__ == '__main__':
    functionParser(sys.argv[1])
