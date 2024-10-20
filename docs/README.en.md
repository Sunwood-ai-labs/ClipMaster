---
title: ClipMaster
emoji: 🌖
colorFrom: pink
colorTo: purple
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
license: mit
---

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/ClipMaster/main/docs/icon2.png" width="30%">
<br>
<h1 align="center">Clip-Master-Toolkit</h1>
<h2 align="center">
  ～A New Frontier in Clipboard Management～
</h2>

<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/ClipMaster"><img src="https://img.shields.io/badge/GitHub-Repository-blue?logo=github" alt="GitHub Repository"></a>
  <a href="https://github.com/Sunwood-ai-labs/ClipMaster/stargazers"><img src="https://img.shields.io/github/stars/Sunwood-ai-labs/ClipMaster?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/Sunwood-ai-labs/ClipMaster/network/members"><img src="https://img.shields.io/github/forks/Sunwood-ai-labs/ClipMaster?style=social" alt="GitHub forks"></a>
  <a href="https://github.com/Sunwood-ai-labs/ClipMaster/commits/main"><img src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/ClipMaster" alt="GitHub last commit"></a>
  <a href="https://github.com/Sunwood-ai-labs/ClipMaster/search?l=python"><img src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/ClipMaster" alt="GitHub top language"></a>
  <a href="https://github.com/Sunwood-ai-labs/ClipMaster/releases"><img src="https://img.shields.io/github/v/release/Sunwood-ai-labs/ClipMaster?sort=semver&color=red" alt="GitHub release"></a>
  <a href="https://github.com/Sunwood-ai-labs/ClipMaster/tags"><img src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/ClipMaster?color=orange" alt="GitHub tag"></a>
  <a href="https://pypi.org/project/clip-master-toolkit/"><img src="https://img.shields.io/pypi/v/clip-master-toolkit.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/clip-master-toolkit/"><img src="https://img.shields.io/pypi/dm/clip-master-toolkit.svg" alt="PyPI downloads"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyQt6-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt6">
  <img src="https://img.shields.io/badge/LiteLLM-FF6F61?style=for-the-badge&logo=openai&logoColor=white" alt="LiteLLM">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/pip-3775A9?style=for-the-badge&logo=pypi&logoColor=white" alt="pip">
  <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown">

</p>

> [!IMPORTANT]
> Many of this repository's release notes, README, and commit messages were created using [ChatGPT](https://chat.openai.com/) and [litellm](https://github.com/BerriAI/litellm).


## 🚀 Clip-Master-Toolkit Overview

Clip-Master-Toolkit is an innovative application that takes clipboard management and utilization to the next level.  With a PyQt6-based GUI and integration with large language models (LLMs) through LiteLLM, it makes everyday text processing tasks more efficient and intelligent. Version 0.2.5 includes fixes for the version number and CLI entry point, updated build files, and an updated README.  Due to changes in the package structure, the path to the CLI entry point has changed.


## ✨ Key Features

- **Clipboard History Management:** Saves previously copied text as a history for easy access and reuse.
- **LLM Integration:** Processes clipboard contents using various language models via LiteLLM.
- **Customizable GUI:** Intuitive and user-friendly interface built with PyQt6.
- **Flexible Model Selection:** Allows you to freely specify the LLM model to use.
- **Export/Import Functionality:** Enables backing up and restoring clipboard history.
- **README Display in Streamlit App:** View the README content directly within the Streamlit app.


## 🔧 How to Use

1. **Installation**:
   ```bash
   pip install clip-master-toolkit
   ```

2. **Launch**:
   ```bash
   clip-master-toolkit
   ```

3. **Basic Usage**:
   - Clipboard contents are automatically displayed.
   - Click the "Process with LLM" button to process text using an LLM.
   - Select past clipboard contents from the sidebar to reuse them.
   - Run the Streamlit app to view the contents of README.md.


## 📦 Installation Instructions

Run `pip install clip-master-toolkit`. For updates, use `pip install --upgrade clip-master-toolkit`.


## 🆕 What's New (Version 0.2.5)

- **Updated Build Files:** Added `clip_master_toolkit.egg-info` to `.SourceSageignore` to prevent unnecessary files from being included in the version control system.
- **Improved `setup.py`:** Dependency management is clarified, and fallback handling is added for cases without `requirements.txt`. This automatically installs `PyQt6`, `pyperclip`, `litellm`, `qt-material`, and `loguru`.
- **CLI Entry Point Change:** Due to changes in the package structure, the CLI entry point path has changed from `clip_master_toolkit.cli:main` to `clip_master.cli:main`.  You may need to update existing scripts or automated tasks.
- **Updated README File:** The English and Japanese README files have been updated.


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## 🤝 Contributions

Contributions of all kinds are welcome, including pull requests, issues, and feature suggestions. Please open an issue to discuss before making large changes.


## 🙏 Acknowledgements

Maki, iris-s-coon


## 📬 Contact

For questions or suggestions, please open a [Github issue](https://github.com/Sunwood-ai-labs/ClipMaster/issues). Email: sunwood.ai.labs@gmail.com


---

<p align="center">
  Revolutionize your clipboard experience with Clip-Master-Toolkit! 🚀✨
</p>