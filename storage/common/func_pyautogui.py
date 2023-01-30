# PyAutoGuiをimport
import pyautogui

# 処理を実行するたびに0.3秒待機
# pyautogui.PAUSE = 0.3

class PythonAutoGuiTools:
# data
    win = "win"
    R = "r"

# methods
    def __init__(self):
        pass

    def __del__(self):
        pass

    # @brief ショートカットキーの使用
    # @param key1 1つ目のキー
    # @param key2 2つ目のキー
    def use_shortcut(self, key1, key2):
        pyautogui.keyDown(key1)
        pyautogui.keyDown(key2)
        pyautogui.keyUp(key1)
        pyautogui.keyUp(key2)

    def key_write(self, sentence):
        pyautogui.write(sentence)

    def key_press(self, key):
        pyautogui.press(key)

    # @brief 入力して実行
    # @param command 実行したいコマンド
    def exec_command(self, command):
        pyautogui.write(command)
        pyautogui.press("enter")

    # @brief コマンドプロンプト起動
    def launch_cmd(self):
        self.use_shortcut(self.win, self.R)
        pyautogui.write("cmd")
        pyautogui.press("enter")

