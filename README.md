RDS Aurora - Schedule Add / Delete Reader Node with Lambda Function and CloudWatch Event


---Add Reader Node

First step, I create Lambda Function "Add-Node.py"

![GitHub Logo](https://github.com/mryutran/RDS-Aurora-Schedule-Add-Delete-Reader-Node/blob/main/Add-Node.png)

Second step, I add trigger with CloudWatch Event - Schedule expression: cron(17 7 * * ? *) 

This schedule will run lambda function at 7:17:00 GMT , to VNT (GMT+7) at 14:17:00


---Delete Reader Node

First step, I create Lambda Function "Delete-Node.py"

![GitHub Logo](https://github.com/mryutran/RDS-Aurora-Schedule-Add-Delete-Reader-Node/blob/main/Delete-Node.png)
    

Second step, I add trigger with CloudWatch Event - Schedule expression: cron(27 7 * * ? *) 

This schedule will run lambda function at 7:27:00 GMT , to VNT (GMT+7) at 14:27:00
