import time
import boto3
import botocore
def lambda_handler(event, context):
    rds = boto3.client('rds')
    rds.delete_db_instance(
        DBInstanceIdentifier='My-RDS-Aurora-Lambda-Instance',
        SkipFinalSnapshot=False)
    
