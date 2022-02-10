import psutil
import glob
import hashlib
import time
from pyudev import Context, Monitor
import pyudev

def hash_file(filename):
   """"This function returns the SHA-1 hash
       of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   #return the hex representation of digest
#    print(h.hexdigest())
   return h.hexdigest()

#virus database
virus_hash = ['6eef567354ffe2a5efd16ffd9c3a23013fc98b98', 'dd4d4d63b6fa353ac5c61f9c7834316a49ab6159', '1da6d2e50d7ad9a46ddf72247c0d44db9dd17af3']

context = Context()

monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block')

for device in iter(monitor.poll, None):
    if 'ID_FS_TYPE' in device:
        print('{0} partition {1}'.format(device.action, device.device_node))
        partition = device.device_node
        time.sleep(1)
        for p in psutil.disk_partitions():
            #print(p.device)
            if p.device == partition:
                print("  {}: {}".format(p.device, p.mountpoint))
                files = glob.glob(p.mountpoint + "/*.txt")
                print("list of files:")
                for f in files:
                    print("\t"+f)
                    if(hash_file(f) in virus_hash):
                        print("USB HAS VIRUS")
                        break;

