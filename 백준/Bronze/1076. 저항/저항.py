a = input()
b = input()
c = input()

resistor = {
    "black": ('0', 1),
    "brown": ('1', 10),
    "red": ('2', 100),
    "orange": ('3', 1_000),
    "yellow": ('4', 10_000),
    "green": ('5', 100_000),
    "blue": ('6', 1_000_000),
    "violet": ('7', 10_000_000),
    "grey": ('8', 100_000_000),
    "white": ('9', 1_000_000_000)
}
res = int(resistor[a][0] + resistor[b][0]) * resistor[c][1]
print(res)