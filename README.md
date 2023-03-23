Abstract:
Api Crud operation deployed to aws ec2
Step 1:
Have github, aws cli, vscode installed to you pc 

Step 2:
Startup an ec2 instance on aws
ssh into you ec2 instance

Step 3:
Install dependences
pymongo, pandas, fastapi, uvicorn to your ec2 
clone your github repo to you ec2 or 
create a folder and copy python codes to the folder
Step 4:
Run server with uvicorn ecom:app --port 8081 --host '0.0.0.0'

How to use:
=================
Use the public ip of ec2 + colon + port/docs on web to view swagger page
