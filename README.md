# 🗼 OpsTower.ai AWS AI CLI Assistant

Do you have trouble navigating the AWS console and remembering AWS CLI commands? You do?! Well, you're in luck!

This is an AWS CLI AI assistant that lets you fetch information about your AWS resources using natural language.

## Installation

Installed as a plugin for [LLM](https://llm.datasette.io/), A CLI utility and Python library for interacting with Large Language Models.

Install `llm` if you haven't yet:

```bash
pip install llm
```

Install the OpsTower plugin:

```bash
llm install https://github.com/opstower-ai/llm-opstower/archive/refs/heads/main.zip
```

Set your API key. When prompted, provide your API key in the form of `AWS_ACCESS_KEY_ID:AWS_SECRET_ACCESS_KEY`:

```bash
 llm keys set opstower
```

Make `opstower` your default model:

```bash
llm models default opstower
```

## Usage

```bash
llm 'What is the average CPU utilization of my EC2 instances?'
```

See [some example questions](https://gist.github.com/itsderek23/300fb4184c10895f82a9b9eb62fabd60) the agent has been tested with as well as our current [evaluation results](https://www.opstower.ai/2023-evaluating-ai-agents/).

## Example output:

```bash
% llm 'What is the average CPU utilization of my EC2 instances?'

Log:
https://app.opstower.ai/chats/d98adf29-3973-4352-805a-8232e1c97367/transcript

I'll fetch all the EC2 instances and calculate their average CPU utilization.

Generating AWS SDK code...this will take up to 60 seconds...

The average CPU utilization of your EC2 instances is approximately 40.12%.
```


