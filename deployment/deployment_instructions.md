# deployment/deploy_instructions.md

## Cloud Run / Agent Engine Deployment Guide

This agent is configured to run inside a Docker container using the provided `Dockerfile`.

### 1. Build the Container Image

1.  Ensure you have Docker installed and the Google Cloud CLI (gcloud) setup.
2.  Run the build command from the root directory:
    ```bash
    gcloud builds submit --tag gcr.io/[PROJECT_ID]/halal-chef-agent
    ```
    *Replace [PROJECT_ID] with your Google Cloud project ID.*

### 2. Deploy to Cloud Run

1.  Deploy the built image to Cloud Run:
    ```bash
    gcloud run deploy halal-chef-agent --image gcr.io/[PROJECT_ID]/halal-chef-agent --region us-central1 --platform managed --allow-unauthenticated
    ```

**Note:** This demonstrates readiness for deployment. The agent runs once (`python main.py`) and completes its task, suitable for a serverless execution environment.