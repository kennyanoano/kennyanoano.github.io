---
layout: default
title: "OpenAI APIを使った簡単なツール作成ガイド"
date: 2023-12-15
categories: AI
---

# AIはチャットだけじゃない！ツール化もカンタン！

chatGPTでチャットしてて、わあ！便利！これを一括処理で使えたらなあ～！と思ったときに、あんがい簡単にできるよ！という話。

GoogleのAPIもOpenAI(chatGPT)のAPIも同じようなかんじですが、Googleは(当面は)個人利用が無料、OpenAIは最初の5ドルが無料で以後有料。

---

#### 1. **事前準備**
まず以下の準備を済ませておきましょう。手順の詳細はかなり省略。

1. **APIキーを取得**  
   - OpenAIやGoogleのアカウントからAPIキーを発行する。  
   Google:https://aistudio.google.com/app/apikey
   OpenAI:https://platform.openai.com/api-keys

   - 取得したキーをパソコンの環境変数に登録しておきます(やり方はAIに教わる)。
   Google:GOOGLE_API_KEYという名前で取得したAPIキーを保存
   OpenAI:OpenAI_API_KEYという名前で取得したAPIキーを保存

2. **カーソル（Cursor）をインストール**  
   - わかる人はなんでもOK、初心者で何もわからない人はCursorをインストールして教えてもらいながらやる。

3. **Pythonをインストール**  
   - Pythonをパソコンにインストール
   - OpenAI/Googleが応答できるようにモジュールをインストール(やりかたはcursorに教わる)

---

#### 2. **OpenAIのAPIを使ってみる**

1. **プレイグラウンドで試す**  
   OpenAIの「Playground」というWebツールにアクセスします。
   https://platform.openai.com/playground
   
   ここで、  
   - **使いたいモデル**（例: gpt-4oなど）を選択  
   - **欲しい応答のスタイル**（会話形式、リスト形式など）を設定  
   実際にチャットを行ってみる。

2. **コードをコピーする**  
   「いい感じの応答だな」と思ったら、画面の「code」ボタンを押してPythonコードをコピーします。

3. **cursorで実行する**  
   コピーしたコードをカーソルに貼り付け、「test.py」などの名前で保存して、実行ボタン▶を押す！エラーが起きなければ成功

4. **返答をプリントしてみる**  
   取得したコードでは、AIの応答が結局何だったのか、結果が表示されないことが多いので、最後に「結果を表示する`print()`文を加える」必要があります。cursorに頼めばやってくれます。

5. **使いたいように改造する**  
    一括処理で使いたい場合などはcursorで改造。

---

#### 3. **Google APIも同じ手順で！**
OpenAIのAPIと同じ手順でGoogleのPlaygroundも利用できます。
https://aistudio.google.com/app/prompts/new_chat

codeは、Get codeボタンで取得できます。

---

#### 4. **応用例**
これを応用すれば、以下のようなことが簡単に実現できます：

- JSON形式で複雑なデータをAIから返してもらう  
- 必要な項目や値をAIに指定してレスポンスを調整  

---