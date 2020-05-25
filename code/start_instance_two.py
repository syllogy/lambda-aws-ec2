import boto3

region = "us-east-1"
instances = ["INSTANCES-ID"]

ec2 = boto3.client("ec2", region_name=region)

# ==============================================================================
# LAMBDA HANDLER FUNCTION
# ==============================================================================

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print(f"Started your instances: {instances}")
    