def kill_process(pid, ppid, kill):
    killed = [kill]

    if kill in ppid:
        # get all indices where
        kill_idx = ppid.index(kill)

    return killed


if __name__ == '__main__':
    pid = []
    ppid = []
    killed_processes = kill_process(pid, ppid, 10)
    print(killed_processes)
