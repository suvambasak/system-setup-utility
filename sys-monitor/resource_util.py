import psutil
import sys
import matplotlib.pyplot as plt


pid = int(sys.argv[1])

if psutil.pid_exists(pid):
    process = psutil.Process(pid)

cpu = []
mem = []
total_mem = psutil.virtual_memory().total

try:
    while process.is_running():
        cpu.append(process.cpu_percent(interval=1))
        mem.append((total_mem*process.memory_percent())/104857600)
except Exception as e:
    print(str(e))
finally:
    plt.subplot(1, 2, 1)
    plt.title("CPU Utilization")
    plt.xlabel("Time(s)")
    plt.ylabel("CPU(%)")
    plt.plot(cpu, marker='o')

    plt.subplot(1, 2, 2)
    plt.title("Memory Utilization")
    plt.xlabel("Time(s)")
    plt.ylabel("Memory(MB)")
    plt.plot(mem, marker='o')

    plt.tight_layout(w_pad=2)
    # plt.show()
    plt.savefig(str(pid)+'.png', dpi=1000)
