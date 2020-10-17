#model class

class users:
    #initilized using init menthod
    def __init__(self):
        pass
    
    #private variable will only used by class/methods itself not outside the class/methods
    __username = ""
    __password = ""
    __fname    = ""
    __lname    = ""
    __email    = ""
    __contact  = ""
    __date     = ""
    __address  = ""
    __userid   = 0
    __message  = ""
    
    #Setter(mutators) method to set details under above mentioned variables
    def setUsername(self, param):
        self.__username = param
    def setPassword(self, param):
        self.__password = param
    def setFname(self, param):
        self.__fname = param
    def setLname(self, param):
        self.__lname = param
    def setEmail(self, param):
        self.__email = param
    def setContact(self, param):
        self.__contact = param
    def setDate(self, param):
        self.__date = param
    def setAddress(self, param):
        self.__address = param
    def setUserid(self, param):
        self.__userid = param
    def setMessage(self, param):
        self.__message = param
       
       
    #Getter(accessors) method to get details set under above mentioned varaibles
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getFname(self):
        return self.__fname
    def getLname(self):
        return self.__lname
    def getEmail(self):
        return self.__email
    def getContact(self):
        return self.__contact
    def getDate(self):
        return self.__date
    def getAddress(self):
        return self.__address
    def getUserid(self):
        return self.__userid
    def getMessage(self):
        return self.__message
    

    
    
    
    