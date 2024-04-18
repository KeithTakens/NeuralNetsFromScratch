import numpy as np
import matplotlib.pyplot as plt
import math


def generate_polynomial(a, b, c, d, e):
    x = np.linspace(-10, 10, 400)
    y = a*x**4 + b*x**3 + c*x**2 + d*x + e
    return x,y

# Function to generate noisy data and plot with the polynomial
def generate_noisy_data(a, b, c, d, e, noise_level, ammountOfPoints):
    x_original = np.linspace(-10, 10, ammountOfPoints)
    y_original = a*x_original**4 + b*x_original**3 + c*x_original**2 + d*x_original + e
    y_noisy = y_original + np.random.normal(0,noise_level,x_original.size)

    return x_original,y_noisy

def displayData(dataX,dataY,PlotLineX=0,PlotLineY=1):
    plt.figure(figsize=(8, 6))
    plt.scatter(dataX, dataY, color='red', s=10, label='Noisy Data Points')
    plt.title('Polynomial Curve with Noisy Data')
    plt.plot(PlotLineX,PlotLineY,label='Curve')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def save_to_csv(x,y, filename):

    csv_string = "X,Y\n"

    for xi, yi in zip(x, y):
        csv_string += f"{xi},{yi}\n"

    with open(filename, 'w') as file:
        file.write(csv_string)

def load_from_csv(filename):
    # Initialize empty lists to store the x and y values
    x = []
    y = []
    
    with open(filename, 'r') as file:
        # Skip the header
        next(file)
        
        # Read each subsequent line
        for line in file:
            values = line.strip().split(',')
            if len(values) == 2:  # Ensure there are exactly two columns
                x.append(float(values[0]))
                y.append(float(values[1]))

    return x, y



def checkLoss(a,b,c,d,e,dataX,dataY):
    L = []
    for valX,valY in zip(dataX,dataY):

        correctValue = a*valX**4 + b*valX**3 + c*valX**2 + d*valX + e
        Dist = abs(correctValue-valY)
        L.append(Dist)

    return(sum(L)/len(L))