import psutil
import time
import os
import sys
import matplotlib.pyplot as plt

mem = []
total_mem = psutil.virtual_memory().total

try:
    print('Started...')
    while True:
        m = 0
        for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_percent']):
            if proc.info['pid'] != os.getpid() and proc.info['name'] in ('pip3', 'python3', 'opera', 'ansible-playboo'):
                # print(proc.info)
                m += proc.info['memory_percent']
        if m:
            mem.append((total_mem*m)/104857600)
        time.sleep(1)

except KeyboardInterrupt as e:
    print('Stopping..')

finally:
    plt.title("Memory Utilization")
    plt.xlabel("Time(s)")
    plt.ylabel("Memory(MB)")
    plt.plot(mem, marker='o',
             label=f'MAX: {round(max(mem),1)} MB\nAVG: {round(sum(mem)/len(mem),1)} MB')
    plt.legend()

    file_name = f'./snaps/{sys.argv[1]}-mem.png' if len(
        sys.argv) > 1 else f'./snaps/{os.getpid()}-mem.png'

    plt.savefig(file_name, dpi=1000)
