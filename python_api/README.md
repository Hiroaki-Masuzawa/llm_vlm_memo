# python api

## single image
### build 
```
./build.sh
```
### run
```
./run.sh
```

### pythonで実行
```
python3 test_vllm2.py --text "What is there in the photo?" --image_path image.png --server xxx.xxx.xxx.xxx --port yyyy
```

## movie
APIサーバーは`llava-onevision-qwen2`で動く．
```
python3 test_video.py
```
<!-- ## audio
```
python3 test_audio.py
``` -->

### 参考
- https://docs.vllm.ai/en/latest/serving/multimodal_inputs.html#online-serving