import collections


class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CodecDFS(object):

    # this should work across object instances
    def serialize(self, root):
        def helper(node, string=''):
            if node is None:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = helper(node.left, string)
                string = helper(node.right, string)
            return string

        return helper(root)

    def deserialize(self, data):
        def helper(dt):
            if dt[0] == 'None':
                return None

            root = TreeNode(dt[0])
            dt.pop(0)  # Terrible terrible idea
            root.left = helper(dt)
            root.right = helper(dt)
            return root

        data_list = data.split(',')
        return helper(data_list)


class CodecBFS(object):

    def serialize(self, root):
        string = ''
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node is None:
                string += 'None,'
                continue
            string += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)

        return string

    def deserialize(self, data):
        data = data.split(',')

        if data[0] == 'None':
            return None
        root = TreeNode(int(data[0]))
        queue = collections.deque()
        queue.append(root)
        i = 1
        while queue and i < len(data):
            node = queue.popleft()
            if data[i] != 'None':
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1
            if data[i] != 'None':
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1
        return root


if __name__ == '__main__':
    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3, left=TreeNode(4)))
    # codec = CodecDFS()
    # print(codec.serialize(root))

    ser = CodecBFS()
    deser = CodecBFS()
    result = deser.deserialize(ser.serialize(None))
