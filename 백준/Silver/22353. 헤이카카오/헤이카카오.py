a, d, k = map(int, input().split())

def expected_value(d):
    if d >= 100:
        return a
    tmp = d * 0.01 * a + (100-d) * 0.01 * (a + expected_value(d * (1 + k * 0.01)))
    return tmp

print("{:.10f}".format(expected_value(d)))