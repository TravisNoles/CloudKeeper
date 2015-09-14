from django.db import models
import yaml, json, requests
from os.path import expanduser


# Load actions from digitalocean api.

# Create your models here.
class Droplet(models.Model):
    
    #User provided values:
    hostname = models.CharField(max_length=50)
    region = models.CharField(max_length=4)
    size = models.CharField(max_length=4)
    image = models.CharField(max_length=20)
    sshkeys = models.CommaSeparatedIntegerField()
    backups = models.BooleanField()
    ipv6 = models.BooleanField()
    privateNetwork = models.BooleanField()
    UserData = models.TextField()

    
    #Files to upload to homedirectory?


    #Unchangable api provided values.
    ipAddress = models.GenericIPAddressField()
    createdAt = models.DateField()


    def getAuth(option):
        headers=""
        apidata = []

        # Open add read config.
        configFile = open(__SETTINGSFILE)

        # Read settings file for api key.
        settingsFileData = yaml.safe_load(configFile)

        apikey = 'Bearer ' + settingsFileData['DigitalOcean']['apikey']
        




        #Access apikey



        # Return Data
        return apidata['option']

    #Create a new droplet.  
    def createDroplet(cls, hostname, region, size, image, sshkeys, backups, ipv6, privateNetwork, UserData):
        newdroplet = cls(hostname, region, size, image, sshkeys, backups, ipv6, privateNetwork, UserData)






        return newdroplet



# Create a new droplet: droplet = Droplet.Create("example.org")