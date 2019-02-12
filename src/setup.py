from setuptools import setup, find_packages

setup (
  name                 = "todobackend",
  version              = "0.1.0",
  description          = "Todobackend Django REST service",
  packages             = find_packages(),
  include_package_data = True,
  scripts              = ["manage.py"],
  install_requires     = ["django",
                          "django-cors-headers==2.4.0",
                          "djangorestframework==3.9.1",
                          "mysqlclient==1.3.7",
                          "pytz==2018.9",
                          "uwsgi==2.0.18"],
  extras_require       = {
                          "test" : [
                            "colorama==0.4.1",
                            "coverage==4.5.2",
                            "django-nose==1.4.6",
                            "nose==1.3.7",
                            "pinocchio==0.4.2",
                            "pytz==2018.9",
                          ]
                        }
)