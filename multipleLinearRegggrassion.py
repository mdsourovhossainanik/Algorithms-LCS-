 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

 
X = np.array([
    [800, 2, 10],
    [1000, 3, 5],
    [1200, 3, 15],
    [1500, 4, 7],
    [1800, 4, 2]
])  
y = np.array([150, 200, 240, 310, 400])   
 
 
model = LinearRegression()
model.fit(X, y)

size_input = int(input("Enter size of new house (sq ft): "))
bedrooms_input = int(input("Enter number of bedrooms: "))
age_input = int(input("Enter age of house (years): "))
new_house = np.array([[size_input, bedrooms_input, age_input]])
predicted_price = model.predict(new_house)[0]

print(f"Estimated price: {predicted_price:.2f} hajar taka")


"""------------------------------------------------------------------------------------"""

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[:,0], X[:,1], y, color='blue', s=50, label='Existing Houses')
# plt.plot(X, model.predict(X), color='red')
ax.scatter(size_input, bedrooms_input, predicted_price, color='green', s=100, label='Predicted House')
ax.set_xlabel('House Size (sq ft)')
ax.set_ylabel('Bedrooms')
ax.set_zlabel('Price (hajar taka)')
ax.set_title('Multiple Linear Regression - House Price Prediction')
ax.legend()
plt.show()