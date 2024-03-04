# With this way Python manages file open and close
with open('trial.txt', 'r', encoding='utf8') as trialFile:
    # Read all file content
    # print(trialFile.read())

    # Read num of characters
    # print(trialFile.read(5))

    # Read line
    # print(trialFile.readline())

    # Access to specific line
    print(trialFile.readlines()[1])
