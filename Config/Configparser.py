"""
Parse config file and will return value based on key and Header you have provided.

e.g. If 'Phase1' is header and 'to_email' is  key ,
       config_parser.parser("Phase1","to_email") will give you value provided with 'to_email' key.
"""
import configparser

class config_parser():
   pass

#Returning value based on header and key provided.
def parser(header,key):

   configParser = configparser.ConfigParser()

   configParser.read('config.prop') #Read config file.

   return configParser.get(header,key) #Returning value.