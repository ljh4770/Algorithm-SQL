def ccw(x1, y1, x2, y2, x3, y3):
    """
    Outer product of 3 points (x1, y1), (x2, y2), (x3, y3).
    A: (x1, y1)
    B: (x2, y2)
    C: (x3, y3)
    AB vector: (x2 - x1, y2 - y1)
    AC vector: (x3 - x1, y3 - y1)
    Returns a positive value if the points are in counter-clockwise order,
    a negative value if they are in clockwise order, and zero if they are collinear.
    If the points are collinear, the value is zero.
    """
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split(' '))
    x3, y3, x4, y4 = map(int, input().split(' '))

    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

    if ccw123 * ccw124 < 0 and ccw341 * ccw342 < 0:
        # In parallel lines, check if the segments overlap
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            print(1)
        else:
            print(0)
    else:
        if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
            # If the segments are collinear, check if they overlap
            if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
                print(1)
            else:
                print(0)
        else:
            print(0)