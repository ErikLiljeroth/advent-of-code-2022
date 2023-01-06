import copy

def snafu_2_dec(snafu_str):
    conv_dict = {'2':2, '1':1, '0':0, '-':-1, '=':-2}
    chars = [(c,len(snafu_str) - i - 1) for i,c in enumerate(snafu_str)]
    output = 0
    for char in chars:
        output += conv_dict[char[0]] * (5**(char[1]))
    return output

def dec_2_snafu(dec_nbr):
    action_dict = {0:'0', 1:'1', 2:'2', 3:'=', 4:'-'}
    snafu_str = []
    cnt = 0
    nbr = copy.copy(dec_nbr)
    while nbr != 0:
        rest = nbr % 5
        nbr = nbr - rest
        if rest in [3, 4]:
            nbr = nbr + (5**(cnt+1))
        snafu_str.insert(0, action_dict[rest])
        nbr = int(nbr/5)
    return snafu_str

def main():
    filename = 'input.txt'
    with open(filename, 'r') as f:
        input = f.readlines()
    # Part I
    sum = 0
    for line in input:
        sum += snafu_2_dec(line.strip())
    result = ''.join(dec_2_snafu(sum))
    print('Answer Part i:', result)

if __name__ == '__main__':
    main()