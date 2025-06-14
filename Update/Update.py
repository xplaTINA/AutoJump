import requests
import os

def download_github_zip(repo_url, output_path='New.zip'):
    # GitHubのZIPダウンロードURLを生成
    if repo_url.endswith('/'):
        repo_url = repo_url[:-1]
    zip_url = repo_url + '/archive/refs/heads/main.zip'

    # ダウンロード処理
    print(f"ダウンロード中: {zip_url}")
    response = requests.get(zip_url)

    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"保存完了: {output_path}")
    else:
        print(f"ダウンロード失敗: {response.status_code}")

# 例のGitHubリポジトリ
repo_url = 'https://github.com/xplaTINA/AutoJump'
download_github_zip(repo_url)
