outcomes = {
    "A": {
        "X": 3,
        "Y": 4,
        "Z": 8
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 2,
        "Y": 6,
        "Z": 7
    }
}

points = 0
for line in open('input.txt', 'r').readlines():
    points += outcomes[line[0]][line[2]]
    
print(points)
