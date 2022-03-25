
## Vault

---

By default Vault is available at http://localhost:8200

Follow instructions below to set up Vault

 1. Login to vault. The token value is `dev-root-token`

    ![Login Form](https://github.com/makushenk/airflow-multi-env/blob/master/__static__/vault-login.png?raw=true)

 2. Create new key/value storage
 
    ![Secrets Engines](https://github.com/makushenk/airflow-multi-env/blob/master/__static__/vault-enable-new-engine.png?raw=true)
 
    ![KV Engine](https://github.com/makushenk/airflow-multi-env/blob/master/__static__/vault-new-kv-engine.png?raw=true)
    
    ![KV Engine Settings](https://github.com/makushenk/airflow-multi-env/blob/master/__static__/vault-kv-engine-settings.png?raw=true)

 3. Add new secret (switch to json format for convenience)

    - path for the secret (name): `dags_env_list`
    - secret data: *copy from `.vault/default-dags-env-list.json` file* 
        
    ![Secret Data](https://github.com/makushenk/airflow-multi-env/blob/master/__static__/vault-secret-data.png?raw=true)

### Important note

In development mode Vault stores its secrets **in-memory**. If you restart vault service you'll lose all secrets you created.
