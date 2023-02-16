from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

x_init = np.array([1/4,1/4,1/4,1/4]) 



A = np.array([[0,0,1,1/2],[1/3,0,0,0],[1/3,1/2,0,1/2],[1/3,1/2,0,0]])


print(x_init)
print(A.T)
listOfFirstPage = []
listOfSecondPage = []
listOfThirdPage = []
listOfFourthPage = []

listOfEigenValue = []
ax = np.dot(A, x_init.T)
for i in range(50):
    eigenValue = max(ax)
    eigenVector = ax/max(ax)
    listOfEigenValue.append(eigenValue)
    ax = np.dot(A, eigenVector.T)
    

print(eigenValue)
print(eigenVector)
plt.plot([i for i in range(len(listOfEigenValue))], listOfEigenValue)
plt.grid()
plt.show()



def pageRank(cof, x, numberOfIter=3):
    for i in range(numberOfIter):
        x = np.dot(x, cof.T)
        listOfFirstPage.append(x[0])
        listOfSecondPage.append(x[1])
        listOfThirdPage.append(x[2])
        listOfFourthPage.append(x[3])
    return x

pageRank = pageRank(A,x_init, numberOfIter=30)
print(pageRank)


valueGeneral = [1,2,3,4]
valueWithout1 = [2,3,4]
valueWithout2 = [1,3,4]
valueWithout3 = [1,2,4]
valueWithout4 = [1,2,3]

numberOfHit1List = []
numberOfHit2List = []
numberOfHit3List = []
numberOfHit4List = []

nIter = 2000
def monte_carlo_method(value):
    numberOfHit1 = 0
    numberOfHit2 = 0
    numberOfHit3 = 0
    numberOfHit4 = 0
    randomValue = np.random.choice(value)
    if randomValue == 1:
            currentRandom = np.random.choice(valueWithout1, p=[1/3,1/3,1/3])
    elif randomValue == 2:
            currentRandom = np.random.choice(valueWithout2, p=[0,0.5,0.5])
    elif randomValue == 3:
            currentRandom = np.random.choice(valueWithout3, p=[1,0,0])
    elif randomValue == 4:
            currentRandom = np.random.choice(valueWithout4, p=[0.5,0,0.5])

    for i in range(nIter):
        if currentRandom == 1:
            currentRandom = np.random.choice(valueWithout1, p=[1/3,1/3,1/3])
            numberOfHit1 = numberOfHit1+1

        elif currentRandom == 2:
            currentRandom = np.random.choice(valueWithout2, p=[0,0.5,0.5])
            numberOfHit2 = numberOfHit2 + 1

        elif currentRandom == 3:
            currentRandom = np.random.choice(valueWithout3, p=[1,0,0])
            numberOfHit3 = numberOfHit3 + 1

        elif currentRandom == 4:
            currentRandom = np.random.choice(valueWithout4, p=[0.5,0,0.5])
            numberOfHit4 =numberOfHit4+ 1
        numberOfHit1List.append(numberOfHit1/(i+1))
        numberOfHit2List.append(numberOfHit1/(i+1))
        numberOfHit3List.append(numberOfHit1/(i+1))
        numberOfHit4List.append(numberOfHit1/(i+1))

    return [numberOfHit1/nIter, numberOfHit2/nIter, numberOfHit3/nIter, numberOfHit4/nIter]

print(monte_carlo_method(valueGeneral))
plt.plot([i for i in range(len(numberOfHit1List))], numberOfHit1List, label="1 page")
plt.plot([i for i in range(len(numberOfHit2List))], numberOfHit2List, label="2 page")
plt.plot([i for i in range(len(numberOfHit3List))], numberOfHit3List, label="3 page")
plt.plot([i for i in range(len(numberOfHit4List))], numberOfHit4List, label="4 page")
plt.grid()
plt.show() 
        
        

