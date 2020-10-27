numberOfScores = 0
score1 = 0
score2 = 0
total = 0
average = 0.0
scoreCount = 0

score = int(input("Please enter the score: "))
total = total + score
scoreCount = scoreCount + 1

if scoreCount != numberOfScores:
    average = total / numberOfScores
    print(average)
