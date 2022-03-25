
build:
	docker-compose build

start:
	docker-compose up -d

run-1:
	docker exec -e "TERM=xterm-256color" -it airflow-multi-env_app_1 python src/dags/dag_1.py

run-2:
	docker exec -e "TERM=xterm-256color" -it airflow-multi-env_app_1 python src/dags/dag_2.py
