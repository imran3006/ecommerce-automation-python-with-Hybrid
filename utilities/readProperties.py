import configparser

config= configparser.RawConfigParser()        #/rawconfigparser is a method under configparser package. we create object of this method
config.read(".\\Configurations\\config.ini")  # read the config.ini file in where common files are written
# utility file to read the data from ini file
class ReadConfig:
    @staticmethod
    def getApplicationURL(self):
        url= config.get('common info','baseUrl')
        return url


    def getUserEmail(self):
        username= config.get('common info','useremail')
        return username


    def getPassword(self):
        password= config.get('common info','password')
        return password