import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets import core_dbt_assets, finance_dbt_assets
from .constants import dbt_project_dir
from .schedules import schedules
from .project import DBT_PROJECT_DIR

defs = Definitions(
    assets=[core_dbt_assets, finance_dbt_assets],
    schedules=schedules,
    resources={
        "dbt_core": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
        "dbt_finance": DbtCliResource(project_dir=DBT_PROJECT_DIR),
    },
)