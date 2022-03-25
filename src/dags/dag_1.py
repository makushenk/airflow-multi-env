from etl.config import settings
from etl.pipelines import color_output

DAG_ID = 'dag_1'


def dag():
    for env in settings.dags_envs_list[DAG_ID].to_list():
        config = settings.from_env(env)

        print(f"Running DAG [{DAG_ID}] through environment [{env}]")

        color_output.run(config)


if __name__ == '__main__':
    dag()
