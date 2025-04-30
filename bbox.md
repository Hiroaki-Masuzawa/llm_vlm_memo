# bounding box推定
## 概要
Qwen2-VLはgrounding(画像中の領域と言語の紐づけ)が行われており，それをうまく使うと直接bounding boxが推定できる．

## 例
```
./run_vllm_bash.sh
```
``` 
# 画像をダウンロードする
wget https://c.p02.c4a.im/images/item/18505268/86f4cbbb3be51b318ae1e7d71e562f07ecbc6e3dc068397fa496c8edc69bcee5?d=583x585 -O cans.jpg
# プログラムを実行する
python3 pred_bbox.py --object "red can" --image_path cans.jpg --output result.png
```

## 参考
- https://qiita.com/yufuin/items/f7b6ec67f60e1d2e69d8
    - Qwen2-VLのバウンディングボックスについて書いてある
- https://zenn.dev/robustonian/articles/qwen2_vl_mac
    - Qwen2-VLのコード全体が書いてある．
- https://www.creema.jp/item/18505268/detail
    - 缶の画像の出所