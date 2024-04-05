from cryptography.fernet import Fernet

'''
If 'key.key' file is not presend in your folder,run this method once and comment it out again                 
def createKey() :                        
    key = Fernet.generate_key()
    with open('key.key', 'wb') as kf :
        kf.write(key)

createKey()
'''

def loadKey() :
    file = open('key.key' , 'rb')
    key = file.read()
    file.close()
    return key

def add(accountName, password) :
    with open('userData.txt', 'a') as f :
        f.write(fer.encrypt(accountName.encode()).decode() + " | " + fer.encrypt(password.encode()).decode() + "\n")

def view() :
    lines = list()
    serialNo = 1
    with open('userData.txt', 'r') as f :
        for line in f.readlines() :
            data = line.rstrip()
            accountName, password = data.split('|')
            newLine = str(serialNo) + '. Account : ' + fer.decrypt(accountName.encode()).decode() \
                                       + ' | Password : ' + fer.decrypt(password.encode()).decode()
            lines.append(newLine)
            serialNo += 1

    return lines

masterPwd = 'asd'
key = loadKey()
fer = Fernet(key)
