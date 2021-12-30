import os
import sys
import time
import psutil
import matplotlib.pyplot as plt


def cleanup():
    for file in os.listdir('./data'):
        os.remove(f'./data/{file}')


def plot(cpu_load):
    plt.title("CPU Utilization")
    plt.xlabel("Time(s)")
    plt.ylabel("CPU(%)")
    plt.plot(cpu_load, marker='o',
             label=f'MAX: {round(max(cpu_load),1)} %\nAVG: {round(sum(cpu_load)/len(cpu_load),1)} %')
    plt.legend()

    file_name = f'./snaps/{sys.argv[1]}-mem.png' if len(
        sys.argv) > 1 else f'./snaps/{os.getpid()}-mem.png'

    plt.savefig(file_name, dpi=1000)


def generate_result():
    PID = 0
    CPU = 8
    COMMAND = -1
    cpu_load = []

    file_name = 0
    for _ in os.listdir('./data'):
        file_path = f'./data/{file_name}'
        top_output = open(file_path, 'r').read().strip().split('\n')
        cpu = 0.0
        for process_index in range(7, len(top_output)):
            process_details = top_output[process_index].split()
            if str(os.getpid()) != process_details[PID] and process_details[COMMAND] in ('pip3', 'python3', 'opera', 'ansible-playboo'):
                cpu += float(process_details[CPU])
                # print(
                #     f'{process_details[PID]}, {process_details[CPU]}, {process_details[COMMAND]}')
        file_name += 1
        cpu_load.append(round((cpu/psutil.cpu_count()), 1))

    # print(cpu_load)
    start = 0
    end = 1
    while cpu_load[start] == 0.0:
        start += 1
    while cpu_load[-end] == 0.0:
        end += 1
    # print(cpu_load[start: -(end-1)])
    plot(cpu_load[start: -(end-1)])


file_id = 0
try:
    print('Started...')
    while True:
        file_name = f'./data/{file_id}'
        os.system(f'top -bn1 > {file_name}')
        file_id += 1
        time.sleep(1)
except KeyboardInterrupt as e:
    print('Stoping..')
finally:
    generate_result()
    cleanup()
