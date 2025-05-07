import platform
import psutil

def check_computer_specs():
    print("=== Computer Specifications ===")
    
    # OS Info
    print(f"System      : {platform.system()}")
    print(f"Version     : {platform.version()}")
    print(f"Release     : {platform.release()}")
    
    # CPU Info
    print(f"Processor   : {platform.processor()}")
    print(f"CPU Cores   : {psutil.cpu_count(logical=False)} physical / {psutil.cpu_count()} logical")
    
    # RAM Info
    ram_gb = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    print(f"RAM         : {ram_gb} GB")
    
    # Disk Info
    disk = psutil.disk_usage('/')
    disk_gb = round(disk.total / (1024 ** 3), 2)
    print(f"Disk        : {disk_gb} GB")

# Run the function
check_computer_specs()
