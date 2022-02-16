from inc import *

context = Context()

monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block')

for device in iter(monitor.poll, None):
    if 'ID_FS_TYPE' in device:
        print('{0} partition {1}'.format(device.action, device.device_node))
        partition = device.device_node
        time.sleep(1)
        for p in psutil.disk_partitions():
            # print(p.device)
            if p.device == partition:
                print("  {}: {}".format(p.device, p.mountpoint))
                yarafolder = r'yararules'
                if __name__ == "__main__":
                    scan(p.mountpoint, yarafolder)
                
