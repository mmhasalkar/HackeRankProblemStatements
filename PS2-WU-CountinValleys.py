# Complete the countingValleys function below.
def countingValleys(n, s):
    tracker = 0
    steps = list(s)
    valley_started = False
    valleys = 0

    for step in steps:
        if step == "U":
            tracker += 1
        else:
            tracker -= 1

        if tracker < 0:
            valley_started = True

        if tracker == 0 and valley_started:
            valleys += 1
            valley_started = False

    if tracker < 0:
        valleys += 1

    return valleys


if __name__ == '__main__':
    result = countingValleys(8, "UDDDUDUDUUUD")
    print(result)