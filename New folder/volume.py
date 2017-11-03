#!/usr/bin/env python2
import boto.ec2

REGION = 'us-east-2'
conn = boto.ec2.connect_to_region(REGION,aws_access_key_id="AKIAJMH7L7IHP3YIKAZQ",aws_secret_access_key="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")

def main():
    volumes = conn.get_all_volumes()

    for volume in volumes:
        print volume

        # Match to an instance id
        print volume.attach_data.instance_id

        # # Object attributes:
        # print volume.__dict__

        # # Object methods:
        # print(dir(volume))

if __name__ == '__main__':
    main()