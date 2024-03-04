output "aws_iam_role_name" {
  value = aws_iam_role.lambda_role.name
}

output "aws_iam_role_arn" {
  value = aws_iam_role.lambda_role.arn
}

output "lambda_policy_name" {
  value = aws_iam_policy.lambda_policy.name
}
output "lambda_policy_arn" {
  value = aws_iam_policy.lambda_policy.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.pshynin_analyze_stocks.function_name
}

output "lambda_function_arn" {
  value = aws_lambda_function.pshynin_analyze_stocks.arn
}
