1. Create a Conda Environment
conda create -n medibot python=3.10 -y
conda activate medibot
2. Install the Requirements
pip install -r requirements.txt
3. Create .env File

Create a .env file in the root directory and add your Pinecone & OpenAI credentials:

PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
4. Store Embeddings to Pinecone
python src/store_index.py
5. Run the Application
python app.py

Then open:

http://localhost:8000
Tech Stack Used

Python

LangChain

Flask

GPT

Pinecone

AWS (EC2, ECR)

CI/CD Deployment with GitHub Actions

AWS Deployment Steps
1. Login to AWS Console
2. Create IAM User for Deployment

Attach the following policies:

AmazonEC2ContainerRegistryFullAccess

AmazonEC2FullAccess

3. Create ECR Repository

Save the URI, for example:

302263089029.dkr.ecr.us-east-1.amazonaws.com/medicalbot
4. Build Docker Image of the Source Code
5. Push Docker Image to ECR
6. Launch EC2 Instance (Ubuntu)
7. Install Docker in EC2
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
8. Pull Docker Image from ECR in EC2
9. Run Docker Image in EC2
10. Configure EC2 as Self-Hosted GitHub Runner

Go to:

Settings → Actions → Runners → New self-hosted runner

Choose OS and run the provided commands in EC2 terminal.

11. Setup GitHub Secrets

Add the following secrets in GitHub:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION

ECR_REPO

PINECONE_API_KEY

OPENAI_API_KEY