# Globals
g_src = []
g_dest = []
g_temp = []


def Hanoi(num_disks, src: list[int], dest: list[int], temp: list[int]):
    if num_disks > 0:
        Hanoi(num_disks - 1, src, temp, dest)
        if len(src) > 0:
            biggest_disk = src.pop()
            dest.append(biggest_disk)

        print(f"src: {g_src}\tdest: {g_dest}\ttemp: {g_temp}")
        Hanoi(num_disks - 1, temp, dest, src)


if __name__ == "__main__":
    n_disks = 4
    g_src = list(range(1, n_disks + 1))
    Hanoi(n_disks, g_src, g_dest, g_temp)
