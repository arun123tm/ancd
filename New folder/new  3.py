from pprint import pprint
from boto import ec2

AWS_ACCESS_KEY_ID = 'AKIAJMH7L7IHP3YIKAZQ'
AWS_SECRET_ACCESS_KEY = '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'

ec2conn = ec2.connection.EC2Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
reservations = ec2conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for i in instances:
    pprint(i.__dict__)
    break # remove this to list all instances