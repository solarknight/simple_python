def rank(score):
    if score < 60:
        return 'E'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'

print(rank(66))
print(rank(82))
