def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def point_within_sensor_range(point, sensors):
    for sx, sy, d in sensors:
        if manhattan_distance(point, (sx, sy)) <= d:
            return True
    return False

def point_in_range(point):
    return point[0] >= 0 and point[1] >= 0 and point[0] < 4000000 and point[1] < 4000000

def find_outside_points(sensors):
    outside_points = set()

    for sx,sy,d in sensors:
        # West
        for idx,x in enumerate(range(sx-d-1, sx)):
            # Northwest
            pnw = (x, sy+idx)
            if point_in_range(pnw):
                if pnw in outside_points :
                    #outside_points.remove(pnw)
                    pass
                else:
                    outside_points.add(pnw)
            # Southwest
            psw = (x, sy-idx)
            if point_in_range(psw):
                if psw in outside_points:
                    #outside_points.remove(psw)
                    pass
                else:
                    outside_points.add(psw)
        # East
        for idx,x in enumerate(range(sx, sx+d+1+1)):
            # Northeast
            pne = (x, sy + (d+1) - idx)
            if point_in_range(pne):
                if pne in outside_points:
                    #outside_points.remove(pne)
                    pass
                else:
                    outside_points.add(pne)
            # Southeast
            pse = (x, sy -(d+1) + idx)
            if point_in_range(pse):
                if pse in outside_points:
                    #outside_points.remove(pse)
                    pass
                else:
                    outside_points.add(pse)
    return outside_points

def find_tuning_frequency(point):
    return point[1] * 4000000 + point[0]

def main():
    filename = 'input.txt'
    with open(filename, 'r') as f:
        input = f.readlines()

    sensors, beacons = list(), list()
    for line in input:
        splt_line = line.strip().split()
        sx = eval(splt_line[2][2:].replace(',', '').replace(':', ''))
        sy = eval(splt_line[3][2:].replace(',', '').replace(':', ''))
        bx = eval(splt_line[8][2:].replace(',', '').replace(':', ''))
        by = eval(splt_line[9][2:].replace(',', '').replace(':', ''))
        dist = manhattan_distance((sy,sx), (by,bx))
        # notice swap of x/y to get axes conventional
        sensors.append((sy,sx,dist))
        beacons.append((by, bx))

    # Part I
    x = 2000000
    min_y = min([y-d for _,y,d in sensors])
    max_y = max([y+d for _,y,d in sensors])
    # iterate through row
    cnt = 0
    for y in range(min_y, max_y):
        if point_within_sensor_range((x,y), sensors) and (x,y) not in beacons:
            cnt += 1
    print('Answer part I:', cnt) # 5240818

    # Part II
    search_space = find_outside_points(sensors)
    range = 4000000

    for p in search_space:
        if p[0] >= 0 and p[0] <= range and p[1] >= 0 and p[1] <= range:
            if not point_within_sensor_range(p, sensors): #and p not in beacons:
                print('Answer part II:', find_tuning_frequency(p)) # 13213086906101
                print('p:', p)
                break

if __name__ == '__main__':
    main()