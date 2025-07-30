# 使い方
## 環境セットアップ
### dockerを使用しない方法
Node.jsをセットアップする
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install 20
nvm use 20
nvm install
```
### dockerを使用する方法
```
./run.sh
```
```
npm install
```

## ソースコード実行方法
```
node index.mjs xxx.xxx.xxx.xxx yyyy
```
- xxx.xxx.xxx.xxxはサーバURL
- yyyyはサーバポート番号
