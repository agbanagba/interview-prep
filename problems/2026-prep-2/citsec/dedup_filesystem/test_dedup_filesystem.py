
import pytest
from deduplicating_file_system import DedupFileSystem


@pytest.fixture
def fs():
    return DedupFileSystem()

def test_write_then_read(fs):
    fs.writefile("/a/b/c.txt", "hello")
    assert fs.readfile("/a/b/c.txt") == "hello"


def test_identical_content_stored_once(fs):
    fs.writefile("/a/b/c.txt", "hello")
    fs.writefile("/a/b/e.txt", "hello")

    assert fs.readfile("/a/b/c.txt") == "hello"
    assert fs.readfile("/a/b/e.txt") == "hello"


def test_same_size_different_content_stored_separately(fs):
    fs.writefile("empty", "")
    fs.writefile("empty2", "")
    assert fs.readfile("empty") == ""


def test_read_missing_raises(fs):
    with pytest.raises(FileNotFoundError):
        fs.readfile("missing")


def test_delete_missing_raises(fs):
    with pytest.raises(FileNotFoundError):
        fs.delete("missing")