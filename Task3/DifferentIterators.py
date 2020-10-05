def FloatIterator(start, difference, numberIterations):
    n = 0
    while n != numberIterations:
        print(start)
        start += difference
        n += 1


def TimeIterator(start, step, numberIterations):
    n = 0
    while n != numberIterations:
        print(':'.join([str(x) for x in start]))
        sec = (start[2] + step[2])
        minute = (start[1] + step[1]) + (sec // 60)
        h = start[0] + step[0] + (minute // 60)
        start[2] = (sec) % 60
        start[1] = (minute) % 60
        start[0] = (h) % 24
        n += 1


FloatIterator(1.23, 345.34, 6)
TimeIterator([int(x) for x in '12:00:00'.split(':')], [int(x) for x in '00:15:45'.split(':')], 10)
