import sys
import os
from dotenv import load_dotenv
load_dotenv()
from atproto import Client

def main():
    handle = os.environ.get("BSKY_HANDLE")
    password = os.environ.get("BSKY_PASSWORD")
    if handle is None or password is None:
        print("ハンドル名またはパスワードが設定されていません。")
        sys.exit(1)

    # Bskyクライアントの作成
    client = Client()
    # ログイン
    client.login(handle, password)
    # 投稿
    f = open("post.txt", "r")
    content = f.read()
    post = client.send_post(content)

if __name__ == '__main__':
    main()
