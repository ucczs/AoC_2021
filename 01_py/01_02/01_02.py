with open('input.txt') as f:
    lines = f.readlines()

firstThree = True
count = 0

slidingAverageList = []
lastslidingAverage = 0
slidingAverage = 0

for idx, line in enumerate(lines):
    if idx < 3:
        slidingAverageList.append(int(line))
    else:
        lastslidingAverage = sum(slidingAverageList) / 3
        del slidingAverageList[0]
        slidingAverageList.append(int(line))
        slidingAverage = sum(slidingAverageList) / 3
        if lastslidingAverage < slidingAverage:
            count += 1

print(count)
