from setuptools import find_packages, setup

setup(
    name="testing_loom_finance",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-duckdb",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)