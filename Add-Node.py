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
