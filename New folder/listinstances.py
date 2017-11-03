# Name : laststopped.py
# Description : Lists EC2 isntances
# Date of Creation : March-2016
# Language Used : Python [boto,pymssql]

import boto.ec2
import datetime
import csv
import configparser
#import MySQLdb

try:
	file = {}
	config = configparser.ConfigParser()
	config.read('C:\Users\bharbs\Desktop\New folder\property.conf')
	credentialFile = config.get("InputFile",'credentialFile')
	regionFile = config.get("InputFile",'regionFile')					
except IOError:
	print "Input file does not exists"
	

try:
	with open(credentialFile,'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			customer = row['customer']
			aws_access_key_id = row['aws_access_key_id']
			aws_secret_access_key = row['aws_secret_access_key']
			with open(regionFile,'r') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					region_name = row['region']
					conn = boto.ec2.connect_to_region(region_name,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
					#conndb = MySQLdb.connect("awsreports","root","cloud@123")
					#print conndb
					#cur = conndb.cursor()
					reservations = conn.get_all_instances()
					#try:
					for r in reservations:
						for i in r.instances:
							instid = i.id.strip('u')
							state = i.state.strip('u')
							publicip = i.ip_address
							privateip = i.private_ip_address
							reason = i.reason.strip('u')
							vpc = i.vpc_id
							type = i.instance_type
							region = i.placement
							print instid,state,publicip,privateip,reason,vpc,type,region
							#cur.execute("INSERT INTO reports.instance VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (instid,state,type,region,privateip,publicip,vpc,reason,str(datetime.datetime.now()),customer))
							#conndb.commit()
					#conn.close()
					#except MySQLdb.Error as e:
						#print "Caught an expcetion", e
except IOError:
	print "Error in Connection "

				
		
