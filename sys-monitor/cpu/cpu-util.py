import os
import sys
import time
import json
import psutil
import matplotlib.pyplot as plt


def cleanup():
    'Delete TOP command output files'
    for file in os.listdir('./data'):
        os.remove(f'./data/{file}')


def plot(cpu_load):
    'Plotting the graph'

    # Create graph
    plt.title("CPU Utilization")
    plt.xlabel("Time(s)")
    plt.ylabel("CPU(%)")
    plt.plot(
        cpu_load, label=f'MAX: {round(max(cpu_load),1)} %\nAVG: {round(sum(cpu_load)/len(cpu_load),1)} %')
    plt.legend()
    plt.ylim([0, 100])

    # File name is process ID unless the name given from cmd line arg
    file_name = f'./snaps/{sys.argv[1]}-cpu.png' if len(
        sys.argv) > 1 else f'./snaps/{os.getpid()}-cpu.png'

    print(f'\nImage Saved: {file_name}')
    plt.savefig(file_name, dpi=1000)


def generate_result():
    '''Process text files and generate the result'''

    # Index of the relevent fields
    PID = 0
    CPU = 8
    COMMAND = -1

    # Aggregated CPU load in each seconds
    cpu_load = []
    file_name = 0

    # For each file inside `data` directory
    for _ in os.listdir('./data'):
        # Reading each file of top output
        file_path = f'./data/{file_name}'
        top_output = open(file_path, 'r').read().strip().split('\n')
        cpu = 0.0

        # Filtering out the relevent process and extracting CPU %
        for process_index in range(7, len(top_output)):
            process_details = top_output[process_index].split()
            if str(os.getpid()) != process_details[PID] and process_details[COMMAND] in ('pip3', 'python3', 'opera', 'ansible-playboo', 'sshd'):
                cpu += float(process_details[CPU])
                # print(
                #     f'{process_details[PID]}, {process_details[CPU]}, {process_details[COMMAND]}')
        file_name += 1

        # Converting and mapping with 100% CPU utilization
        cpu_load.append(round((cpu/psutil.cpu_count()), 1))

    # print(cpu_load)

    # Stripping out 0.0% utilization of start and end
    start = 0
    end = 1
    while cpu_load[start] == 0.0:
        start += 1
    while cpu_load[-end] == 0.0:
        end += 1
    # print(cpu_load[start: -(end-1)])

    # File name is process ID unless the name given from cmd line arg
    file_name = f'./json/{sys.argv[1]}-cpu.json' if len(
        sys.argv) > 1 else f'./json/{os.getpid()}-cpu.json'

    # Saving Data into JSON file
    data = dict()
    data['cpu_load'] = cpu_load[start: -(end-1)]
    with open(file_name, 'w') as json_file:
        json_file.write(json.dumps(data, indent=1))
    print(f'\nJSON Saved: {file_name}')

    # Plot graph
    plot(cpu_load[start: -(end-1)])


file_id = 0
try:
    # Ensure path exist
    if not os.path.exists('./data'):
        os.mkdir('./data')
    if not os.path.exists('./json'):
        os.mkdir('./json')

    # Running shell command `top` in batch mode and output redirected to text file each second
    print('\nStarted...')
    while True:
        file_name = f'./data/{file_id}'
        os.system(f'top -bn1 > {file_name}')
        file_id += 1
        time.sleep(1)
except KeyboardInterrupt as e:
    print('\nStoping..')
finally:
    print('\nProcessing..')
    generate_result()
    cleanup()
    print('\nDone.')
