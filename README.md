Abstract:
Api Crud operation deployed to aws ec2


Step 1:
required github, aws cli, vscode installed to pc 


Step 2:
Startup an ec2 instance on aws
ssh into the ec2 instance

Step 3:
Install dependencies
pymongo, pandas, fastapi, uvicorn to your ec2 
clone your github repo to you ec2 or 
create a folder and copy python codes to the folder


Step 4:
Run server with uvicorn ecom:app --port 8081 --host '0.0.0.0'


![run ecom server](https://user-images.githubusercontent.com/126528702/227372295-bc3586b7-c4b5-4383-90c5-61ee7a30d22a.PNG)

![ecom swagger page](https://user-images.githubusercontent.com/126528702/227372453-4f425c55-1e3e-47ad-bc7f-c2a709c82693.PNG)


How to use:
=================
Use the public ip of ec2 + colon + port/docs on web to view swagger page
Create an entry with post request and execute 

![fastapi_put](https://user-images.githubusercontent.com/126528702/227372152-e3b1b137-0179-4408-ae31-3b1f4d5b5abd.PNG)
