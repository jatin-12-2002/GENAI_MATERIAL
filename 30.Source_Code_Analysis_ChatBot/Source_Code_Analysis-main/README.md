# Source Code Analysis ChatBot

## Installation

To set up the Source Code Analysis ChatBot locally, follow these steps:

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/Source_Code_Analysis
```

### Step-2: Navigate to the project directory:
```bash
    cd Source_Code_Analysis
```

### Step 3: Create a conda environment after opening the repository

```bash
    conda create -p env python=3.10 -y
```

```bash
    conda activate ./env
```

### Step 4: Install the requirements
```bash
    pip install -r requirements.txt
```

### Step-5: Set up environment variables:
- Create a .env file in the project directory.
- Define the necessary environment variables such as database connection strings, API keys, etc.
- My .env file is [here](https://drive.google.com/file/d/1HadmVnwU_LLi_XvA9ci9MHFLsq_p3Y3o/view?usp=sharing)
  
### Step-6: Run the Flask application:
```bash
    python store_index.py
```

```bash
    python app.py
```