from PyQt6.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject
import litellm

class LLMWorkerSignals(QObject):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

class LLMWorker(QRunnable):
    def __init__(self, messages, model):
        super().__init__()
        self.messages = messages
        self.model = model
        self.signals = LLMWorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            response = litellm.completion(
                model=self.model,
                messages=self.messages
            )
            print("-------------------")
            print(response.choices[0].message.content)
            if response:
                llm_output = response.choices[0].message.content
                self.signals.finished.emit(llm_output)
            else:
                self.signals.error.emit("LLMからの応答がありません。")
        except Exception as e:
            self.signals.error.emit(str(e))
