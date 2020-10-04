# tgbot-aws-lambda-template
Template to create a simple Telegram Bot to run in AWS Lambda environment.
## Getting started.
This template is tested with Python 3.8.5.
AWS Lambda - serverless function that runs on trigger (https://aws.amazon.com/lambda).
The template uses AWS API Gateway as a trigger (https://aws.amazon.com/api-gateway).

To run this template in AWS Lambda you have to:
1. Create AWS Account
2. Create AWS Lambda function using "Author from scratch" case with runtime environment "Python 3.8"
3. Add AWS open HTTP API Gateway trigger to function
4. Get Telegram API token using BotFuther (https://t.me/botfather)
5. Set AWS Lambda environment variables:
TOKEN - Telegram API token
WEBHOOK_URL - AWS API Gateway invoke URL (https://<aws-url>/<api-route>)
6. create and upload function.zip to AWS Lambda:
```
$ git clone https://github.com/whataboutio/tgbot-aws-lambda-template.git
$ cd tgbot-aws-lambda-template
$ pip3 install --target ./package pyTelegramBotAPI
$ cd package
$ zip ${OLDPWD}/function.zip .
$ cd ${OLDPWD}
$ zip -g function.zip lambda_function.py
```
7. deploy your AWS Lambda function

Template bot: http://t.me/AWSLambdaTemplateBot