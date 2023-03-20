# posnet

## Development Environment

|Category| - |
| --- | --- |
|Language|python v3.8.16|
|Web Framework|Django v3.2.18|

## How to Execute

Execute the following lines to properly clone and run the project.   
config.yaml file is required!!!

```
$ git clone https://github.com/qudwn1114/posnet.git
add config.yaml to /posnet/config 
$ conda create -n ["env"] python=3.8.16
$ conda activate ["env"]
$ cd posnet
$ pip install -r requirements.txt
$ python manage.py runserver