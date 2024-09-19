
<p align="center">
<img src="icon2.png" width="30%">
<br>
<h1 align="center">ClipMaster</h1>
<h2 align="center">
  ～クリップボード管理の新境地～

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Sunwood-ai-labs/ClipMaster)
[![GitHub stars](https://img.shields.io/github/stars/Sunwood-ai-labs/ClipMaster?style=social)](https://github.com/Sunwood-ai-labs/ClipMaster)
[![GitHub forks](https://img.shields.io/github/forks/Sunwood-ai-labs/ClipMaster?style=social)](https://github.com/Sunwood-ai-labs/ClipMaster)
[![GitHub last commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/ClipMaster)](https://github.com/Sunwood-ai-labs/ClipMaster)
[![GitHub top language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/ClipMaster)](https://github.com/Sunwood-ai-labs/ClipMaster)
[![GitHub release](https://img.shields.io/github/v/release/Sunwood-ai-labs/ClipMaster?sort=semver&color=red)](https://github.com/Sunwood-ai-labs/ClipMaster)
[![GitHub tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/ClipMaster?color=orange)](https://github.com/Sunwood-ai-labs/ClipMaster)

  <br>

</h2>

</p>

> **重要なお知らせ**
> このリポジトリのリリースノートやREADME、コミットメッセージの多くは、[ChatGPT](https://chat.openai.com/)や[litellm](https://github.com/Namek/py-litellm)を活用して作成されています。

## プロジェクト: ClipMaster

```plaintext
OS: nt
Directory: C:\Projects\ClipMaster

├─ clipmaster/
│  ├─ app.py
│  ├─ title_bar.py
│  ├─ llm_worker.py
│  ├─ resources/
│      ├─ clipboard_icon.png
├─ requirements.txt
├─ README.md
```

## 🌟 ClipMasterへようこそ！

ClipMasterは、クリップボードの管理と活用を次のレベルに引き上げる革新的なアプリケーションです。クリップボードの履歴管理、LLM（大規模言語モデル）との統合、そしてユーザーフレンドリーなインターフェースを備えています。メールやドキュメント作成など、日常のタスクをより効率的かつスマートにこなすことができます。

## 🚀 ClipMasterの特長

### 1. クリップボード履歴の管理

- 過去にコピーしたテキストを履歴として保存し、いつでも簡単にアクセスできます。
- サイドバーに履歴が表示され、クリックするだけで内容を再利用可能。

### 2. LLMとのシームレスな統合

- 大規模言語モデルを活用し、クリップボードの内容を加工・変換します。
- カスタムプロンプトを入力して、テキストの要約、翻訳、リライトなど多彩な処理が可能。

### 3. ユーザーフレンドリーなインターフェース

- 直感的に操作できる洗練されたデザイン。
- ウィンドウサイズの調整やドラッグ&ドロップでの移動も簡単。

### 4. カスタマイズ可能なモデル選択

- 使用する言語モデルを自由に指定可能。
- デフォルトでは `"bedrock/anthropic.claude-3-sonnet-20240229-v1:0"` が設定されています。

### 5. 生産性の向上

- コピーしたテキストを即座に加工し、クリップボードに反映。
- メールアプリやドキュメントエディタでの作業がスムーズに。

## 🛠️ 使い方

1. **必要なライブラリのインストール**

   ```bash
   pip install -r requirements.txt
   ```

2. **litellmの設定**

   - litellmを使用するために、必要なAPIキーや環境変数を設定してください。
   - 詳細は[litellmのドキュメント](https://github.com/Namek/py-litellm)を参照してください。

3. **アプリケーションの起動**

   ```bash
   python clipmaster/app.py
   ```

4. **基本的な操作**

   - **クリップボードの内容を表示**: クリップボードにコピーされたテキストがメインエリアに表示されます。
   - **LLMで処理**: カスタムプロンプトとテキストを入力し、「LLMで処理」ボタンをクリックすると、結果が表示されクリップボードにコピーされます。
   - **履歴の活用**: サイドバーから過去のクリップボード内容を選択して再利用できます。

## 📝 アップデート

### v1.0.0 (2023-10-01)

- 初回リリース。
- クリップボードの履歴管理機能を実装。
- LLMとの統合機能を追加。
- ウィンドウのリサイズとドラッグ機能をサポート。

## 🤝 コントリビューション

ClipMasterはオープンソースプロジェクトとして、皆様からのご協力をお待ちしております。バグの報告、機能の提案、プルリクエストなど、大歓迎です。詳細は[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

## 📄 ライセンス

ClipMasterはMITライセンスの下で公開されています。詳細については、[LICENSE](LICENSE)ファイルをご確認ください。

## 🙏 謝辞

ClipMasterの開発にあたり、OpenAIのGPT-4、およびlitellmプロジェクトに深く感謝いたします。これらの技術なしでは、本アプリケーションの実現は不可能でした。

ClipMasterをぜひお試しください。クリップボードの可能性を最大限に引き出し、生産性を向上させましょう！

