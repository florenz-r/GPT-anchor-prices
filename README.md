# GPT-anchor-prices

## Reproduce Experiments

### 1. Create virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies:
```
pip install -r requirements.txt
```

### 3. Set up your OpenAI API key:

1. Create a file named openai_key in the root directory of the project. Add your OpenAI API key to this file. Prepare the experiment data:
2. Setup the experiment_data.py file as shown in the existing file.

### 4. Run Script
```
python run_experiment.py --file_name experiment_results.csv
```

## Check Results

Open the `experiment_results.csv` file for further data analysis.