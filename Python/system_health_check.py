import socket,shutil,psutil

def check_localhost():
    localhost=socket.gethostbyname('localhost')
    return localhost=='127.0.0.1'

def check_disk_usage(disk):
    '''Verifies that there's enough free space on disk'''
    du=shutil.disk_usage(disk)
    free=du.free / du.total*100
    return free>20

def check_memory_usage():
    '''Verifies that there's enough free space on disk'''
    mu=psutil.virtual_memory().available
    total=mu/(1024.0**2)
    return total>500

def check_cpu_usage():
    '''Verifies that there's enough unused CPU'''
    usage=psutil.cpu_percent(1)
    return usage<80

if not check_cpu_usage():
    print('⚠️ - CPU usage is over 80%')
else:
    print('CPU is operating within normal parameters')

if not check_memory_usage():
    print('⚠️ - Available memory is less than 500MB')
else:
    print('Memory is operating within normal parameters')

if not check_disk_usage('/'):
    print('⚠️ - Available disk space is less than 20%')
else:
    print('Disk is operating within normal parameters')

if not check_localhost():
    print('⚠️ - localhost cannot be resolved to 127.0.0.1')
else:
    print('Localhost is operating within normal parameters')
