# 使い方

## Node.jsのセットアップ
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install 20
nvm use 20
```

## ソースコードの実行
```
node index.mjs
```

### ソースコードの書き換え
以下の2箇所を書き換えてください：

- `baseURL`: `http://133.15.97.107:8000/v1`（現在使用している OpenAI API 互換サーバのURL）
- `model`: `Qwen2-VL-7B-Instruct`（現在使用しているモデル名）

```
import OpenAI from 'openai'

const openai = new OpenAI({
  baseURL: 'http://133.15.97.107:8000/v1', // 現在使用しているOpenAI API 互換サーバのURL
  apiKey: 'ollama', // 任意のダミーキー
})

async function main() {
  const completion = await openai.chat.completions.create({
    model: 'Qwen2-VL-7B-Instruct',　　　　//現在使用しているモデル名に書き換え
    messages: [{ role: 'user', content: 'こんにちは、調子はどう？' }],
  })

  console.log(completion.choices[0].message.content)
}

main()

```