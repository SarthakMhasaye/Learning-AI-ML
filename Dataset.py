from sklearn.linear_model import LinearRegression
import pickle

houses = [[1000,1],[2000,2],[3400,3],[4500,4]]
price = [1000000,2000000,300000,5400000]

model = LinearRegression()
model.fit(houses,price)

with open("Houcepricemodel.pkl","wb") as file:
    pickle.dump(model,file)