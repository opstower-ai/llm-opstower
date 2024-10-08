# 🗼 OpsTower.ai - DevOps AI Assistant

See beyond your dashboards, metrics, and logs. OpsTower.ai takes the grunt work out of DevOps, connecting to your systems (AWS, Docker, Kubernetes, etc) and debugging problems on its own.

🚧 As of Oct '23, OpsTower.ai can answer questions about your AWS resources and perform calculations on cloudwatch metrics from the command line. [Learn about our larger vision](#user-content-vision).

__🏆 OpsTower.ai is the current SOTA for accuracy in the [DevOps AI Assistant Open Leaderboard](https://github.com/opstower-ai/devops-ai-open-leaderboard) for AWS Services, AWS Cloudwatch Metrics, and AWS Billing.__

_📅 [Book a time on my calendar](https://calendly.com/derek-haynes) or email derek@opstower.ai to chat about what capabalities you'd like to see._

<p align="center">
  <a href="https://www.loom.com/share/dcab0392e5104364a8dcc6a05491b906?sid=378db519-45c7-49df-b792-6d7af0d8854a" target="_blank"><img src="https://public-opstower.s3.amazonaws.com/demo_screenshot.png"/></a>
</p>

<p align="center">
<a href="#user-content-vision"><strong>Vision</strong></a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="#user-content-install"><strong>Install</strong></a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="#user-content-usage"><strong>Usage</strong></a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="#user-content-demo-mode"><strong>Demo Mode</strong></a>
</p>

## Vision

OpsTower.ai is AI Assistant that takes the grunt work out of DevOps. OpsTower.ai connects to your systems (AWS, Docker, Kubernetes, etc) and debugs and researches problems on its own.

You've probably played with some fragile demos in this space. That's not OpsTower.ai. At the heart of OpsTower.ai is a robust evaluation framework that allows us to measure the agent's performance against a large dataset of questions across problem domains. We're building a platform that will allow us to iterate on the agent's capabilities and measure its performance over time. We'll transparently share our results.

See our [Capabilities Roadmap](#user-content-capabilities-roadmap) below for more details on current evaluation results and planned knowledge areas.

## Install

Installed as a plugin for [LLM](https://llm.datasette.io/), A CLI utility for interacting with LLMs.

Install `llm` if you haven't yet:

```bash
pip install llm
```

Install the OpsTower plugin:

```bash
llm install https://github.com/opstower-ai/llm-opstower/archive/refs/heads/main.zip
```

Set your API key. Use `demo` to try with a live AWS account or see [our docs](docs/aws_read_only_iam_user.md) for on creating a read-only IAM user.

```bash
llm keys set opstower --value demo
```

Make `opstower` your default model:

```bash
llm models default opstower
```

## Usage Examples

__AWS Services__

```bash
llm "list each ec2 instance id, name, state, last restart, image, and size"
```

__AWS Cloudwatch Metrics__

```bash
llm "What is the average CPU utilization of my EC2 instances?"
```
__AWS Billing__

```bash
llm "breakdown bill by aws service over the past 30 days"
```

_The default timeframe is the past hour. You can specify a different timeframe in the question (ex: "...over the past 10 minutes")._

## How it works

![how it works](https://www.opstower.ai/assets/images/agent_eval/agent_orch.png)

OpsTower.ai provides a OpenAI-compatible API. The `llm` CLI utility sends your credentials and question to our API. Server-side, OpsTower.ai generates AWS SDK code to answer your question and execute it in an isolated environment, summarizing the response.

Read how the agent is structured and our current [evaluation results](https://www.opstower.ai/2023-evaluating-ai-agents/) against an AWS question dataset.

## Authentication

You can query against your account by setting your API key in the following format:

```bash
llm keys set opstower --value AWS_ACCESS_KEY_ID:AWS_SECRET_ACCESS_KEY:AWS_REGION
```

## Demo Mode

You can execute commands against a demonstration AWS account that contains an EC2 instance, RDS instance, an Application Load Balancer, several Lambda functions, S3 buckets, and more.

Set the opstower key to `demo`:

```bash
llm keys set opstower --value demo
```

## Capabilities Roadmap

Just like how a Junior DevOps engineer isn't assigned with high-level tasks, OpsTower.ai's training is starting with a focus on information retrieval (ex: "what is our estimated AWS bill for this month"). After building up a base set of skills, OpsTower.ai will tackle reasoning you cannot infer from a ready-made dashboard (ex: "what resources appear to be not used and/or over-provisioned and how much could we reduce costs?").

| Knowledge area | Status | Accuracy % |
| -------- | -------- | -------- |
| AWS services  | Released  | [92%](https://github.com/opstower-ai/devops-ai-open-leaderboard#-current-leaderboard)  |
| AWS cloudwatch metrics | Released  | [89%](https://github.com/opstower-ai/devops-ai-open-leaderboard#-current-leaderboard)  |
| AWS billing  | Released  | [91%](https://github.com/opstower-ai/devops-ai-open-leaderboard#-current-leaderboard)  |
| AWS cloudwatch logs  |  🚧 | N/A |
| AWS deployment  |   | N/A  |
| AWS security  |   | N/A  |
| Advanced AWS reasoning  |   | N/A  |
| Docker  |   | N/A  |
| Kubernetes  |   | N/A  |
| Terraform  |   | N/A  |
| Advanced Kubernetes reasoning  |   | N/A  |
| Incident Investigation  |   | N/A  |

## Limitations

1. Only read-only operations are permitted. To be safe, you should only use an IAM user with read-only access.
2. OpsTower.ai does not support higher-level and/or abstact questions like "Has there been a sudden change in any critical ec2, rds, or s3 metrics?". Try to be specific.
3. Support for the `llm --continue` option is not yet available.

## Uninstall

```bash
llm uninstall llm-opstower
```
