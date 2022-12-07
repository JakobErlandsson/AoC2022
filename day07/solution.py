from os import getenv


class File:

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:

    def __init__(self, name: str, parent):
        self.name = name
        self.files = []
        self.dirs = []
        self.parent = parent

    def size(self) -> int:
        return sum([f.size for f in self.files]) + sum([d.size() for d in self.dirs])

    def get_subdir(self, name: str):
        for d in self.dirs:
            if d.name == name:
                return d


class Solution:

    def __init__(self):
        self.commands = open('input.txt', 'r').read().split('\n')
        self.root = None

    def explore(self):
        current_dir = None
        i = 0
        while i < len(self.commands):
            com = self.commands[i].split(' ')
            if com[1] == 'cd':
                if com[2] == '..':
                    current_dir = current_dir.parent
                elif not current_dir:
                    current_dir = Directory(com[2], None)
                    self.root = current_dir
                else:
                    current_dir = current_dir.get_subdir(com[2])
                i += 1
            elif com[1] == 'ls':
                i += 1
                while i < len(self.commands) and self.commands[i][0] != '$':
                    row = self.commands[i].split(' ')
                    if row[0] == 'dir':
                        current_dir.dirs.append(Directory(row[1], current_dir))
                    else:
                        (size, name) = row
                        current_dir.files.append(File(name, int(size)))
                    i += 1


def get_sizes(root):
    if not root.dirs:
        s = root.size()
        return s if s <= 100000 else 0
    else:
        s = root.size()
        s = s if s <= 100000 else 0
        s += sum([get_sizes(d) for d in root.dirs])
        return s


def get_sizes_list(root):
    if not root.dirs:
        return root.size()
    else:
        temp = [root.size()]
        for d in root.dirs:
            t = get_sizes_list(d)
            if isinstance(t, list):
                temp.extend(t)
            else:
                temp.append(t)
        return temp


if __name__ == '__main__':
    sol = Solution()
    sol.explore()
    if getenv('part') == 'part1':
        print(get_sizes(sol.root))
    elif getenv('part') == 'part2':
        disk_space = 70000000 - sol.root.size()
        needed_space = 30000000 - disk_space
        valid = [e for e in get_sizes_list(sol.root) if e > needed_space]
        print(min(valid))






