import re

def new_path(current_dir, cd_arg):
    #print("============")
    #print("new path:")
    #print("current_dir: " + str(current_dir))
    #print("cd arg: " + cd_arg)
    if cd_arg == '/':
        #print("new: []")
        return []
    elif cd_arg == '..':
        #print("new: " + str([x for x in current_dir[:-2]]))
        return [x for x in current_dir[:-1]]
    else:
        #print("new: " + str(([x for x in current_dir] + [cd_arg])))
        return [x for x in current_dir] + [cd_arg]

def path_to_str(path):
    return '/' + '/'.join(path)

def subdir_path(current_dir, subdir_name):
    return path_to_str(new_path(current_dir, subdir_name))

def dir_size(filesystem, current_dir):
    if current_dir not in filesystem:
        return 0
    total_size = filesystem[current_dir]["files"]
    for subdir in filesystem[current_dir]["dirs"]:
        total_size += dir_size(filesystem, subdir)

    return total_size

with open('input.txt', 'r') as infile:
    lines = [line.strip().split('\n') for line in infile.read().split('$') if line.strip()]

#print(lines)

filesystem = {}
current_path = []

for cmd in lines:
    if cmd[0] == "ls":
        files = [int(file.split(' ')[0]) for file in cmd[1:] if not file.startswith('dir')]
        dirs = [subdir_path(current_path, file.split(' ')[1]) for file in cmd[1:] if file.startswith('dir')]
        # print("current_dir: " + path_to_str(current_path))
        # print("current_dir's files: " + str(files))
        # print("current_dir's subdirectories: " + str(dirs))
        path_str = path_to_str(current_path)
        if path_str not in filesystem:
            filesystem[path_str] = {}
        filesystem[path_str]["files"] = sum(files)
        filesystem[path_str]["dirs"] = dirs
    else:
        # it is a cd command
        new_dir = cmd[0].split(' ')[1]
        current_path = new_path(current_path, new_dir)

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000
current_free_space = TOTAL_SPACE - dir_size(filesystem, '/')
smallest_dir = ''
smallest_size = TOTAL_SPACE
for dir in filesystem:
    dsize = dir_size(filesystem, dir)
    if current_free_space + dsize > REQUIRED_SPACE and dsize < smallest_size:
        smallest_dir = dir
        smallest_size = dsize

print(smallest_dir)        
print(smallest_size)        
