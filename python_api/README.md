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

## speech to text
APIサーバーは`whisper-small`で動く．
```
python3 test_transcription.py --audio_path 001-sibutomo.mp3
```

### 参考
- https://docs.vllm.ai/en/latest/serving/multimodal_inputs.html#online-serving
- https://platform.openai.com/docs/api-reference/audio/createTranscription
- https://qiita.com/hyeonwoo_kim/items/27e1566ec8b4e93192d1