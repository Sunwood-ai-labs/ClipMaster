import streamlit as st
import os
import re

try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
    
    # 正規表現を使用して、先頭のYAMLフロントマターを削除
    readme_content = re.sub(r'^---\n.*?---\n', '', readme_content, flags=re.DOTALL)
    
    # 余分な空行を削除
    readme_content = re.sub(r'\n{3,}', '\n\n', readme_content)
    
    st.markdown(readme_content, unsafe_allow_html=True)
except FileNotFoundError:
    st.error("README.mdが見つかりませんでした。")
