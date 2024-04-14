import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_polynomial(a, b, c, d, e):
    x = np.linspace(-10, 10, 400)
    y = a*x**4 + b*x**3 + c*x**2 + d*x + e
    return x,y

# Function to generate noisy data and plot with the polynomial
def generate_noisy_data(a, b, c, d, e, noise_level):
    x_original = np.linspace(-10, 10, 500)
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
    data = {'X': x, 'Y': y}
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def load_from_csv(filename):
    df = pd.read_csv(filename)
    return df
