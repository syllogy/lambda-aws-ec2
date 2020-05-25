<p align="center">
  <img alt="header" src="https://www.simform.com/wp-content/uploads/2018/07/Add-subheading-5-4.png" width="250px" float="center"/>
</p>

<h1 align="center">Welcome to Project EC2 AWS Lambda Function</h1>

<p align="center">
  <strong>Lambda Function that help you Automating the Start/Stop of EC2 Instances</strong>
</p>

### Menu

<p align="center">
  <a href="#setup">Setup</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#architecture">Architecture</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#how-to-contribute">How to contribute</a>
</p>

## Copyright (c)

Stefanini Solutions (c) 2020 - **Team Cloud**

### Getting Started

To use this repository you need to make a **git clone**:

```bash
git clone --depth 1 https://git.stefanini.io/msp/aws/lambda/ec2.git -b master
```

This will give access on your **local machine** to this project.

### Built with

- [AWS](https://aws.amazon.com/pt/)
- [Python](https://www.python.org/)

### Pre-Requisites

* An AWS Account.
* Python 3.8 Version.

### Description

The use of this automation is to stop or start EC2 instances at a certain time every day. In our use case, we stop instances every night and start those instances in the next morning.

### Setup

I want to reduce my Amazon Elastic Compute Cloud (Amazon EC2) usage by stopping and starting my EC2 instances automatically. How do I use AWS Lambda and Amazon CloudWatch Events to do that? To this setup all that you need is:

1. Create a custom AWS Identity and Access Management (IAM) policy and execution role for your Lambda function.
2. Create Lambda functions that stop and start your EC2 instances.
3. Create CloudWatch Events rules that trigger your function on a schedule. For example, you could create a rule to stop your EC2 instances at night, and another to start them again in the morning.

**Policy Name**

* PolicyStartStopEC2
	* Policy used in Lambda Function to stop EC2 Instances

**Role Name**

* LambdaStartStopEC2

**Lambda Functions Name**

* StartEC2Instances
* StopEC2Instances

**Adding Trigger**

* CloudWatch Events/EventBridge

**CloudWatch Trigger**

* Name: TriggerEvery18Hour
* Description: Trigger Rule to run every 18 hour every day
* Schedule expression: cron(00 20 * * ? *)

**Note**: To implement this automation on EC2 instances, you have to add a tag in your instances. Tag key is **env** and the tag value is **hom**.

### Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
      {
          "Effect": "Allow",
          "Action": [
              "logs:CreateLogGroup",
              "logs:CreateLogStream",
              "logs:PutLogEvents"
          ],
          "Resource": "arn:aws:logs:*:*:*"
      },
      {
          "Effect": "Allow",
          "Action": [
              "ec2:DescribeInstances",
              "ec2:DescribeRegions",
              "ec2:StartInstances",
              "ec2:StopInstances"
          ],
          "Resource": "*"
      }
  ]
}
```

### Architecture

<p align="center">
  <img alt="aws-lambda-ec2" src="https://i.ytimg.com/vi/bv-CKOMPCpI/maxresdefault.jpg" width="700" float="center"/>
</p>

### Links

* https://aws.amazon.com/pt/blogs/apn-latam/automatizando-o-startstop-das-suas-instancias-ec2/
* https://www.linkedin.com/pulse/automa%C3%A7%C3%A3o-e-redu%C3%A7%C3%A3o-de-custos-na-aws-utilizando-tags-pierre-rezende/
* https://github.com/drezende/aws-lambda-start-stop/blob/master/lambda-stop-instances.py
* https://www.it-swarm.dev/pt/api/desligamento-automatico-e-iniciar-instancia-do-amazon-ec2/968113033/
* https://medium.com/@cmacetko/aws-ligando-e-desligando-uma-instancia-ec2-em-hor%C3%A1rios-determinados-b43ad357ee52
* https://aws.amazon.com/pt/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/
 
### How to contribute

>
> 1. Make a **Fork**.
> 2. Follow the project organization.
> 3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.
> 4. Make the **Commit**.
> 5. Open a **Pull Request**.
> 6. Wait for your pull request to be accepted.. 🚀
>
Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

### Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push origin master
```

### Versioning

- [CHANGELOG](CHANGELOG.md)

### Show your support

Give a ⭐️ if this project helped you!

### Project Status

* ✔️ Finish

---

Feito com ❤️ by **Cloud Team**
