import psutil
partition = psutil.disk_partitions()
test = psutil.disk_mountpoints()
print(type(partition))
print(test)
#print(partition)
#for mountpoint in disk_partitions :
print (psutil.mountpoint) 
handle = open('/dev/disk2', 'rb')
print (handle)