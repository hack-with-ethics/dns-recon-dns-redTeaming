#!/bin/bash
#*************************************************
#Author:hack_with_ethics
#created:31-1-2023
#last modified=31-1-2023
#*************************************************

import dns.resolver
#import statement
import socket  

print("[+]RED-TEAMING-DNS==>Information-Gathering<")

print("[+]GETTING DNS INFORMATION:")

def check():

	global dns

	if choice=="1":

		print("\n[+]YOU HAVE SELECTED NSlookup-info:")

		dns=dns.resolver.resolve(host) 



		for i in dns:

			print(f"[+]IP-INFORMATION {host}:",i)

	elif choice=="2":

		print("\n[+] YOU HAVE SELECTED ipV6-info:")



		dns=dns.resolver.resolve(host,"AAAA")


		for i in dns:
			print(f"IPV6-INFO {host}",i)
	elif choice=="3":

		print("[+]YOU HAVE SELECTED dns-record:")



	
		try:

			dns=dns.resolver.resolve(host,"NS")

			for i in dns:

				print("[+]DNS-RECORD",i)

		except:

			print("host error")

	elif choice=="4":

		print("[+] YOU HAVE SELECTED TXT-record:")

		try:

			dns=dns.resolver.resolve(host,"TXT")

	
			for i in dns:
				print("TXT-record:",i)
		except:
			print("no txt Record found")

	elif choice=="5":

		print("[+] YOU HAVE SELECTED mail-server-info:")

		try:
			dns=dns.resolver.resolve(host,"MX")
			for i in dns:
				print(f"[+]MAIL-SERVER-INFO {host}:",i)
		except:
			print(f"mail-server-info not found for {host}")

	elif choice=="6":

		print("[+]YOU HAVE SELECTED zone Transfer-info:")

		try:
			dns=dns.resolver.resolve(host,"SOA")

			for i in dns:
				print(f"[+]zone Transfer-info {host}:",i)
		except:
			print(f"not zone Transfer-info {host}")

print("\n1.NSlookup-info\n2.ipV6-info:\n3.dns-record:\n4.TXT-record:\n5.mail-server-info:\n6.zone Transfer-info:")

choice=input("\n[+]ENTER THE CHOICE:")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input("\n[+]ENTER THE HOST NAME:")



s.connect((host,80))

if s:
	print(f"\n[+]HOST {host} IS ALIVE")
	check()
else:
	print("\n[+]HOST IS NOT ALIVE")

