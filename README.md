# Project 01

Text analytics project.

## API Execution

```bash
sudo snap install docker
sudo docker pull --platform linux/x86_64 ghcr.io/uniandes-data-wizards/project-01-api:main
sudo docker run --platform linux/amd64 -p 8000:8000 ghcr.io/ghcr.io/uniandes-data-wizards/project-01-api:main
```

## Dashboard Execution

```bash
sudo snap install docker
sudo docker pull --platform linux/x86_64 ghcr.io/uniandes-data-wizards/project-01-app:main
sudo docker run --platform linux/amd64 -p 8050:8050 ghcr.io/ghcr.io/uniandes-data-wizards/project-01-app:main
```

## Deployment on a VM

Use a VM with Python3.10 and then run the following commands:

```bash
git clone https://github.com/uniandes-data-wizards/project-01.git
cd project-01/
sudo apt install python3-pip
pip3 install -r requirements.txt
cd model_deployment/
python -m uvicorn main:app --reload
```
For dashboard:

```bash
git clone https://github.com/uniandes-data-wizards/project-01.git
cd project-01/
sudo apt install python3-pip
pip3 install -r requirements.txt
python3 model_deployment/app.py
```

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](LICENSE)**
- Copyright 2023 © Felix Rojas, Daniel Reales & Juan Alegría
