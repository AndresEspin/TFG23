# TFG23

* setup venv 
    ```bash
    $ python3 -m venv .venv
    $ souce .venv/bin/activate
    $ pip install -r requirements.txt
    $ deactivate
    ```

# Utils

## GDriveUtils
Para configurar la utilidad:

* Crear credenciales para usar la api de google( https://medium.com/@chingjunetao/simple-way-to-access-to-google-service-api-a22f4251bb52 ).

* Renombrar el fichero de credenciales a ./client_secrets.json

Para ejecutar el tst
* Editar los parámetros de configuración de la localización de los ficheros en tst/gdrive.tst.py:
    ```python
    [...]
    HOST=GDriveHost.SHARED_WITH_ME # or GDriveHost.MINE
    FILE_LOCATION_PATH="/TFG"
    [...]
    ```
* ejecutar tst desde carpeta raiz del proyecto
    ```bash
    $ python3 tst/gdrive_tst.py
    ```