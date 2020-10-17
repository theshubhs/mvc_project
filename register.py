#View or UI

#importing model class users
from model import users
#importing controller class accounts
from controller import account

#created object to access model class users
u = users()
#created object to access controller class accounts
acc = account()

print("--------------User Registration----------------")

u.setUsername(input("Please choose the username: "))
u.setPassword(input("Please create the new password: "))
u.setFname(input("Please enter the First Name: "))
u.setLname(input("Please enter the Last Name: "))
u.setEmail(input("Please enter the Email ID: "))
u.setContact(input("Please enter the Contact number: "))
u.setAddress(input("Please enter the Address: "))

#accessing login method from object acc of class account and passing attribute u which is object of class users    


acc.Save(u)
print(u.getMessage())

