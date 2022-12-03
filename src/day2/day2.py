outcomes = {
    "A": {
        "X": 4,
        "Y": 8,
        "Z": 3
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 7,
        "Y": 2,
        "Z": 6
    }
}

points = 0
for line in open('input.txt', 'r').readlines():
    points += outcomes[line[0]][line[2]]
    
print(points)
