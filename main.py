import sys
import os

from atproto import Client
from dotenv import load_dotenv

from util import generate_fibonacci_pattern

load_dotenv()


def main():
    handle = os.environ.get("BSKY_HANDLE")
    password = os.environ.get("BSKY_PASSWORD")
    if handle is None or password is None:
        print("ハンドル名またはパスワードが設定されていません。")
        sys.exit(1)

    result = generate_fibonacci_pattern(5)
    if result == "":
        print("パターン設定値を10未満にしてください。")
        sys.exit(1)

    # Bskyクライアントの作成
    client = Client()
    # ログイン
    client.login(handle, password)
    # 投稿
    client.send_post(result)


if __name__ == "__main__":
    main()
