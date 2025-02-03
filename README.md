# Wine-Quality-Prediction End-to-End

## Project Development - Step by Step
### Setup
1. Environment Creation: Separate environment for different projects.
```
conda create -p venv python==3.10 -y
conda activate venv
```
2. Requirements in `requirements.txt`
```
pip install -r requirements.txt
```
3. Create the Project Structure - template.py`
```
python template.py
```
4. Implement Custom Logging
5. Implement `utils/common.py`

### Workflow
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Trainer
5. Model Evaluation

## Steps followed in every step of Workflow
1. Update `config.yaml`
2. Update `schema.yaml` -- Not in Data Ingestion
3. Update `params.yaml`
4. Update the entity
5. Update the configuration manager in `src`
6. Update the components
7. Update the pipeline
8. Update the `main.py`

## Running the End To End Project
1. Clone the repository:
```
git clone https://github.com/Agam-Patel-DS/wine-quality-prediction-end-to-end.git
```
2. Create Env
```
conda create -p venv python==3.10 -y
conda activate venv
```
3. Requirements in `requirements.txt`
```
pip install -r requirements.txt
```
4.a. Run the flask app (to train while running the app)
```
python app.py
```
4.b. Run the main.py (to only run training pipeline)
```
python main.py
```