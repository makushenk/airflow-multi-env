
## Vault

By default Vault is available at http://localhost:8200

Follow instructions below to set up Vault

 1. Login to vault. The token value is `dev-root-token`

    ![Login Form](https://github.com/makushenk/airflow-multi-env/blob/master/.__static__/vault-login.png?raw=true)

 2. Go to `secret` engine
 
    ![Engine 'secret'](https://github.com/makushenk/airflow-multi-env/blob/master/.__static__/vault-secret-engine.png?raw=true)
 
 4. Add new secret (switch to json format)

     - *path for the secret*: `etl/default`
     - *secret data*: *copy from `.vault/default-dags-env-list.json` file*

    ![New secret](https://github.com/makushenk/airflow-multi-env/blob/master/.__static__/vault-new-secret.png?raw=true)

### Important note

In development mode Vault stores its secrets **in-memory**. If you restart vault service you'll lose all secrets you created.
