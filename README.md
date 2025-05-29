# SearxNG + LangChain Integration Demo

[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=flat&logo=nginx&logoColor=white)](https://nginx.org/)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.25-yellow)](https://python.langchain.com/)

A comprehensive demo showcasing how to integrate SearxNG with LangChain in a production-ready environment. This demo includes Docker containerization, Nginx reverse proxy, rate limiting, and proper security configurations.

## 🚀 Quick Start with Docker

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)
- OpenAI API key
- `uv` package manager (for local development)

### Using Docker (Recommended)

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/searxng-langchain-demo.git
    cd searxng-langchain-demo
    ```

2. **Configure environment variables**:
    ```bash
    cp .env.example .env
    # Edit .env with your OpenAI API key and other settings
    ```

3. **Start the services**:
    ```bash
    docker compose up -d
    ```

The services will be available at:
- SearxNG web and api: http://127.0.0.1:8080
- Searxng health check: http://127.0.0.1:8080/healthz
- Nginx (main entry point): http://127.0.0.1:8080

### Local Development Setup

1. **Install uv**:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. **Create virtual environment**:
    ```bash
    uv venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    uv pip install -e .
    ```

4. **Replace the .env.example with your actual environment variables**:
    ```bash
    cp .env.example .env
    # Edit .env with your OpenAI API key and other settings
    ```

## 🔧 Configuration Information

- [docker-compose.yml](./docker-compose.yml)
- [src/configs/nginx.conf](./src/configs/nginx.conf)
- [src/configs/settings.yml](./src/configs/settings.yml)
- [src/configs/limiter.toml](./src/configs/limiter.toml)

## 💻 Usage Examples

- The [demo](./src/main.py) includes a simple LangChain flow that uses SearxNG as a search tool.

## 📚 Documentation

- [SearxNG Documentation](https://docs.searxng.org/)
- [LangChain Documentation](https://python.langchain.com/)
- [Docker Documentation](https://docs.docker.com/)
