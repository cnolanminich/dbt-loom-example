import os
from dagster_dbt import DbtProject
from pathlib import Path


dbt_project_path = Path(__file__).parent.parent.parent
DBT_PROJECT_DIR = os.fspath(dbt_project_path)

dbt_project = DbtProject(
    project_dir=dbt_project_path,
    state_path="target/",
    target="dev",
)
