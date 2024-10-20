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
  A New Frontier in Clipboard Management
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
> Much of this repository's release notes, README, and commit messages were created using [ChatGPT](https://chat.openai.com/) and [litellm](https://github.com/BerriAI/litellm).


## 🚀 Clip-Master-Toolkit Overview

Clip-Master-Toolkit is an innovative application that elevates clipboard management and utilization to the next level.  With a PyQt6-based GUI interface and integration with large language models (LLMs) via LiteLLM, it makes everyday text processing tasks more efficient and intelligent. Version 0.2.4 includes updated package versioning and PyPI publishing workflows, along with README file adjustments.  The project name has changed from `clip_master` to `clip-master-toolkit`, requiring updates to existing scripts and automation tasks.  The README is also updated in both English and Japanese. Improvements to `setup.py` clarify dependency management and add fallback handling for the absence of `requirements.txt`. This automatically installs `PyQt6`, `pyperclip`, `litellm`, `qt-material`, and `loguru`.


## ✨ Key Features

- **Clipboard History Management:** Saves previously copied text as a history for easy access and reuse.
- **LLM Integration:** Uses LiteLLM to process clipboard contents with various language models.
- **Customizable GUI:** Intuitive and user-friendly interface built with PyQt6.
- **Flexible Model Selection:** Allows you to freely specify the LLM model to use.
- **Export/Import Functionality:** Enables backup and restoration of clipboard history.
- **README Display in Streamlit App:** View the README content directly within the Streamlit application.


## 🔧 Usage

1. **Installation**:
   ```bash
   pip install clip-master-toolkit
   ```

2. **Launch**:
   ```bash
   clip-master-toolkit
   ```

3. **Basic Usage**:
   - Clipboard contents are displayed automatically.
   - Click the "Process with LLM" button to process text with an LLM.
   - Select and reuse past clipboard contents from the sidebar.
   - Run the Streamlit app to view the contents of README.md.


## 📦 Installation Instructions

Run `pip install clip-master-toolkit`. For upgrades, use `pip install --upgrade clip-master-toolkit`.


## 🆕 What's New (Version 0.2.4)

- 🚀 The project name has changed from `clip_master` to `clip-master-toolkit`. The CLI command has also changed from `clip_master` to `clip-master-toolkit`.  You need to update existing scripts and automation tasks.
- 🚀 The package version has been updated from `0.2.3` to `0.2.4`. The YAML front matter at the beginning of the README.md file has been removed and formatted. Extra blank lines in the README.md have been removed to improve readability. The `re` module has been added to enhance README.md processing.
- 🚀 The PyPI package name has been changed from `clip_master` to `clip-master-toolkit`.
- 🚀 Image paths in the README.md file have been corrected.
- 🚀 Improvements to `setup.py` clarify dependency management and add fallback handling if `requirements.txt` is missing.  `PyQt6`, `pyperclip`, `litellm`, `qt-material`, and `loguru` are automatically installed.


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributions

Contributions of all kinds are welcome, including pull requests, issues, and feature suggestions.  Please open an issue to discuss before making large changes.

## 🙏 Acknowledgements

Maki, iris-s-coon

## 📬 Contact

For questions or suggestions, please open a [Github issue](https://github.com/Sunwood-ai-labs/ClipMaster/issues). Email: sunwood.ai.labs@gmail.com


---

<p align="center">
  Revolutionize your clipboard experience with Clip-Master-Toolkit! 🚀✨
</p>