import psutil, os, sys
from optparse import OptionParser

DiskList = os.system("diskutil list") 
user_input = input("Choose Your Disk ex) /dev/disk2 : ")


handle = open(user_input, 'rb')
print (handle)
handle.seek(1024)
mbr = handle.read(512)

if ord(chr(mbr[510])) == 0x55 and ord(chr(mbr[511])) == 0xAA :
	print ('MBR Read Success')
else :
	print ('MBR Read Fail')

print (mbr)