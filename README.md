# AWS_Lambda_ShutDown_EC2_Instance
Creating a Basic Lambda Function to Shut Down an EC2 Instances in all regions

In this section we will create a basic Lambda function to shut down/Stop an EC2 instances. 
We will start step by step with creating below AWS Services.

a. Custom IAM policy for the IAM role. 
b. Basic Lambda function.
c. Smaple EC2 instances.

Solution
Log in to the AWS Management Console **https://aws.amazon.com.**

a. Create a Custom IAM Policy and Role for a Lambda Function
   From the AWS Management Console, navigate to IAM.
   On the left menu, select Roles.
   Click Create role.
   With AWS service selected, click Lambda.
   Click Next: Permissions.
   Click Create policy.
   Select the JSON tab.
   Delete the existing code and paste in the following:
   
   https://github.com/Sharathkumar-dp/AWs_Lambda_ShutDown_EC2_Instance/blob/master/IAM_Policy.json

   Click Next: Tags.
   Click Next: Review
   In Name, enter "**ec2lambdapolicy**" and click Create policy.
   On the left menu, select Roles > Create role.
   Select Lambda again and click Next: Permissions.
   Select the newly created ec2lambdapolicy and click Next: Tags > Next: Review.
   In Role name, enter "**ec2role**" and click Create role.

b. Create a Basic Lambda Function
   From the AWS Management Console, navigate to Lambda.
   With Author from scratch selected, set the following values:
   Function name: lambdaEC2stop
   Runtime: Python 3.8 
   Click Change default execution role to expand options.
   Under Execution role, select Use an existing role.
   Under Existing role, select ec2role.
   Click Create function.
   Scroll down to Code source and double-click lambda_function.py.
   Delete the existing code and paste in the following :
   
   https://github.com/Sharathkumar-dp/AWs_Lambda_ShutDown_EC2_Instance/blob/master/EC2_Stop_Lambda.py
   
   Click Deploy.

c. Smaple EC2 instances
   From the AWS Management Console, navigate to EC2.
   On the right top side, select Launch instance.
   Select AMI > select instance-type > instances = 3
   Selct Review and launch and launch the instances

d. Create a Test event in the Lambda Console
   In the AWS Lambda console, select the function and click Test.
   In Configure test event, create an event name and click Create.
   Click Test and view the execution result.
   Return to the EC2 console.
   On the left menu, click Instances.
   Under Details, the Instance state should now be shown as Stopped. 
   
   
   **Congratualations**
