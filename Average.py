numberOfScores = 0
score1 = 0
score2 = 0
total = 0
average = 0.0
scoreCount = 0
#numberOfScores = int(input("Please enter the number of scores that you want to average: "))

#What python loop structure could we use to repeat the next 3 lines
score = int(input("Please enter the score: "))
total = total + score
scoreCount = scoreCount + 1

if scoreCount != numberOfScores:
    average = total / numberOfScores
    print(average)
