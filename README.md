# performance_test 実行環境雛形

## 概略

パフォーマンス計測ツール[locust](https://docs.locust.io/en/stable/index.html)を実行するテンプレートとなるプロジェクト

初期設定(`src/main.conf`)では GUI を用いて実行することは想定していない(`headless=true`)

## 要件

- python 3.9
- Docker
- Docker Compose 3.8

## 構成

```bash
├── Dockerfile              # コンテナ作成のためのDockerfile
├── Pipfile                 # Dockerコンテナでインストールされるモジュール定義
├── Pipfile.lock
├── docker-compose.yml      # master - worker 構成のための docker-compose
└── src
    ├── locustfile.py       # locust 実行時にデフォルトでされる.pyファイル
    └── main.conf           # locust の実行時の各種設定
```

### docker-compose 構成

`docker-compose` 内のボリュームで `src` 以下をバインドしている。

設定、コード等を変更する場合は、`src` 以下を編集する。

## 実行方法

### 設定変更

#### API のドメイン、実行時間/ユーザ数など

`src/main.conf` を変更する。

設定値の内容については以下参照

https://docs.locust.io/en/stable/configuration.html#configuration-file

#### API のエンドポイントやユースケースなど

`src/locustfile.py` を変更する。

コードについては以下参照

http://docs.locust.io/en/stable/writing-a-locustfile.html#writing-a-locustfile

### 実行コマンド

`docker-compose` 内の起動コマンドで `locust` を実行するようになっている。

そのため、`docker-compose` を起動するだけで計測がされる。

```bash
# 必要に応じて docker のビルドを実行
docker-compose build

# master - worker 構成で実行する場合
docker-compose up

# worker を複数使用する構成で実行する場合
# <数>を任意の数値に置き換える
docker-compose up --scale worker=<数>
```

### local 開発環境の作成

```bash
# pipenv にて local 開発環境を作成
pipenv install --dev

# 必要なモジュールがあれば追加
# pipenv install <追加モジュール>
```

#### GUI 実行

1. `src/main.conf` の `headless` 設定を削除(もしくは`false`に設定)
1. `docker-compose` を起動
1. `http://localhost:8089/` にアクセス
