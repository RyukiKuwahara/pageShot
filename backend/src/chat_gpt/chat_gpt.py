import openai #OpenAIのAPIを利用するために必要

def get_prompt(option):
    prompt = ""
    if option == "summarize":
        prompt = "translate it to japanese in 100 words"
    elif option == "translate":
        prompt = "translate it to japanese"
    return prompt


def chatGPT(input_txt, option):
    openai.api_key = '#####自分のAPI keyを入力#####'
    prompt = get_prompt(option)
    res = openai.ChatCompletion.create( # resにAPIのレスポンスが格納される
        model="gpt-3.5-turbo", # ChatGPTのモデルを選択する 後述➀
        messages=[
            {
                "role": "system", # ChatGPTの設定・状況を指定
                "content": prompt # 日本語で返答するよう設定・状況づけ
            },
            {
                "role": "user", # roleをsystem, user, assistantの3種類から選択する 後述➁
                "content": input_txt # 聞きたい質問や行いたい指示を入力する
            },
        ],
    )
    # print(res) # レスポンス（res）を出力する
    # print(res['choices'][0]['message']['content']) # レスポンス（res）の中から返答のみを指定して出力する
    return res['choices'][0]['message']['content']

if __name__ == "__main__":
    input_txt = "The present volume consists of chapters by participants in \
    the Language and Space conference held in Tucson, Arizona, 16-19 March 1994. \
    In most cases the chapters have been written to reflect the numerous interactions at the conference, \
    and for that reason we hope the book is more than just a compilation of isolated papers. \
    The conference was truly interdisciplinary, including such domains as neurophysiology, \
    neuropsychology, psychology, anthropology, cognitive science, and linguistics. Neu- \
    ral mechanisms, developmental processes, and cultural factors were all grist for the \
    mill, as were semantics, syntax, and cognitive maps."
    print(chatGPT(input_txt, "summarize"))