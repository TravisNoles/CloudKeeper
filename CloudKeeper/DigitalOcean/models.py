from django.db import models
import yaml, json, requests
from os.path import expanduser


#Action Manager Model
class Actions(models.Model):
    self.id = models.IntegerField()
    self.token = None
    self.status = None
    self.type = None
    self.started_at = None
    self.completed_at = None
    self.resource_id = None
    self.resource_type = None
    self.region = None
    self.region_slug = None

    def getExisting(id):
        return action

    def getAll():
        return actions

    def do(actiontype):
        return status_code

#Domain manager model
class Domains(models.Model):
    def getAll():
        return domains_list

#Region manager model
class Regions(models.Model):
    def listAll():
        return region_list

#Image manager model
class Images(models.Model):


    def listAll():

        return Images;


    #
    def create():


        return status_code

#Droplet manager model
class Droplet(models.Model):
    # Droplet Manager - Sets and returns data on all droplets.
    self.id = models.IntegerField() #Auto-gen
    self.name = models.CharField(max_length=50) #User
    self.memory = models.CharField(max_length=10)
    self.kernel = models.CharField()
    self.vcpus = models.CharField(max_length=5)
    self.disk = models.CharField(max_length=10)
    self.status = models.CharField()
    self.ip_address = models.IPAddressField()
    self.region = models.CharField(max_length=4)
    self.size_slug = models.CharField(max_length=10)
    self.image = models.CharField(max_length=20)
    self.sshkeys = models.CommaSeparatedIntegerField()
    self.backups = models.BooleanField()
    self.ipv6 = models.BooleanField()
    self.private_network = models.BooleanField()
    self.user_data = models.TextField()
    self.created_at = models.DateTimeField()

    #Gets default values (for debug)
    def getDropletDefaults(hostname):
        """Return default values for digitial ocean"""
        dropletDefaults['name'] = hostname
        dropletDefaults['region'] = 'nyc3'
        dropletDefaults['size'] = '512mb'
        dropletDefaults['image'] = 'ubuntu-14-04-x64'
        dropletDefaults['sshkeys'] = []
        dropletDefaults['backups'] = False
        dropletDefaults['ipv6'] = False
        dropletDefaults['private_network'] = False
        dropletDefaults['user_data'] = ''
        return dropletDefaults

    def _getAuth():
        headers=""
        apidata = []
        apiurl = "https://api.digitalocean.com/v2/droplets"

        # Open add read config.
        configFile = open(__SETTINGSFILE)

        # Read settings file for api key.
        settingsFileData = yaml.safe_load(configFile)

        # Set API key.
        apikey = 'Bearer ' + settingsFileData['DigitalOcean']['apikey']
       
        # Return Data
        return apidata

    #Get data, along with requesting root json info
    def _getData(suburl, req):
        
        # Get auth headers and store it in headers var.       
        headers = getAuth(suburl)

        # Get data from digitalocean using full API url, and custom authentication headers.
        r = requests.get(apiurl, headers=headers)

        #load data from api and return
        data = json.loads(r.text)
        return data[req]

    def getDroplet(id):
        """Get droplet by ID."""
        
        droplet = []
            


        return droplet

    def power_on():
        return results;
    
    def getActiveDroplets():
        return results

    #Create a new droplet.  
    def createDroplet(cls, name, region, size, image, ssh_keys, backups, ipv6, privateNetwork, user_data):
        newdroplet = cls(hostname, region, size, image, sshkeys, backups, ipv6, private_net, user_data)
        newdroplet = {'name': name, "region": region, "size": size, "image": image, "ssh_keys": ssh_keys, "backups": backups, "ipv6": ipv6, "user_data": user_data, "private_networking": private_net}

        apiurl = __BASEURL
        headers = _getAuth()

        r = requests.post(apiurl, json=newdroplet, headers=headers) 


        return newdroplet


    def removeDroplet():
        return;

#DigitalOcean Account Info
class Account(models.Model):
    def getDropletLimit():
        return droplet_limit

    def getEmail():
        return email




# Create a new droplet: droplet = Droplet.Create("example.org")