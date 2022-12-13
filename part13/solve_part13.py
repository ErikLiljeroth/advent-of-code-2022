from functools import cmp_to_key

def compare_int(left:int, right:int) -> int:
    if left < right:
        return 1
    elif left > right:
        return -1
    else:
        return 0

def compare(left, right) -> int:
    if isinstance(left, int):
        if isinstance(right, int):
            return compare_int(left, right)
        else:
            return compare([left], right)#comma after?
    if isinstance(right, int):
        return compare(left, [right])
    for idx in range(min(len(left), len(right))):
        result = compare(left[idx], right[idx])
        if result in [-1,1]:
            return result
    if len(left) < len(right):
        return 1
    if len(right) < len(left):
        return -1
    return 0

def main():
    filename = 'input.txt'
    with open(filename, 'r') as f:
        input = f.readlines()

    packets = []
    packet = []
    for idx,line in enumerate(input):
        if idx == len(input)-1:
            packet.append(eval(line.strip()))
            packets.append(packet)
        elif line != '\n':
            packet.append(eval(line.strip()))
        else:
            packets.append(packet)
            packet = []
    # Part I
    sum = 0
    for idx,pack in enumerate(packets):
        if compare(pack[0], pack[1]) == 1:
            sum += idx + 1
        else:
            pass
    print('Answer part I:', sum)
    # Part II
    packets_not_grouped = [l for packet in packets for l in packet]
    packets_not_grouped.extend([[[2]], [[6]]])
    packets_sorted = sorted(packets_not_grouped, key=cmp_to_key(compare), reverse=True)
    relevant_idx = []
    for idx,pack in enumerate(packets_sorted):
        if ascii(pack) == '[[2]]':
            relevant_idx.append(idx + 1)
        elif ascii(pack) == '[[6]]':
            relevant_idx.append(idx + 1)
        else:
            pass

    print('Answer part II:', relevant_idx[0]*relevant_idx[1])

if __name__ == '__main__':
    main()