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
> このリポジトリのリリースノートやREADME、コミットメッセージの多くは、[ChatGPT](https://chat.openai.com/)や[litellm](https://github.com/BerriAI/litellm)を活用して作成されています。

## 🚀 ClipMasterの概要

ClipMasterは、クリップボードの管理と活用を次のレベルに引き上げる革新的なアプリケーションです。PyQt6を使用したGUIインターフェースと、LiteLLMを通じて大規模言語モデル（LLM）と統合されており、日常のテキスト処理タスクをより効率的かつインテリジェントに行うことができます。バージョン0.2.1では、StreamlitアプリへのREADME.md表示機能追加、READMEファイルのメタデータ追加によるアプリ概要の明確化、およびいくつかのバグ修正と改善を行いました。PyPIパッケージ名も`clip-master`に変更されていますのでご注意ください。

## ✨ 主な機能

- クリップボード履歴管理：過去にコピーしたテキストを履歴として保存し、簡単にアクセス・再利用できます。
- LLM統合：LiteLLMを使用して、クリップボードの内容を様々な言語モデルで処理できます。
- カスタマイズ可能なGUI：PyQt6で構築された直感的で使いやすいインターフェース。
- フレキシブルなモデル選択：使用するLLMモデルを自由に指定可能。
- エクスポート/インポート機能：クリップボード履歴のバックアップと復元が可能。
- StreamlitアプリへのREADME表示：StreamlitアプリでREADMEの内容を直接確認できます。


## 🔧 使用方法

1. **インストール**:
   ```bash
   pip install clip-master
   ```

2. **起動**:
   ```bash
   clip-master
   ```

3. **基本的な使い方**:
   - クリップボードの内容は自動的に表示されます。
   - 「LLMで処理」ボタンをクリックして、テキストをLLMで処理します。
   - サイドバーから過去のクリップボード内容を選択して再利用できます。
   - Streamlitアプリを実行することで、README.mdの内容を確認できます。


## 📦 インストール手順

`pip install clip-master` を実行してください。バージョンアップには `pip install --upgrade clip-master` を使用してください。


## 🆕 最新情報

- StreamlitアプリにREADME.md表示機能を追加しました。
- プロジェクトメールアドレスとバージョン番号を更新しました。(バージョン 0.2.1)
- README.mdを更新し、プロジェクト概要を英語と日本語の両方で記述、各セクションの見出しを明確化、箇条書きを多用して内容を分かりやすく整理しました。使用しているライブラリ、GitHub Actionsなどのツールを利用した自動化をREADMEに反映しました。
- PyPIパッケージ名が `clip-master` に変更されました。


## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 🤝 コントリビューション

プルリクエスト、イシュー、機能提案など、あらゆる形での貢献を歓迎します。大きな変更を加える前に、まずイシューを開いて議論しましょう。

## 🙏 謝辞

Maki、iris-s-coon

## 📬 連絡先

質問や提案がある場合は、[Githubのイシュー](https://github.com/Sunwood-ai-labs/ClipMaster/issues)を開いてください。  メールアドレス: sunwood.ai.labs@gmail.com


---

<p align="center">
  ClipMasterで、あなたのクリップボード体験を革新しましょう！🚀✨
</p>