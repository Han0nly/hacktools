import ftplib
import optparse
def annoLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','me@your.com')
        print '\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded'
        ftp.quit()
        return True
    except Exception,e:
        print '\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed'
def main():
    parse = optparse.OptionParser('usage%prog -H <hostname>')
    parse.add_option('-H',dst='hostname',type='string',help='specify a hostname')
    (options,args) = parse.parse_args()
    hostname = options.hostname
    annoLogin(hostname)
if __name__ == '__main__':
    main()