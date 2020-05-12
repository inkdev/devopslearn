import boto3
import sys


def changestat(region_name, current_status, new_status):
    ec2 = boto3.resource('ec2', region_name)
    instance_list = ec2.instances.all()
    for instance in instance_list:
        ec2state = instance.state
        for current_status in ec2state:
            if current_status == 'terminated':
                print("You can't change terminated status")
                sys.exit()
            elif current_status == 'stopped' and new_status not in ['running', 'terminated']:
                print("You need to start or terminate this instance")
                sys.exit()
            if new_status == 'stopped':
                ec2.Instance(instance.id).stop()
            elif new_status == 'terminated':
                ec2.Instance(instance.id).terminate()
            elif new_status == 'reboot':
                ec2.Instance(instance.id).reboot()
            elif new_status == 'running':
                ec2.Instance(instance.id).start()

