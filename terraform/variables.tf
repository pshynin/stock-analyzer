variable "lambda_function_name" {
  description = "Name of the Lambda function"
  default     = "pshynin-analyze-stocks"
}

variable "lambda_function_handler" {
  description = "Handler function for the Lambda function"
  default     = "analyze_stocks.handler"
}

variable "lambda_function_runtime" {
  description = "Runtime for the Lambda function"
  default     = "python3.8"
}

variable "lambda_function_zip_path" {
  description = "Path to the Lambda function ZIP file"
  default     = "../lambda/analyze_stocks.zip"
}

variable "aws_region" {
  description = "AWS region where the Lambda function will be deployed"
  default     = "us-east-1"
}

variable "iam_role_name" {
  description = "Name of the IAM role for the Lambda function"
  default     = "pshynin-analyze-stocks-role"
}

variable "iam_policy_name" {
  description = "Name of the IAM policy for the Lambda function"
  default     = "pshynin-analyze-stocks-policy"
}
