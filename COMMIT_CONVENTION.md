🧠 COMMIT MESSAGE CONVENTION FOR ML PROJECTS
--------------------------------------------

This repository follows a consistent commit message style inspired by Conventional Commits,
with additions for ML-specific workflows.

FORMAT
------
<type>: <short summary>

Example:
feat: add RandomForestRegressor training script
data: clean cellphone dataset and encode categorical features
model: save trained model v1.0 using joblib
serve: implement FastAPI prediction endpoint
deploy: deploy model API to Render


COMMIT TYPES
------------
data      - Changes or updates to datasets, preprocessing, or feature engineering
             Example: data: add cleaned cellphone dataset

feat      - Add new functionality or components (scripts, modules, features)
             Example: feat: add model evaluation script

model     - Model training, saving, loading, or tuning
             Example: model: train LinearRegression baseline

exp       - Experimentation and parameter tuning
             Example: exp: test RandomForest with max_depth=10

serve     - Serving models via API (FastAPI, Flask, etc.)
             Example: serve: create /predict endpoint

deploy    - Deployment to cloud (Render, Railway, Hugging Face Spaces)
             Example: deploy: first deployment of API

fix       - Fix bugs or errors in code or logic
             Example: fix: correct data scaling issue

refactor  - Code cleanup or restructuring without changing functionality
             Example: refactor: simplify preprocessing pipeline

docs      - Documentation updates (README, comments, setup guides)
             Example: docs: add API usage section

test      - Add or update tests
             Example: test: add tests for model evaluation

chore     - Maintenance tasks (requirements.txt, .gitignore, configs)
             Example: chore: update dependencies


EXAMPLES
--------
data: preprocess and normalize cellphone dataset
feat: add feature selection and scaling pipeline
model: train and evaluate RandomForestRegressor
exp: compare RandomForest vs LinearRegression results
serve: build FastAPI endpoint for price prediction
deploy: deploy API to Render with Dockerfile
docs: update README with API usage and deployment steps


TIPS
----
- Keep commits small and focused — one logical change per commit.
- Use imperative mood (e.g., "add", "update", "fix", not "added" or "fixed").
- Include details of major changes in the commit body if needed:

  Example:
  model: tune hyperparameters for RandomForest

  - max_depth=10
  - n_estimators=200
  - improved RMSE by ~5%

- Avoid committing large datasets or model binaries unless necessary.


RECOMMENDED WORKFLOW
--------------------
1. Stage only relevant files.
2. Write a clear, descriptive commit message.
3. Push after completing a self-contained step (data, training, serving, or deploy).

Example Workflow:
git add data_cleaning.py
git commit -m "data: clean and encode cellphone dataset"

git add train_model.py
git commit -m "model: train RandomForestRegressor and evaluate RMSE"

git add main.py
git commit -m "serve: expose /predict endpoint using FastAPI"

git add Dockerfile
git commit -m "deploy: containerize model for Render deployment"


OPTIONAL BRANCH NAMING CONVENTION
---------------------------------
Use consistent branch names for clarity and experiment tracking.

feature/<feature-name>      e.g., feature/serve-api
exp/<experiment-name>       e.g., exp/tuning-v2
fix/<issue-description>     e.g., fix/preprocessing-bug
docs/<update>               e.g., docs/update-readme


SUMMARY
-------
Following this format keeps your ML workflow organized and easy to track — 
from data prep to deployment.
