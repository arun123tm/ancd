# Name : laststopped.py
# Description : Lists EC2 isntances
# Date of Creation : March-2016
# Language Used : Python [boto,pymssql]

import boto.ec2
import datetime
#import csv
#import configparser
#import MySQLdb

region_name="US East (Ohio)"
aws_access_key_id="AKIAJMH7L7IHP3YIKAZQ"
aws_secret_access_key="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"

	
try:
	conn = boto.ec2.connect_to_region(region_name,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
	reservations = conn.get_all_reservations()
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
except IOError:
	print "Error Connecting Database"

				
		