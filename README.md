# Wine-Quality-Prediction End-to-End

## Project Development - Step by Step
### Setup
1. Environment Creation: Separate environment for different projects.
```
conda create -p venv python==3.10 -y
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