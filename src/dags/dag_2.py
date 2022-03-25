from etl.config import settings
from etl.pipelines import fibonacci

DAG_ID = 'dag_2'


def dag():
    for env in settings.dags_envs_list[DAG_ID].to_list():
        config = settings.from_env(env)

        print(f"Running DAG [{DAG_ID}] through environment [{env}]")

        fibonacci.run(config)


if __name__ == '__main__':
    dag()
