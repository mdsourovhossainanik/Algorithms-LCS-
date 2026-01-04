 
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

 
# X = np.array([800, 1000, 1200, 1500, 1800]).reshape(-1, 1)  
# y = np.array([150, 200, 240, 310, 400])   
 
 
# model = LinearRegression()
# model.fit(X, y)
# Size=int(input("Enter size of new house that you want to predict how to price:")) 
# new_size = np.array([[Size]])
# predicted_price = model.predict(new_size)

# print(f"{Size} square_fit flat er price: {predicted_price[0]:.2f} hajar taka")
# """---------------------------------------------------------------------------------------"""
 
# plt.scatter(X, y, color='blue')
# plt.plot(X, model.predict(X), color='red')
# plt.scatter(new_size, predicted_price, color='green')
# plt.xlabel(' size of hoUSE')
# plt.ylabel('Price of house')
# plt.title(' pridict prie of house- Linear Regression')
# plt.show()

# #simple version
# # import numpy as np

# # # Data
# # x = np.array([800, 1000, 1200, 1500, 1800])
# # y = np.array([150, 200, 240, 310, 400])

# # n = len(x)

# # # Calculate sums
# # sum_x = np.sum(x)
# # sum_y = np.sum(y)
# # sum_xy = np.sum(x * y)
# # sum_x2 = np.sum(x * x)
# # # Calculate slope m
# # """m=n∑xy-(∑x)(∑y)/n∑x*x-(∑x)^2"""
# # m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)

# # # Calculate intercept c
# # c = (sum_y - m * sum_x) / n

# # # Predict
# # size = int(input("Enter house size (sq ft): "))
# # predicted_price = m * size + c

# # print(f"{size} sq ft house price: {predicted_price:.2f} hajar taka")
# # plt.scatter(X, y, color='blue')
# # plt.plot(X, model.predict(X), color='red')
# # plt.scatter(new_size, predicted_price, color='green')
# # plt.xlabel(' size of hoUSE')
# # plt.ylabel('Price of house')
# # plt.title(' pridict prie of house- Linear Regression')
# # plt.show()
import numpy as np
import matplotlib.pyplot as plt
 
x = np.array([800, 1000, 1200, 1500, 1800])
y = np.array([150, 200, 240, 310, 400])

n = len(x)

 
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x * x)

 
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
 
c = (sum_y - m * sum_x) / n

print("Slope (m):", m)
print("Intercept (c):", c)
 
predicted_y = m * x + c
 
plt.scatter(x, y, label='Data Points')
plt.plot(x, predicted_y, label='Best Fit Line', linewidth=2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression Line")
plt.legend()
plt.grid(True)
plt.show()
