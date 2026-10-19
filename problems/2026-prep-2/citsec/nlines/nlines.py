import os
import sys
import mmap

MAX_CHUNK = 1 << 20 # 1mb cap on chunks

# we return the position where n starts from. so we aim to read
# from that position to the end of file
def tail_start(fd: int, size: int, n: int) -> int:
    """ Byte offset where the last n lines begin """
    
    if n <= 0 or size == 0:
        return size
    
    # some files may have \n at the end.
    end = size - 1 if os.pread(fd, 1, size - 1) == b"\n" else size
    
    # reading in 4kb chunks
    position, seen, chunk = end, 0, 4096
    while position > 0:
        length = min(chunk, position)
        position -= length
        buf = os.pread(fd, length, position)
        
        count = buf.count(b"\n") # number of \ns will be tell me how many we have seen
        if seen + count < n:
            seen += count
            # Increase chunk size to read next. we can decide to keep reading in 
            # fixed chunks instead of doubling
            chunk = min(chunk * 2, MAX_CHUNK) 
            continue
        
        i = len(buf)
        while True:
            i = buf.rfind(b"\n", 0, i)
            seen += 1
            if seen == n:
                return position + i + 1
            
    return 0 

def write_range(fd: int, offset: int, size: int) -> None:
    out = sys.stdout.buffer
    out.flush()
    
    while offset < size:
        sent = os.sendfile(out.fileno(), fd, offset, size - offset)
        if sent == 0:
            break
        offset += sent
    

def tail(path: str, n: int) -> None:
    with open(path, "rb") as f:
        fd = f.fileno()
        size = os.fstat(fd).st_size
        tail_nstart = tail_start(fd, size, n)
        write_range(fd, tail_nstart, size)



# mmap version of all of the above. 
def tail_start_mmap(fd: int, size: int, n: int) -> int:
    
    if n <= 0 or size == 0:
        return size
    
    with mmap.mmap(fd, 0, access=mmap.ACCESS_READ) as m:
        position = size - 1 if m[-1] == 0x0A else size
        # above can also be written as i = size - 1 if m[-1:] == b"\n" else size
        for _ in range(n):
            position = m.rfind(b"\n", 0, position)
            if position == -1:
                return 0
            
            
    out = sys.stdout.buffer
    out.flush
    while position < size:
        sent = os.sendfile(out.fileno(), fd, position, size - position)
        if sent == 0:
            break
        position += sent
    

# This is the chunked version of the above.
def tail_start_mmap_chunk(f, n: int) -> int:
    size = f.seek(0, os.SEEK_END)
    if n <= 0 or size == 0:
        return size
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        end = size - 1 if m[size - 1] == 0x0A else size
        pos, seen = end, 0
        while pos > 0:
            start = max(0, pos - 1 << 20)
            cnt = m[start:pos].count(b"\n")     # one C call per chunk
            if seen + cnt < n:
                seen += cnt
                pos = start
                continue
            i = pos                              # answer is in [start, pos)
            while True:
                i = m.rfind(b"\n", start, i)
                seen += 1
                if seen == n:
                    return i + 1
        return 0
    