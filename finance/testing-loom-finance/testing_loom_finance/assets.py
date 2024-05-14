from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .constants import dbt_manifest_path
from testing_loom_finance.project import (
    dbt_project,
)

@dbt_assets(
    manifest=dbt_project.manifest_path,
    select="finance.*")
def finance_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    