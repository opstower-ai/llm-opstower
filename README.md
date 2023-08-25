# 🗼 OpsTower.ai AWS AI CLI Assistant

An AWS CLI AI assistant that can answer questions about your AWS resources and perform calculations on cloudwatch metrics from the command line.

<p align="center">
  <a href="https://asciinema.org/a/604723" target="_blank"><img src="https://asciinema.org/a/604723.svg" width=600 /></a>
</p>

<p align="center">
<a href="#user-content-install"><strong>Install</strong></a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="#user-content-usage"><strong>Usage</strong></a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="#user-content-demo-mode"><strong>Demo Mode</strong></a>
</p>

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

Set your API key. 
Use `demo` to try with a live AWS account we provide. Or, provide a key in the form of `AWS_ACCESS_KEY_ID:AWS_SECRET_ACCESS_KEY`:

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

See [some example questions](https://gist.github.com/itsderek23/300fb4184c10895f82a9b9eb62fabd60) the agent has been evaluated with and the [evaluation results](https://www.opstower.ai/2023-evaluating-ai-agents/).

## Demo Mode

You can execute commands against a demonstration AWS account that contains an EC2 instance, RDS instance, an Application Load Balancer, several Lambda functions, S3 buckets, and more. 

Set the opstower key to `demo`:

```bash
llm keys set opstower --value demo
```

## Uninstall

```bash
llm uninstall llm-opstower
```

## Creating a read-only IAM user

You can create an IAM user with read-only access for use with OpsTower.ai.

1. In the IAM Console, click on ‘Users‘ on the left or under IAM Resources. Then select ‘Add User‘.
2. Give the user a name (Eg: OpsTower) and click ‘Next‘.
3. Click the ‘Attach policies directly‘ button at the top.
4. Search for 'ReadOnlyAccess' and set 'Filter by type' to 'AWS managed - job function'.
5. Select the checkbox for the 'ReadOnlyAccess' policy and click ‘Next‘.
6. Click 'Create user'.
7. In the green confirmation banner at the top, click 'View user' button.
8. Click 'Security credentials' tab.
9. Under 'Access Keys' click the 'Create access key' button.
10. Click 'Third Party Service' and the confirmation checkbox. Click the 'next' button.
11. Leave the description blank and click 'Create access key'.
12. Click the 'Download .csv file' button and save the file to your computer. Open the file and use the keys.

## How it works

OpsTower.ai provides a OpenAI-compatible API. The `llm` CLI utility sends your credentials and question to our API. We then generate AWS SDK code to answer your question and execute it in an isolated environment, summarizing the response.

## Limitations

1. Only read-only operations are permitted. To be safe, you should only use an IAM user with read-only access.
2. OpsTower.ai does not support higher-level and/or abstact questions like "Has there been a sudden change in any critical ec2, rds, or s3 metrics?". Try to be specific.
3. Support for the `llm --continue` option is not yet available.



