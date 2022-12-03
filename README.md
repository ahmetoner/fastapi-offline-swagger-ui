# Fastapi Offline Swagger UI
By default FastAPI uses CDN for swagger ui assets (js and css files), with this repository you can use it offline. This repository aims to download CDN urls and store inside of a python module. You can easily use this downloaded assets with following examples.

## Install
You can install this software via pip or poetry.

```sh
pip3 install git+https://github.com/ahmetoner/fastapi-offline-swagger-ui
```

or pyproject.toml

```sh

[tool.poetry.dependencies]
...
fastapi-offline-swagger-ui = {git = "https://github.com/ahmetoner/fastapi-offline-swagger-ui"}

```


## Usage Examples
After installing the module, create a python file. Copy and run following.
```py
from fastapi import FastAPI, File, UploadFile, Query, applications
from fastapi.responses import StreamingResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
import fastapi_offline_swagger_ui

app = FastAPI()

''' This following code block necessary to switch offline cdn files via fastapi_offline_swagger_ui module
'''
assets_path = fastapi_offline_swagger_ui.__path__[0]
if path.exists(assets_path + "/swagger-ui.css") and path.exists(assets_path + "/swagger-ui-bundle.js"):
    app.mount("/assets", StaticFiles(directory=assets_path), name="static")
    def swagger_monkey_patch(*args, **kwargs):
        return get_swagger_ui_html(
            *args,
            **kwargs,
            swagger_favicon_url="",
            swagger_css_url="/assets/swagger-ui.css",
            swagger_js_url="/assets/swagger-ui-bundle.js",
        )
    applications.get_swagger_ui_html = swagger_monkey_patch

```

## Live Example
Alternatively you can browse [ahmetoner/whisper-asr-webservice](https://github.com/ahmetoner/whisper-asr-webservice/) repository to see how it is implemented.
