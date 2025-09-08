from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="LLMOPS-Project",
    version="0.1",
    author="Siddhant",
    packages=find_packages(),
    install_requires = requirements,
)