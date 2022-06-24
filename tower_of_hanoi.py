# Globals
g_src = [4, 3, 2, 1]
g_dest = []
g_temp = []


def hanoi(num_disks, src: list[int], dest: list[int], temp: list[int]):
    if num_disks > 0:
        hanoi(num_disks-1, src, temp, dest)
        biggest_disk = src.pop()
        dest.append(biggest_disk)
        print(f'src: {g_src}\tdest: {g_dest}\ttemp: {g_temp}')
        hanoi(num_disks-1, temp, dest, src)


if __name__ == '__main__':
    hanoi(4, g_src, g_dest, g_temp)
