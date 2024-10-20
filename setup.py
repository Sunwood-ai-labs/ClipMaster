from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="clip_master",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A clipboard management tool with GUI and CLI interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/clip_master",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "clip_master": ["resources/*"],
    },
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "clip_master=clip_master.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
