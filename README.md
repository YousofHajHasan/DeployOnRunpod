
This is the documentation for my first deployment of a 'Hugging Face' model on Runpod serverless.  
So, this is only a reference to me for the following deployments.  
  
In this tutorial, I want to deploy the OpenAI's whisper model, which is available publically on [HuggingFace](https://huggingface.co/openai/whisper-large-v3)  
  
  
Actually, Runpod's Quick Deploy provides a fast-whisper model, which reimplementation OpenAI's Whisper model using CTranslate2, which is a fast inference engine for Transformer models. But I only want to mimic the deployment for any other Huggingface model that is unavailable in Runpod's Quick Deploy.  
  

This tutorial is a good starting point for [getting started with Runpod endpoints](https://docs.runpod.io/serverless/get-started)

  

## For this tutorial, I need the following:

- Docker installed on your machine.

- Runpod API Key and a 5$ minimum charged to the account.

- AWS account "or any other cloud for storage."

  

## We will end up with the following files:

- `rp_handler.py`: Python script handles the input of the JSON file inside Runpod endpoints.
- `dockerfile`: Defines the container environment for the application.
- send.py`: Python script to send requests to the endpoint.
- `PrepareURL`: Python script used to generate the audio file URL inside the S3 bucket.

## Step 1: Generate the audio file URL `PrepareURL.py`:
- This file needs the `boto3` library to be installed in your environment.
- You need to specify the AWS credentials to access AWS API.
	- To get AWS credentials, you can navigate to AWS Console then on the top right got to **security credentials** page
	- Using your command prompt, run the following commands:
	```bash 
	set AWS_ACCESS_KEY_ID=your-access-key-id
	set AWS_SECRET_ACCESS_KEY=your-secret-access-key
	set AWS_DEFAULT_REGION=your-region 
	```
**The generated URL is only available for one hour*	

## Step 2: Preparing the rp_handler.py File  
This file is the core of the application, responsible for handling the input JSON and processing it using the Whisper model.

## Step 3: Preparing the Dockerfile  
The Dockerfile defines the container environment for deploying the Whisper model.
You need to download FFmpeg as one of the system dependecies

## Step 4: Deploying the files to Runpod
**You need to start by building our Docker image:**
```bash 
docker build --tag yousofhajhasan24/ready-runpod:1.0.0 .
```

**Then pushing it to a Container Registry:**
```bash
docker push yousofhajhasan24/whisper-runpod2:latest
```

Now 
- login to **Runpod**
-   Select "Deploy Serverless Endpoint."
-   Use the container image: `yousofhajhasan24/whisper-runpod2:latest`.
-   Configure the endpoint with appropriate memory, CPU, and GPU settings.


All Done...

#### General Notes:
- Any print statement will appear on the logs not in the returned output -JSON File-.'
- You can combine the two Python scripts in one script that generates the URL and pass it to the model inference.
 
