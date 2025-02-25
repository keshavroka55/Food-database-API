from setuptools import setup, find_packages

setup(
    name="food_api",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "Flask-SQLAlchemy",
        "mysql-connector-python"
    ],
)
