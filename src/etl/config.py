from pathlib import Path

from dynaconf import Dynaconf

__all__ = ["settings"]

root_path = str(Path(__file__).resolve().parent.parent.parent.parent)

settings = Dynaconf(
    environment=True,
    envvar_prefix="ETL",
    load_dotenv=True,
    root_path=root_path,
    settings_files=[".envs/.alpha.toml", ".envs/.beta.toml", ".envs/.gamma.toml", ".envs/.lambda.toml"],
    vault_enabled=True,
)
