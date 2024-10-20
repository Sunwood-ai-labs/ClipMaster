import pyperclip
import os

def check_clipboard(last_clipboard):
    clipboard_content = pyperclip.paste()
    if clipboard_content != last_clipboard:
        return clipboard_content
    return None

def add_to_history(window, content):
    if content not in window.clipboard_history:
        window.clipboard_history.insert(0, content)
        window.history_list.insertItem(0, content)

def load_from_history(window, item):
    window.text_edit.setPlainText(item.text())

def clear_history(window):
    window.clipboard_history.clear()
    window.history_list.clear()

def copy_selected_item(window):
    selected_items = window.history_list.selectedItems()
    if selected_items:
        content = selected_items[0].text()
        pyperclip.copy(content)

def delete_selected_item(window):
    selected_items = window.history_list.selectedItems()
    if selected_items:
        item = selected_items[0]
        row = window.history_list.row(item)
        window.history_list.takeItem(row)
        del window.clipboard_history[row]

def export_history(window):
    with open("clipboard_history.txt", "w", encoding="utf-8") as f:
        for item in window.clipboard_history:
            f.write(item + "\n")

def import_history(window):
    if os.path.exists("clipboard_history.txt"):
        with open("clipboard_history.txt", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
            for line in lines:
                if line not in window.clipboard_history:
                    window.clipboard_history.append(line)
                    window.history_list.addItem(line)
