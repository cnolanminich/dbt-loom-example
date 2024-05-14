import os
from dagster_dbt import DbtProject
from pathlib import Path


dbt_project_path = Path(__file__).parent.parent.parent.joinpath("finance")
DBT_PROJECT_DIR = os.fspath(dbt_project_path)

dbt_project = DbtProject(
    project_dir=DBT_PROJECT_DIR,
    state_path=f"{DBT_PROJECT_DIR}/target/",
    target="dev",
)
