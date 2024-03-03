# Deploying a Lambda Function with GitHub Actions and Terraform

This repository contains Terraform configuration files and a GitHub Actions workflow to deploy a Python-based AWS Lambda function.

## Overview

The deployment process involves the following steps:

1. Packaging the Lambda function code into a ZIP file.
2. Creating necessary IAM roles and policies for the Lambda function.
3. Deploying the Lambda function using Terraform.
4. Cleaning up artifacts after deployment.

## Prerequisites

Before deploying the Lambda function, ensure you have the following prerequisites set up:

- An AWS account with appropriate permissions to create Lambda functions, IAM roles, and policies.
- Python-based Lambda function code packaged into a ZIP file.
- Terraform installed on your local machine or your CI/CD environment.
- AWS credentials configured either through environment variables or the AWS CLI.

## GitHub Actions Workflow

The deployment workflow is automated using GitHub Actions. It consists of the following steps:

1. **Checkout repository**: This step checks out the repository code.
2. **Setup Terraform**: This step sets up Terraform with the specified version.
3. **Initialize Terraform**: This step initializes Terraform within the `lambda/` directory.
4. **Format and validate Terraform configuration**: This step formats and validates the Terraform configuration files.
5. **Plan Terraform changes**: This step creates an execution plan to preview the changes Terraform will make.
6. **Apply Terraform changes**: This step applies the changes to deploy the Lambda function.
7. **Clean up Terraform artifacts**: This step removes Terraform artifacts to keep the workspace clean.
8. **Clean up Lambda ZIP file**: This step removes the Lambda function ZIP file.

For detailed configuration and customization, refer to the `.github/workflows/deploy_lambda.yml` file in this repository.

## Terraform Configuration

The Terraform configuration files (`main.tf`, `variables.tf`, `outputs.tf`, etc.) define the infrastructure resources required for deploying the Lambda function. These files include:

- Definition of IAM roles and policies.
- Configuration of the Lambda function itself.
- Any additional resources required by the Lambda function, such as VPC settings or event source mappings.

Customize these files according to your specific requirements, such as function name, runtime, and environment variables.

## Getting Started

To deploy the Lambda function:

1. Fork or clone this repository.
2. Add your Python-based Lambda function code to a ZIP file named `lambda_function.zip` in the `lambda/` directory.
3. Modify the Terraform configuration files (`main.tf`, `variables.tf`, etc.) as needed.
4. Configure your AWS credentials either through environment variables or the AWS CLI.
5. Commit and push your changes to trigger the deployment workflow.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
