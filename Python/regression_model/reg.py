import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

def meansqerror(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        total_error += (y-(m*x+b))**2
    error = total_error/ float(len(points))
    return error

def graddescent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    n = len (points)

    for i in range(n):
        x = points.iloc[i].studytime
        y = points.iloc[i].score

        m_gradient += (-2/n)*x*(y-m_now*x-b_now)
        b_gradient += (-2/n)*(y-m_now*x-b_now)

    m = m_now - m_gradient*L
    b = b_now - b_gradient*L
    return m,b

m=0
b=0
L=0.001
epos = 300
for i in range(epos):
    m,b = graddescent(m,b,data,L)
print("Coefficient : ",m)
print("Intercept : ",b)
print("Mean Squared Error : ",meansqerror(m, b, data))

plt.scatter(data.studytime, data.score, color='red')
plt.plot(data.studytime, m*data.studytime+b,color= 'black')
plt.show()