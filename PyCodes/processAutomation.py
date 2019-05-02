import psutil


def processDisp():
    listProcesses = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listProcesses.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listProcesses


def main():
    print("ProcessMonitor")
    listProcess = processDisp()

    for elem in listProcess:
        print(elem)


if __name__ == '__main__':
    main()
