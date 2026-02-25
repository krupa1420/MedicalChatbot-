# MedicalChatbot-
Medical Chatbot with LLMs, LangChain, Pinecone, Flask &amp; AWS

# How to run?
clone the repo
```bash 
git clone https://github.com/krupa1420/MedicalChatbot-.git

##1. create a conda environment 

```bash
conda create -n medibot python=3.10 -y

```bash 
conda activate medibot

##2. install the requirements
```bash 
pip install -r requirements.txt

##3. icreate env file
```bash 
Create a .env file and add your Pinecone & OpenAI credentials:

PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

##4. Store embeddings to Pinecone
```bash 
python store_index.py


##5. Run the application
```bash
python app.py
Then open:
http://localhost:8000


###**Tech Stack Used**
-Python
-LangChain
-Flask
-GPT
-Pinecone
-AWS (EC2, ECR)
-CI/CD Deployment with GitHub Actions


##**AWS Deployment Steps**

#1.Login to AWS console.

#2.Create IAM user for deployment (with specific access):

AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess

#3.Create ECR repo to store/save docker image Save the URI:

302263089029.dkr.ecr.us-east-1.amazonaws.com/medicalbot

#4.Build docker image of the source code.

#5.Push docker image to ECR.

#6.Launch EC2 instance (Ubuntu).

#7.Install Docker in EC2:

sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

#8.Pull docker image from ECR in EC2.

#9.Run docker image in EC2.

#10.Configure EC2 as a self-hosted GitHub runner:

Go to Settings > Actions > Runners > New self-hosted runner
Choose OS
Run the provided commands in EC2 terminal

#11.Setup GitHub Secrets:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
OPENAI_API_KEY

