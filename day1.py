from collections import Counter

if __name__ == "__main__":
    left, right = [], []
    dist, similar = 0, 0

    with open("input", "r") as f:
        for line in f:
            num = line.split()
            left.append(int(num[0]))
            right.append(int(num[1]))

    left.sort()
    right.sort()

    right_count = Counter(right)

    for l, r in zip(left, right):
        dist += abs(l - r)
        similar += l * right_count[l]

    print(dist)
    print(similar)
