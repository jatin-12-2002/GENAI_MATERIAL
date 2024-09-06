# Ollama Tutorial

## Ollama Official Documentation: https://github.com/ollama/ollama?tab=readme-ov-file

## Installation of Ollama:

To set up the Ollama locally, follow these steps:

### Step-1: Download the Ollama:
```bash
    curl -fsSL https://ollama.com/install.sh | sh
```

### Step-2: Start the Ollama Server:
```bash
    ollama serve
```

### Step-3: Start the llama3.1 Server:
```bash
    ollama run llama3.1
```

### Step-4: Create the llama3.1 Server for our "modelfile":
```bash
    ollama create mario -f ./Modelfile
```

### Step-5: Start the llama3.1 Server for our "modelfile":
```bash
    ollama run mario
```

## To access the WebUI Interface of Ollama:

### Step-1: Run the Docker Container using this command:
```bash
docker run -d --network=host -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

## To Create a Gradio APP with LLama3.1:

To set up the Gradio ChatBot locally, follow these steps:

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/Ollama_Tutorial
```

### Step-2: Navigate to the project directory:
```bash
    cd Ollama_Tutorial
```

### Step 3: Create a conda environment after opening the repository

```bash
    conda create -p env python=3.10 -y
```

```bash
    source activate ./env
```

### Step 4: Install the requirements
```bash
    pip install -r requirements.txt
```

### Step-5: Run the test.py file:
```bash
    python test.py
```