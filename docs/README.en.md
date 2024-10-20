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
<img src="icon2.png" width="30%">
<br>
<h1 align="center">ClipMaster</h1>
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
  <a href="https://pypi.org/project/clip-master/"><img src="https://img.shields.io/pypi/v/clip-master.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/clip-master/"><img src="https://img.shields.io/pypi/dm/clip-master.svg" alt="PyPI downloads"></a>
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


## 🌟 Welcome to ClipMaster!

ClipMaster is an innovative application that takes clipboard management and utilization to the next level.  With a PyQt6-based GUI interface and integration with large language models (LLMs) via LiteLLM, it allows you to perform everyday text processing tasks more efficiently and intelligently.

## 🚀 Key Features

1. **Clipboard History Management**: Saves previously copied text as a history for easy access and reuse.
2. **LLM Integration**: Processes clipboard contents using various language models through LiteLLM.
3. **Customizable GUI**: Intuitive and user-friendly interface built with PyQt6.
4. **Flexible Model Selection**: Allows you to freely specify the LLM model to use.
5. **Export/Import Functionality**: Enables backup and restoration of clipboard history.

## 🛠️ Installation and Usage

1. **Installation**:
   ```bash
   pip install clip-master
   ```

2. **Launch**:
   ```bash
   clip_master
   ```

3. **Basic Usage**:
   - Clipboard contents are automatically displayed.
   - Click the "Process with LLM" button to process the text using an LLM.
   - Select past clipboard entries from the sidebar to reuse them.

## 📚 Project Structure

```
clip_master/
├── __init__.py
├── __main__.py
├── cli.py
├── config.py
├── core.py
├── gui.py
├── utils.py
├── workers.py
└── resources/
    └── icon2.png
```

## 🤝 Contributions

Contributions of all kinds are welcome, including pull requests, issues, and feature suggestions.  Please open an issue to discuss before making significant changes.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) - GUI framework
- [LiteLLM](https://github.com/BerriAI/litellm) - Provides access to various language models
- [pyperclip](https://github.com/asweigart/pyperclip) - Clipboard manipulation library
- [qt-material](https://github.com/UN-GCPDS/qt-material) - Material design style

## 📬 Contact

For questions or suggestions, please open a [Github issue](https://github.com/Sunwood-ai-labs/ClipMaster/issues).

---

<p align="center">
  Revolutionize your clipboard experience with ClipMaster! 🚀✨
</p>
```