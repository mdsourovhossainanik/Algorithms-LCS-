 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

 
X = np.array([800, 1000, 1200, 1500, 1800]).reshape(-1, 1)  
y = np.array([150, 200, 240, 310, 400])   
 
 
model = LinearRegression()
model.fit(X, y)
Size=int(input("Enter size of new house that you want to predict how to price:")) 
new_size = np.array([[Size]])
predicted_price = model.predict(new_size)

print(f"{Size} square_fit flat er price: {predicted_price[0]:.2f} hajar taka")

 
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.scatter(new_size, predicted_price, color='green')
plt.xlabel(' size of hoUSE')
plt.ylabel('Price of house')
plt.title(' pridict prie of house- Linear Regression')
plt.show()