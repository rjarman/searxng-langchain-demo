# SearxNG LangChain Demo

This is a demo project that shows how to use SearxNG with LangChain. It demonstrates two main use cases:
1. Simple search using SearxNG
2. Using SearxNG as a tool with a LangChain agent

## Prerequisites

- Python 3.11 or higher
- A running SearxNG instance (default: http://localhost:8080)
- OpenAI API key (for the agent example)

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -e .
```

3. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'  # On Windows: set OPENAI_API_KEY=your-api-key-here
```

## Usage

Run the demo:
```bash
python main.py
```

The script will demonstrate:
1. A simple search using SearxNG
2. Using SearxNG as a tool with a LangChain agent

## Configuration

The SearxNG host is configured in `main.py`. By default, it's set to `http://localhost:8080`. You can modify this to point to your SearxNG instance.
