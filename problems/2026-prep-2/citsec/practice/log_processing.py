
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Iterable, Iterator

from collections import deque

LEVELS = {"debug": 10, "info": 20, "warn": 30, "error": 40, "fatal": 50}

@dataclass(slots=True)
class Record:
    ts: datetime
    level: str
    service: str
    fields: dict = field(default_factory=dict)
    msg: str = ""
    raw: str = ""

def parse(line: str) -> Record | None:
    
    parts = line.rstrip("\n").split(" ", 3)
    if len(parts) < 3:
        return None
    
    ts_s, level, service = parts[0], parts[1], parts[2]
    try:
        ts = datetime.fromisoformat(ts_s)
    except ValueError:
        return None
    
    fields, words = {}, []
    if len(parts) == 4:
        for token in parts[3].split():
            k, sep, v = token.partition("=")
            if sep and k:
                fields[k] = v
            else:
                words.append(token)
    return Record(ts, level, service, fields, " ".join(words), line.rstrip("\n"))


def error_burst_alerts(lines: Iterable[str], window_s: float, threshold: int):
    win = timedelta(seconds=window_s)
    q = deque()
    firing = False
    
    alerts = []
    for r in records(lines):
        if LEVELS.get(r.level, 0) < LEVELS["error"]:
            continue
        
        q.append(r.ts)
        
        # remove timestamps from entry while there are entries and 
        # while current item 
        while q and r.ts - q[0] >= win:
            q.popleft()
        if len(q) >= threshold and not firing:
            alerts.append((r.ts, len(q)))
            firing = True
        elif len(q) < threshold:
            firing = False
    
    return alerts


# Given request timestamps sorted by time, find the 60s window with the most requests. 
def busiest_window(ts, window):
    best = (0, None, None)
    left = 0
    for right in range(len(ts)):
        while ts[right] - ts[left] >= window:
            left += 1
            
        # we are at the window
        count = right - left + 1
        if count > best[0]:
            best = (count, ts[left], ts[right])
            
    return best

def top_k_error_services(lines: Iterable[str], k: int):
    pass

# latency percentiles per service.
def percentile():
    pass


def records(lines) -> Iterator[Record]:
    for line in lines:
        r = parse(line)
        if r is not None:
            yield r
            
