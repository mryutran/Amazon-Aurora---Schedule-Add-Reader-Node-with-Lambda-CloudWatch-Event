RDS Aurora - Schedule Add / Delete Reader Node with Lambda Function and CloudWatch Event


---Add Reader Node

First step, I create Lambda Function "Add-Node.py"

import time
import boto3
import botocore

def lambda_handler(event, context):
    rds = boto3.client('rds')

    rds.create_db_instance(
        DBParameterGroupName='default.aurora-mysql5.7',
        Engine='aurora-mysql',
        EngineVersion='5.7.mysql_aurora.2.10.0',
        DBClusterIdentifier='My-RDS-Aurora-Cluster',
        AvailabilityZone='ap-east-1a',
        DBInstanceClass='db.t3.small',
        DBInstanceIdentifier='My-RDS-Aurora-Lambda-Instance',
        PubliclyAccessible=True,
        StorageEncrypted=True,
        PromotionTier=15)

Second step, I add trigger with CloudWatch Event - Schedule expression: cron(17 7 * * ? *) 

This schedule will run lambda function at 7:17:00 GMT , to VNT (GMT+7) at 14:17:00


---Delete Reader Node

First step, I create Lambda Function "Delete-Node.py"

import time
import boto3
import botocore
def lambda_handler(event, context):
    rds = boto3.client('rds')
    rds.delete_db_instance(
        DBInstanceIdentifier='My-RDS-Aurora-Lambda-Instance',
        SkipFinalSnapshot=False)
    

Second step, I add trigger with CloudWatch Event - Schedule expression: cron(27 7 * * ? *) 

This schedule will run lambda function at 7:27:00 GMT , to VNT (GMT+7) at 14:27:00
