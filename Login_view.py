#View or UI

#importing model class users
from model import users
#importing controller class accounts
from controller import account

#created object to access model class users
u = users()
#created object to access controller class accounts
acc = account()

print("--------------Welcome----------------")

u.setUsername(input("Enter the username: "))
u.setPassword(input("Enter the password: "))

#accessing login method from object acc of class account and passing attribute u which is object of class users    
acc.Login(u)

print(u.getMessage()) 