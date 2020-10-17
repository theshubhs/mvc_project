#Controller or Business logic

#importing dbcontext file 
from dbcontext import MySql

class account:
    
    #creating connection private variable  
    __connection = None

    #creating init object to initialize DB connect using private variable i.e. connection
    def __init__(self):
        self.__connection = MySql.Connect()
    
    
    def Save(self,users):
        if self.__isvalid(users):
            if self.__sendtoDatabase(users):
                users.setMessage(f"User {users.getUsername()} was registered succesfully ....")
        else:
            users.setMessage("Please Fill all the feilds")    
    
                             
    
    def __sendtoDatabase(self,users):
        try:
            cursor = self.__connection.cursor()
            query = f"INSERT into `users` VALUES (NULL, '{users.getFname()}', '{users.getLname()}', '{users.getUsername()}', '{users.getPassword()}', '{users.getEmail()}', '{users.getContact()}', CURRENT_DATE ,'{users.getAddress()}' )"
            cursor.execute(query)
            # print(query)
            commit = self.__connection.commit()
            cursor.close()
            return True
        except Exception as e:
            users.setMessage(e)
            return False
        
    
    def __isvalid(self,users):
        if users.getUsername() != "" and users.getPassword() != "" and users.getFname() != "" and users.getLname() != "" and users.getEmail() != "" and users.getContact() != "" and users.getAddress() != "" :
            return True
        else:
            return False 
    
    #*********************************************************
    
    def Login(self, users):
        if self.__isvalidLogin(users):
            if self.__isAuthentic(users):
                self.__Authorize(users)
            else:
                print("Incorrect username and password")
        else:
            print ("Please write username and password")
            
            
    
    ##Below are the private methods which is being called by Login method
    
    def __isvalidLogin(self, users): #this method is used to check parameters are not passed as null 
        if users.getUsername() !="" and users.getPassword() !="" :
            return True
        else:
            return False
    
    
    def __isAuthentic(self,users): #this method is used to authenticate user login by checking in DB
        cursor = self.__connection.cursor()
        cursor.execute("SELECT `userid` FROM `users` WHERE `username`='"+users.getUsername()+"' and `password`='"+users.getPassword()+"'")
        record = cursor.fetchone()
        if record != None:
            return True
        else:
            return False
        

    def __Authorize(self,users): #this method is used to called if user is available in DB 
        users.setMessage(users.getUsername()+" is Logged in ....")
        
    
    #******************************************************
    
    def Remove(self,users):
        if self.__isvalidUser(users):
            if self.__isAuthentic(users):
                if self.__deletefromDatabase(users):
                    users.setMessage(f"User {users.getUsername()} is deleted ....")
            else:
                users.setMessage(f"User crednetial doesn't exist ...")     
        else:
            users.setMessage(f"Enter valid username and password")
            
    
    def __isvalidUser(self, users): #this method is used to check parameters are not passed as null 
        if users.getUsername() !="" and users.getPassword() !="" :
            return True
        else:
            return False
        
        
    def __deletefromDatabase(self,users):
        try:
            cursor = self.__connection.cursor()
            query = f"DELETE from `users` where username = '{users.getUsername()}' and password = '{users.getPassword()}'"
            # print(query)
            cursor.execute(query)
            commit = self.__connection.commit()
            cursor.close()
            return True
        
        except Exception as e:
            users.setMessage(e)
            return False
        
        #*****************************************************************
        
    def Updatedetails(self,users):
        if self.__isvalidUser(users):
            if self.__isAuthentic(users):
                self.__changePassword(users)
                users.setMessage(f"Password changed for {users.getUsername()} ....")
                
            else:
                users.setMessage(f"User crednetial doesn't exist ...")
        
        else:
            users.setMessage(f"Enter valid username and password")
            
    
    def __changePassword(self,users):
        passDetail = users.setPassword(input("Create new password: "))
        try:
            cursor = self.__connection.cursor()
            query = f"UPDATE `users` SET `password` = '{users.getPassword()}' where `username` = '{users.getUsername()}'"
            cursor.execute(query)
            commit = self.__connection.commit()
            return True
        
        except Exception as e:
            users.setMessage(e)
            return False
        
        finally:
            cursor.close()
            
            
                

    
