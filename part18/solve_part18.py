def in_scope(cube, scope_xyz_min, scope_xyz_max):
    return all(cube[i] >= scope_xyz_min[i] and cube[i] <= scope_xyz_max[i] for i in range(3))

def get_neighbours(cube):
    dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    return [tuple(sum(tup) for tup in zip(cube, d)) for d in dirs]

def main():
    filename = 'input.txt'

    coords = set()

    with open(filename, 'r') as f:
        for line in f:
            line_tuple = tuple(eval(line.strip()))
            coords.add(line_tuple)

    scope_xyz_min = [min(c[i]-1 for c in coords) for i in range(3)]
    scope_xyz_max = [max(c[i]+1 for c in coords) for i in range(3)]

    # Part I
    exposed_sides = 0
    for c in list(coords):
        next_2_cnt = 0
        if (c[0], c[1], c[2]-1) in coords:
            next_2_cnt += 1
        if (c[0], c[1], c[2]+1) in coords:
            next_2_cnt += 1
        if (c[0], c[1]-1, c[2]) in coords:
            next_2_cnt += 1
        if (c[0], c[1]+1, c[2]) in coords:
            next_2_cnt += 1
        if (c[0]-1, c[1], c[2]) in coords:
            next_2_cnt += 1
        if (c[0]+1, c[1], c[2]) in coords:
            next_2_cnt += 1
        exposed_sides += (6-next_2_cnt)
    print('Answer part I:', exposed_sides)

    # Part II - bfs
    exposed_outer_sides = 0
    seen_cubes = set()
    queue = [tuple(scope_xyz_max)]

    while queue:
        curr_cube = queue.pop(0)
        if curr_cube in coords:
            exposed_outer_sides += 1
            continue
        if curr_cube not in seen_cubes:
            seen_cubes.add(curr_cube)
            for nbr in get_neighbours(curr_cube):
                if in_scope(nbr, scope_xyz_min, scope_xyz_max):
                    queue.append(nbr)

    print('Answer part II:', exposed_outer_sides)


if __name__ == '__main__':
    main()