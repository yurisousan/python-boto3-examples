import boto3
from botocore.exceptions import ClientError

ec2_client = boto3.client('ec2')
asg_client = boto3.client('autoscaling')

def delete_auto_scaling_group(asg_name):
    try:
        describe_asgs = asg_client.describe_auto_scaling_groups(
            AutoScalingGroupNames=[
                asg_name,
            ]
        )
        asg_list = describe_asgs['AutoScalingGroups']
        if len(asg_list) > 0:
            for asg in asg_list:
                if asg['AutoScalingGroupName'] == asg_name:
                    delete = asg_client.delete_auto_scaling_group(
                        AutoScalingGroupName=asg['AutoScalingGroupName'],
                        ForceDelete=True
                    )
                    print(f'Deleting the Auto Scaling Group {asg_name}: COMPLETED')
        else:
            print(f"The Auto Scaling Group {asg_name} no longer exists: COMPLETED")
    except Exception as e:
        if str(e).__contains__("not found"):
            print(f"The Auto Scaling Group {asg_name} no longer exists: COMPLETED")
delete_auto_scaling_group('awspy_autoscaling_group')

def delete_security_group(sg_name):
    try:
        describe_sgs = ec2_client.describe_security_groups(
            GroupNames=[
                sg_name,
            ]
        )
        sg_list = describe_sgs['SecurityGroups']
        for sg in sg_list:
            if sg['GroupName'] == sg_name:
                delete = ec2_client.delete_security_group(
                    GroupName=sg_name
                )
                print(f'Deleting the SecurityGroup {sg_name}: COMPLETED')
    except Exception as e:
        if str(e).__contains__("does not exist"):
            print(f"The Security Group {sg_name} no longer exists: COMPLETED")
delete_security_group('awspy_security_group')

def delete_launch_template(lt_name):
    try:
        describe_lts = ec2_client.describe_launch_templates(
            LaunchTemplateNames=[
                lt_name,
            ]
        )
        lt_list = describe_lts['LaunchTemplates']
        for lt in lt_list:
            if lt['LaunchTemplateName'] == lt_name:
                delete = ec2_client.delete_launch_template(
                    LaunchTemplateName=lt_name
                )
                print(f'Deleting the SecurityGroup {lt_name}: COMPLETED')
    except Exception as e:
        if str(e).__contains__("does not exist"):
            print(f"The Launch Template {lt_name} no longer exists: COMPLETED")
delete_launch_template('awspy_launch_template')