def kill_process(pid, ppid, kill):
    killed = []

    queue = [kill]
    while queue:
        val = queue.pop(0)
        # look for all indices of the ppid and get the children
        indices = []
        for idx, pp_id in enumerate(ppid):
            if pp_id > 0:  # it's not a start ip process
                if val == pp_id:
                    indices.append(idx)

        # Append all pid at indices to queue
        for idx in indices:
            queue.append(pid[idx])
        killed.append(val)

    return killed


def kill_proc(pid, ppid, kill):
    mp = dict()
    for idx in range(len(ppid)):
        l = mp.get(ppid[idx], [])
        l.append(pid[idx])
        mp[ppid[idx]] = l

    killed = []
    queue = [kill]
    while queue:
        val = queue.pop(0)
        killed.append(val)
        if val in mp:
            queue += mp[val]
    return killed


if __name__ == '__main__':
    pid = [1, 3, 10, 5, 11, 12, 14, 15]
    ppid = [3, 0, 5, 3, 5, 10, 12, 11]
    killed_processes = kill_proc(pid, ppid, 5)
    print(killed_processes)
