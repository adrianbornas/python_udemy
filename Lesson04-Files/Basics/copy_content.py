with open('trial.txt', 'r', encoding='utf8') as trialFile:
    with open('copy.txt', 'w', encoding='utf8') as copyFile:
        copyFile.write(trialFile.read())
        print('Content of trial.txt file copied successfully!')
