from setuptools import setup, find_packages

setup(
    name="commit_it",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "questionary",  # Include any other dependencies here
    ],
    entry_points={
    "console_scripts": [
        "commit_it = commit_it.commit_it:main",
    ],
	}
)
