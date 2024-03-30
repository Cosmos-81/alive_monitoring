import time
import requests
import tkinter as tk

# WebRequestを送信してjsonを取得する関数
def get_json(url):
    
    try:
        response = requests.get(url)
    except Exception as e:
        print('Error: WebRequest Failed')
        return False,'Error: WebRequest Failed'

    if response.status_code != 200:
        print('Error: ', response.status_code)
        return False,'Error: ' + str(response.status_code)
    else:
        return True,response.json()

# 設定ファイルを読み込む関数
def get_config():

    # 構成ファイルを読み込み
    import configparser

    raw_config = configparser.ConfigParser()
    raw_config.read('setting.ini')

    # 設定ファイルを変数に格納
    target_url = raw_config['TARGET']['URL']
    interval_sec = int(raw_config['WATCH']['INTERVAL'])

    config = {
        'url': target_url,
        'int_sec': interval_sec
    }
    
    return config

# ポップアップを表示する関数
def show_popup(title, message):
    root = tk.Tk()
    root.title(title)
    root.geometry('500x150')
    label = tk.Label(root, text=message)
    label.pack()
    root.mainloop()


if __name__ == '__main__':

    # ポップアップ処理部を工事中
    title = 'Error: WebRequest Failed'
    message = 'Error'

    show_popup(title, message)


    # 基本的な動作部を工事中
    # config = get_config()

    # while True:
        
    #     print('Start WebRequest')
    #     result, json_data = get_json(config['url'])

    #     # WebRequestが失敗した場合、ポップアップを表示して一時停止
    #     if not result:
    #         root = tk.Tk()
    #         root.title('Error')
    #         root.geometry('200x100')
    #         label = tk.Label(root, text=json_data)
    #         label.pack()
    #         root.mainloop()

    #     time.sleep(config['int_sec'])