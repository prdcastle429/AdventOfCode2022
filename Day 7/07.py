directories = []
global currDirectory
totalSum = 0

class Directory:
    def __init__(self, name, parent_directory=None):
        self.name = name
        self.childDirectories = []
        self.parentDirectory = parent_directory
        self.totalSize = 0

    def add_file_size(self, size):
        self.totalSize += size

    def add_child_directory(self, directory):
        self.childDirectories.append(directory)

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        lineInput = line.split(" ")
        argOne = lineInput[1]
        if argOne == "cd":
            argTwo = lineInput[2]
            if argTwo != "..":
                if len(directories) == 0:
                    currDirectory = Directory(lineInput[2])
                    directories.append(currDirectory)

                if currDirectory.childDirectories:
                    currDirectory = [directory for directory in currDirectory.childDirectories if directory.name == lineInput[2]]
                    currDirectory = currDirectory[0]

            else:
                currDirectory = currDirectory.parentDirectory

        if lineInput[0] == "dir":
            newChildDir = Directory(lineInput[1], currDirectory)
            directories.append(newChildDir)
            currDirectory.add_child_directory(newChildDir)

        if lineInput[0].isdigit():
            currDirectory.add_file_size(int(lineInput[0]))
            if currDirectory.parentDirectory:
                nextParentDirectory = currDirectory.parentDirectory
                while nextParentDirectory:
                    nextParentDirectory.add_file_size(int(lineInput[0]))
                    nextParentDirectory = nextParentDirectory.parentDirectory


# Part One Solution
for directory in directories:
    if directory.totalSize <= 100000:
        totalSum += directory.totalSize

print("Total sum of all directory sizes under 100000: " + str(totalSum))


#Part Two Solution
unusedSpace = 70000000 - directories[0].totalSize
neededSpace = 30000000 - unusedSpace

minSizeOfDirectory = unusedSpace
for directory in directories:
    if neededSpace <= directory.totalSize < minSizeOfDirectory:
        minSizeOfDirectory = directory.totalSize

print("Size of smallest directory that can be deleted: " + str(minSizeOfDirectory))