#!/bin/python3
#*************************************************

# Author:sanjai sa [Mr Whitehat]

# github :https://github.com/hack-with-ethics 

# created:31-1-2023

# last modified:17-8-2024

#*************************************************

import dns.resolver as domain
import os
import socket
import sys
import pyfiglet
import time

class DnsRecord:
    def __init__(self):
        self.isWrite = False

    def txtRecord(self,dns):
        print(" \n[ + ]==================== Txt Records Info =============================")
        if self.isWrite:
            self.writeFile("\n Txt Record ")
        try:
            for i in domain.resolve(dns,"txt"):
                if self.isWrite:
                    self.writeFile(f"[ * ] Txt Record ==> {i}")
                print("\n\t\t[ * ]Txt Records :",i)
        except:
            print("\t\t [ ! ] Record Error")
            if self.isWrite:
                self.writeFile("None")

    def nsLookup(self,dns):
        print("\n [ + ]==================== Name Server Records Info =============================")
        if self.isWrite:
            self.writeFile("\n Ip Record ")
        try:
            for i in domain.resolve(dns):
                if self.isWrite:
                    self.writeFile(f"[ * ] Ip ==> {i}")
                print(" \n\t\t[ * ] Ip ==> ",i)
        except:
            print(" \t\t[ ! ] No Ns Records")
            if self.isWrite:
                self.writeFile("None")

    def ipV6(self,dns):
        print("\n [ + ]========================= IpV6 Records Info ============================")
        if self.isWrite:
            self.writeFile("\n Ipv6 Record ")
        try:
            for i in domain.resolve(dns,"AAAA"):
                if self.isWrite:
                    self.writeFile(f"[ * ]IpV6 ==> {i}")
                print(" \n\t\t[ * ]IpV6 ==> ",i)
                
        except:
            print(" \t\t[ ! ] Resolve Error")
            if self.isWrite:
                self.writeFile("None")
    def dnsRecord(self,dns):
        print("\n [ + ]============================ Dns Records  ===========================")
        if self.isWrite:
            self.writeFile("\n Dns Record ")
        try:
            for i in domain.resolve(dns,"ns"):
                if self.isWrite:
                    self.writeFile(f"[ * ]Dns ==> {i}")
                print("\n\t\t[ * ]Dns Record :",i)
        except:
            print("\t\t [ ! ] Record Error")
            if self.isWrite:
                self.writeFile("None")

    def mailServerInfo(self,dns):
        print("\n [ + ]============================ Mailserver Records  ===========================")
        if self.isWrite:
            self.writeFile("\n Mail Record ")
        try:
            for i in domain.resolve(dns,"mx"):
              
                if self.isWrite:
                    self.writeFile(f"[ * ]MailServer Info ==> {i}")
                print("\n\t\t[ * ]Mail Server :",i)
        except:
            print("\t\t [ ! ]Mail  Record Error")
            if self.isWrite:
                self.writeFile("None")
    def zoneTransferRecords(self,dns):
        print(" [ + ]==================== Zone Transfer Info  =============================")
        if self.isWrite:
            self.writeFile("\n Mail Record ")
        try:
            for i in domain.resolve(dns,"soa"):
                if self.writeFile:
                    self.writeFile(f"[ * ]Zone Transfer Info ==> {i}")
      
                print("\n\t\t[ * ]Zone TransferInfo  :",i)
        except:
            print("\t\t [ ! ]Zone Transfer Record Error")
            if self.isWrite:
                self.writeFile("None")

    def isHostOnline(self,dns):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((dns,80))
            return True
        except:
            return False
    def cls(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    def writeFile(self,data):
        if os.path.exists(sys.argv[2]):
            with open(sys.argv[2],'a') as File:
                File.write("\n"+data)
                File.close()
        else:
            with open(sys.argv[2],'w') as File:
                File.write("\n"+data)
                File.close()
            
    def main(self):
        if len(sys.argv) >=2 and self.isHostOnline(sys.argv[1]):
            self.cls()
            if len(sys.argv) == 3:
                self.isWrite = True
            time.sleep(0.5)
            pyfiglet.print_figlet(" \t\t\tD n s R e c on ")
            print(" ="*50)
            time.sleep(0.2)
            print(" \n[+] Dns Provided : ",sys.argv[1])
            time.sleep(0.1)
            try:
                print(" \n[+] Ip Address Resolved :",socket.gethostbyname(sys.argv[1]))
            except:
                print(" \n[ ! ]Ip Address Resolved : Error")
            time.sleep(0.1)
            if self.isWrite:
                print("\n[ + ]Output File : ",sys.argv[2])
            else:
                print(" \n[ * ]File Write :",self.isWrite)
            time.sleep(0.1)
            print(" \n[+] Status : Online")
            time.sleep(0.1)
            print(" ="*50)
                
            self.nsLookup(sys.argv[1])
            self.ipV6(sys.argv[1])
            self.txtRecord(sys.argv[1])
            self.mailServerInfo(sys.argv[1])
            self.dnsRecord(sys.argv[1])
        else:
            self.usage()
            

    def usage(self):
        self.cls()
        print(" \n \t\t\t\t[ use ]DnsRecon Tool Fetch all The Dns Records [ ! ]")
        
        print(f" \n\n[ * ] usage : {sys.argv[0]} < domain > <outputfile>.txt ")
        print(" \n\n\tDomain - specify the domain Name [google.com , youtube.com]")
        print(" \n\n\toutputfile.txt - file for output file write")

        print("\n\n [ ! ] Error May be due to Offline Domain")
        
     

M = DnsRecord()
M.main()
