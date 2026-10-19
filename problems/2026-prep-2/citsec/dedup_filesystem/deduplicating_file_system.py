import uuid
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Content:
    data: str
    ref_count: int
    size: int
    hash_value: int | None


class DedupFileSystem: 

    def __init__(self):
        self.paths = {} # path -> content_id
        self.index = defaultdict(set) #store data_size -> set of content_id
        self.content = {} # contentid -> content

    def writefile(self, path: str, data: str) -> None:
        
        if path is None or data is None:
            raise Exception("Data or path to data must be provided.")

        # if the path already exists, we want to release it from 
        # the contentid and write a new content id for that path.
        if path in self.paths:
            self._release(path)

        data_size = len(data)

        if data_size in self.index:
            for content_id in self.index[data_size]:
                content: Content = self.content[content_id]
                if self._hash_of(content) != hash(data):
                    continue

                # Check data also for hash collision
                if data != content.data:
                    continue

                # we have a match so we point
                self.paths[path] = content_id
                content.ref_count += 1
                return

        # Here we don't find it in datasize and not in self.paths so we create a new one. 
        content_id = uuid.uuid4()
        self.content[content_id] = Content(data, 0, data_size, None)
        self.paths[path] = content_id
        self.index[data_size].add(content_id)

    def readfile(self, path: str) -> str:
        if path not in self.paths:
            raise FileNotFoundError("The file was not found")
        
        content: Content = self.content[self.paths[path]]
        return content.data

    def _hash_of(self, content: Content) -> str:
        if content.hash_value is None:
            content.hash_value = hash(content.data)
        return content.hash_value

    # this is to remove a reference of the path to the content. 
    # and if there is no reference, remove the content. 
    def _release(self, path: str) -> None:
        content_id = self.paths[path]
        content: Content = self.content[content_id]
        content.ref_count -= 1
        if content.ref_count == 0:
            del self.content[content_id]
            bucket = self.index[content.size]
            bucket.discard(content_id) 
            if not bucket:
                del self.index[content.size]


    def delete(self, path: str) -> str:
        if path not in self.paths:
            raise FileNotFoundError(f"File {path} was not found")

        self._release(path)
        del self.paths[path]
