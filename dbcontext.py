#DBcontext : DB connection

#importing mysql connector library 
import mysql.connector as m

class MySql:
    #creating message variable for further use
    message = ""
    # creating DB connection method
    
    try:    
        @staticmethod  # it allows to call any method outside the class directly without creating any object  
        def Connect():
            #creating connection named object for DB connection string
            connection = m.connect(
                host = "localhost",  #localhost - host name provided by XAMPP
                user = "root",       #default username for myphpadmin provided by XAMPP 
                password = "",       #no password is set for myphpadmin provided by XAMPP
                database = "pythontestdb" #DB name created in myphpadmin provided by XAMPP
            )
            if connection.is_connected():
                MySql.message = "DB-Connected"
                return connection
    
    except Exception as e:
        MySql.message = e
    
    @staticmethod
    def Close(self, connection):
        connection.Close()
        
    
        
        
    

