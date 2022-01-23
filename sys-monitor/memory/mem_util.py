import psutil
import time
import os
import sys
import json
import matplotlib.pyplot as plt

# Memory use of each second
mem = []
# Total available memory
total_mem = psutil.virtual_memory().total

try:
    print('\nStarted...')

    # Scanning all the running processes
    while True:
        m = 0
        for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_percent']):
            # Filter out relevant processes and aggregate mem usage of these
            if proc.info['pid'] != os.getpid() and proc.info['name'] in ('pip3', 'python3', 'opera', 'ansible-playboo', 'sshd'):
                # print(proc.info)
                m += proc.info['memory_percent']
        if m:
            # Convert % to MB and add to the list
            mem.append((total_mem*m)/104857600)
        time.sleep(1)

except KeyboardInterrupt as e:
    print('\nStopping...')

finally:
    # Create Graph
    print('\nProcessing...')
    plt.title("Memory Utilization")
    plt.xlabel("Time(s)")
    plt.ylabel("Memory(MB)")
    plt.plot(
        mem, label=f'MAX: {round(max(mem),1)} MB\nAVG: {round(sum(mem)/len(mem),1)} MB')
    plt.legend()

    # File name is process ID unless the name given from cmd line arg
    graph_file_name = f'./snaps/{sys.argv[1]}-mem.png' if len(
        sys.argv) > 1 else f'./snaps/{os.getpid()}-mem.png'
    json_file_name = f'./json/{sys.argv[1]}-mem.json' if len(
        sys.argv) > 1 else f'./json/{os.getpid()}-mem.json'

    plt.savefig(graph_file_name, dpi=1000)
    print(f'\nImage Saved: {graph_file_name}')

    # Saving data as JSON file
    data = dict()
    data['mem'] = mem
    with open(json_file_name, 'w') as json_file:
        json_file.write(json.dumps(data, indent=1))
    print(f'\nJSON Saved: {json_file_name}')

    print('\nDone.')
