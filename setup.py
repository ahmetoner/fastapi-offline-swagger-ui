from pathlib import Path
from urllib.request import urlretrieve
from setuptools import setup

PROJECT_NAME= "fastapi_offline_swagger_ui"

def download_cdn_files()  -> None:
    static_path = Path(__file__).parent / PROJECT_NAME
    static_path.mkdir(parents=True, exist_ok=True)
    for cdn_url in (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui.css",
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui-bundle.js",
    ):
        urlretrieve(cdn_url, static_path / cdn_url.split("/")[-1])

setup(
    name=PROJECT_NAME,
    version="1.0.0",
    author="Ahmet Oner",
    description="By default FastAPI uses CDN for swagger ui assets, with this repository you can use it offline.",
    long_description_content_type="text/markdown",
    url="https://github.com/ahmetoner/fastapi-offline-swagger-ui",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.6",
    install_requires=download_cdn_files(),
    include_package_data=True,
    packages=[PROJECT_NAME],
    package_data={'': ['*.css', '*.js']},
)
