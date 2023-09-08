# 🗼 OpsTower.ai - DevOps AI Assistant

See beyond your dashboards, metrics, and logs. OpsTower.ai takes the grunt work out of DevOps, connecting to your systems (AWS, Docker, Kubernetes, etc) and debugging problems on its own.

🚧 As of Sep '23, OpsTower.ai can answer questions about your AWS resources and perform calculations on cloudwatch metrics from the command line. [Learn about our larger vision](#user-content-vision).

_📅 [Book a time on my calendar](https://calendly.com/derek-haynes) or email derek@opstower.ai to chat about what capabalities you'd like to see._

<p align="center">
  <a href="https://asciinema.org/a/604723" target="_blank"><img src="https://asciinema.org/a/604723.svg" width=600 /></a>
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

We're building an AI Assistant that takes the grunt work out of DevOps. OpsTower.ai connects to your systems (AWS, Docker, Kubernetes, etc) and debugs and researches problems on its own.

You've probably played with some fragile demos in this space. That's not what we're building. At the heart of OpsTower.ai is a robust evaluation framework that allows us to measure the agent's performance against a large dataset of questions across problem domains. We're building a platform that will allow us to iterate on the agent's capabilities and measure its performance over time. We'll transparently share our results.

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

```bash
llm keys set opstower --value demo
```

Make `opstower` your default model:

```bash
llm models default opstower
```

## Usage

```bash
llm "What is the average CPU utilization of my EC2 instances?"
```

```bash
llm "Are all of our ec2 instances running?"
```

```bash
llm "how many cloudwatch alarms are in the alarm state?"
```

```bash
llm "Were there any Lambda invocations that lasted over 5 seconds in the last day?"
```

## How it works

![how it works](https://www.opstower.ai/assets/images/agent_eval/agent_orch.png)

OpsTower.ai provides a OpenAI-compatible API. The `llm` CLI utility sends your credentials and question to our API. We then generate AWS SDK code to answer your question and execute it in an isolated environment, summarizing the response.

Read how the agent is structured and our current [evaluation results](https://www.opstower.ai/2023-evaluating-ai-agents/) against an AWS question dataset.

## Authentication

You can query against your account by setting your API key in the following format:

```bash
llm keys set opstower --value AWS_ACCESS_KEY_ID:AWS_SECRET_ACCESS_KEY
```

## Demo Mode

You can execute commands against a demonstration AWS account that contains an EC2 instance, RDS instance, an Application Load Balancer, several Lambda functions, S3 buckets, and more.

Set the opstower key to `demo`:

```bash
llm keys set opstower --value demo
```


## Capabilities Roadmap

| Knowledge area | Status | Accuracy % |
| -------- | -------- | -------- |
| AWS resources & cloudwatch  | Preliminary  | [90%](https://www.opstower.ai/2023-evaluating-ai-agents/)  |
| AWS billing  |   | N/A  |
| AWS deployment  |   | N/A  |
| Docker  |   | N/A  |
| Kubernetes  |   | N/A  |
| Terraform  |   | N/A  |
| Incident Investigation  |   | N/A  |

## Other DevOps AI Assistants

| Name | Focus | Benchmarks? |
| -------- | -------- | -------- |
| [aiac](https://github.com/gofireflyio/aiac) | Infastructure as code | No |
| [KubeCtl-ai](https://github.com/sozercan/kubectl-ai) | Kubectl plugin for OpenAI GPT | No |
| [aiws](https://github.com/huseyinbabal/aiws) | AI Driven AWS CLI | No |
| [Terraform AI](https://github.com/jigsaw373/terraform-ai) | Terraform assistant for OpenAI GPT  | No |
| [tfgpt](https://github.com/flavius-dinu/tfgpt) | Provides explanations for Terraform commands and concepts | No |
| [ReleaseAI](https://release.ai/) | AWS CLI, Kubectl, Cron | No |

## Limitations

1. Only read-only operations are permitted. To be safe, you should only use an IAM user with read-only access.
2. OpsTower.ai does not support higher-level and/or abstact questions like "Has there been a sudden change in any critical ec2, rds, or s3 metrics?". Try to be specific.
3. Support for the `llm --continue` option is not yet available.

## Uninstall

```bash
llm uninstall llm-opstower
```
