// index.mjs
import OpenAI from 'openai';

const openai = new OpenAI({
  baseURL: 'http://'+process.argv[2]+':'+process.argv[3]+'/v1', // 現在使用しているAPIサーバURLに変更
  apiKey: 'ollama', // ダミーでOK（OpenAI風に必須なだけ）
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: 'Qwen2-VL-2B-Instruct', // 現在使用している使用モデル名に変更
    messages: [{ role: 'user', content: 'こんにちは、調子はどう？' }],
  });

  console.log(completion.choices[0].message.content);
}

main();
