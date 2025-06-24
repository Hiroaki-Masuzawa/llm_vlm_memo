// index.mjs
import OpenAI from 'openai';

var server_ip = 'localhost'
var port = '8000'
var model_name = 'Qwen2-VL-2B-Instruct'

if (process.argv.length > 2) {
  server_ip = process.argv[2]
}
if (process.argv.length > 3) {
  port = process.argv[3]
}
if (process.argv.length > 4) {
  model_name = process.argv[4]
}

var request_url = `http://${server_ip}:${port}/v1`

const openai = new OpenAI({
  baseURL: request_url,
  apiKey: 'ollama', // ダミーでOK（OpenAI風に必須なだけ）
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: model_name,
    messages: [{ role: 'user', content: 'こんにちは、調子はどう？' }],
  });

  console.log(completion.choices[0].message.content);
}

main();
