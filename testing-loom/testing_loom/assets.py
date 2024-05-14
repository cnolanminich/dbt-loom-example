from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .constants import dbt_manifest_path

from testing_loom.project import (
    dbt_project,
)
@dbt_assets(manifest=dbt_manifest_path)
def core_dbt_assets(context: AssetExecutionContext, dbt_core: DbtCliResource):
    yield from dbt_core.cli(["build"], context=context).stream()


@dbt_assets(
    manifest=dbt_project.manifest_path,
    select="finance.*")
def finance_dbt_assets(context: AssetExecutionContext, dbt_finance: DbtCliResource):
    yield from dbt_finance.cli(["build"], context=context).stream()
    