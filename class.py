class Person():
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerSon(self):
        print("Name: ", self.firstName + ",", self.lastName)
        print("IdNumber : ", self.idNumber)
class Student(Person):
    def __init__(self, firstName, lastName , idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        sm=0
        for x in range(0, len(scores)):
            sm= sm + scores[x]
        avg=sm/len(scores)
        if (avg < 40):
            return "T"
        elif (avg < 55):
            return "D"
        elif (avg < 70):
            return "P"
        elif (avg < 80 ):
            return "A"
        elif (avg < 90):
            return "E"
        else:
            return "O"
line = input().split()
firstName= line[0]
lastName= line[1]
idNumber= line[2]
numScores= list(input())
scores= list(map(int , input().split()))
s= Student(firstName, lastName, idNumber, scores)
s.printPerSon()
print("Grade: ", s.calculate())
