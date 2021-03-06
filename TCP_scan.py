import optparse
from socket import *
from threading import *
screenlock = Semaphore(value = 1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenlock.acquire()
        print '[+]%d/tcp open' % tgtPort
        print '[+] ' + str(results)
        connSkt.close()
    except:
        screenlock.acquire()
        print '[-]%s/tcp closed' % tgtPort
    finally:
        screenlock.release()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host" % tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Result for: ' + tgtName[0]
    except:
        print '\n[+] Scan Result for: ' + tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, tgtPort)


def main():
    parser = optparse.OptionParser("usage%prog  -H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print '[-] You must specify a target host and port[s]'
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
