terraform {
  imports {
    pshynin-analyze-stocks = {
      source = "aws_lambda_function.pshynin_analyze_stocks"
    }
    pshynin-analyze-stocks-role = {
      source = "aws_iam_role.lambda_role"
    }
    pshynin-analyze-stocks-policy = {
      source = "aws_iam_policy.lambda_policy"
    }
  }
}

# IAM role for the Lambda function
resource "aws_iam_role" "lambda_role" {
  name = var.iam_role_name

  assume_role_policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Effect    = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
      Action    = "sts:AssumeRole"
    }]
  })

  lifecycle {
    ignore_changes = [
      assume_role_policy,  # Ignore changes to assume role policy, other attribute changes will be applied
    ]
    prevent_destroy = true  # Prevents the IAM role from being destroyed
  }
}

# IAM policy for the Lambda function
resource "aws_iam_policy" "lambda_policy" {
  name        = var.iam_policy_name
  description = "Policy for ${var.iam_role_name} Lambda function"

  policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Effect   = "Allow",
      Action   = "logs:CreateLogGroup",
      Resource = "arn:aws:logs:*:*:*"
    },
      {
        Effect   = "Allow",
        Action   = [
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = "arn:aws:logs:*:*:*"
      }]
  })
}

# Attach the policy to the role
resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  policy_arn = aws_iam_policy.lambda_policy.arn
  role       = aws_iam_role.lambda_role.name
}

# Lambda function
resource "aws_lambda_function" "pshynin_analyze_stocks" {
  function_name    = var.lambda_function_name
  filename         = var.lambda_function_zip_path
  source_code_hash = filebase64sha256(var.lambda_function_zip_path)
  role             = aws_iam_role.lambda_role.arn
  handler          = var.lambda_function_handler
  runtime          = var.lambda_function_runtime
}
