from setuptools import setup, find_packages #the setup script is responsible for building, distributing and installing modules using DisUtils

setup(
    name = "algoz",
    version = "1.0.0",
    packages = find_packages(),
    entry_points={"console_scripts":["algoz=app:main"]},#algoz stands for what we want to use to call the main function in our app.py file.
)