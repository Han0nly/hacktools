import crypt
def testpass(crypt_pwd):
    salt=crypt_pwd[:2]
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if (crypt_pwd==cryptWord):
            print'[+] Found Password:'+word+"\n"
            return
    print "[-] Password Not Found.\n"
if __name__ == '__main__':
    pwd_file = open('passwords.txt')
    for line in pwd_file:
        if ":" in line:
            username = line.split(':')[0]
            crypt_pwd = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For:"+ username
            testpass(crypt_pwd)