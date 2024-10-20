from setuptools import setup, find_packages
import os

print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())
print("README.md exists:", os.path.exists("README.md"))
print("requirements.txt exists:", os.path.exists("requirements.txt"))


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if os.path.exists("requirements.txt"):
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = fh.read().splitlines()
else:
    requirements = [
        "PyQt6",
        "pyperclip",
        "litellm",
        "qt-material",
        "loguru"
    ]
    
setup(
    name="clip-master-toolkit",
    version="0.2.3",
    author="Sunwood-ai-labs",
    author_email="sunwood.ai.labs@gmail.com",
    description="A comprehensive clipboard management toolkit with GUI and CLI interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sunwood-ai-labs/ClipMaster",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "clip_master": ["resources/*"],
    },
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "clip-master-toolkit=clip_master_toolkit.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
