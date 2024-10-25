import random

# 사용자로부터 5글자 이상 20글자 이하의 단어 3개 입력받기 위한 리스트 초기화
# ユーザーから5文字以上20文字以下の単語を3つ入力するためのリストを初期化
words_list = []
x = 0  # 입력 단어의 순서를 추적하는 변수 초기화
# 入力された単語の順序を追跡するための変数を初期化

# 올바른 단어 3개를 받을 때까지 반복
# 正しい単語を3つ受け取るまで繰り返し
while len(words_list) < 3:
    for i in range(3 - len(words_list)):  # 부족한 단어 개수만큼 반복
        # 不足している単語の数だけ繰り返す
        word = input(f"{x+1} 번째 단어를 입력 하세요: ")  # 사용자로부터 단어 입력 받기
        # ユーザーから単語を入力してもらう
        if 5 <= len(word) <= 20:  # 단어의 길이가 5자 이상 20자 이하인지 확인
            # 単語の長さが5文字以上20文字以下であるか確認
            words_list.append(word)  # 조건을 만족하면 리스트에 추가
            # 条件を満たせばリストに追加
            x += 1  # 올바른 단어를 입력한 경우 순서 증가
            # 正しい単語を入力した場合、順序を増加
        else:
            print("5이상 20이하 글자로 구성된 단어를 입력 하세요.")  # 조건을 만족하지 않으면 경고 메시지 출력
            # 5文字以上20文字以下の単語を入力してください。条件を満たさない場合、警告メッセージを表示

# 단어 목록에서 무작위로 단어 선택
# 単語リストから無作為に単語を選択
word_selected = list(words_list[random.randint(0, 2)])  # 리스트에서 무작위로 단어 하나 선택 후 리스트로 변환
# リストから無作為に単語を1つ選んでリストに変換
word_printed = word_selected[:]  # 선택된 단어를 복사하여 word_printed 변수에 저장
# 選ばれた単語をコピーしてword_printed変数に保存

print("단어 선택 완료 게임을 시작합니다.")  # 게임 시작 알림 메시지 출력
# 単語選択完了。ゲームを開始します。

# 선택된 단어의 글자 수
# 選ばれた単語の文字数
char_num_word = len(word_selected)  # 선택된 단어의 글자 수 계산
# 選ばれた単語の文字数を計算

# 글자 수의 절반을 블라인드 처리
# 文字数の半分をブラインド処理
blind_num_word = char_num_word // 2 + char_num_word % 2  # 블라인드 처리할 글자 수 계산 (홀수일 경우 반올림)
# ブラインド処理する文字数を計算（奇数の場合は切り上げ）

# 블라인드 처리할 인덱스 목록 생성
# ブラインド処理するインデックスリストを生成
list_blind_index = random.sample(range(char_num_word), blind_num_word)  # 단어의 인덱스 중 일부를 무작위로 선택하여 블라인드 처리할 인덱스 목록 생성
# 単語のインデックスの中から一部を無作為に選び、ブラインド処理するインデックスリストを生成
# .sample 란? 예) test = [1, 2, 3 . . . 10] 있을때 random.sample(test, a) 하면 리스트 안에서 무작위로 a 만큼 뽑아오고 저장.
# .sampleとは？例）test = [1, 2, 3 . . . 10] があるとき、random.sample(test, a) とするとリストの中から無作為にa個取り出して保存。
# 예) random.sample(test, 4) -> [1, 4, 6, 9]
# 例）random.sample(test, 4) -> [1, 4, 6, 9]

# 선택된 인덱스를 블라인드 처리
# 選ばれたインデックスをブラインド処理
for index in list_blind_index:
    word_printed[index] = "_"  # 선택된 인덱스의 글자를 "_"로 변경하여 블라인드 처리
    # 選ばれたインデックスの文字を"_"に変更してブラインド処理

print(f"블라인드 처리된 단어: {word_printed}")  # 블라인드 처리된 단어 출력
# ブラインド処理された単語を表示

# 단어 맞추기
# 単語を当てる
count = 1  # 시도 횟수를 추적하는 변수 초기화
# 試行回数を追跡する変数を初期化
while "_" in word_printed:  # 단어에'_'가 남아있는 동안 반복
    # 単語に'_'が残っている間繰り返す
    input_value = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개를 입력하세요.: ")  # 사용자로부터 한 글자 입력 받기
    # ユーザーから1文字を入力してもらう

    if len(input_value) != 1:  # 입력이 한 글자가 아닐 경우
        # 入力が1文字でない場合
        print("한 단어만 입력하세요.")  # 경고 메시지 출력
        # 1文字だけ入力してください。警告メッセージを表示
        continue  # 다음 시도로 넘어감
        # 次の試行に進む

    # 맞춘 글자를 단어에 표시
    # 当てた文字を単語に表示
    blind_index_length = len(list_blind_index)  # 블라인드 처리된 인덱스의 길이 저장
    # ブラインド処理されたインデックスの長さを保存
    list_blind_index = [index for index in list_blind_index if word_selected[index] != input_value]  # 맞춘 글자를 블라인드 인덱스 목록에서 제거
    # 当てた文字をブラインドインデックスリストから削除

    # 표시된 글자 업데이트
    # 表示された文字を更新
    for index in range(char_num_word):
        if word_selected[index] == input_value:  # 맞춘 글자가 단어에 있는 경우
            # 当てた文字が単語にある場合
            word_printed[index] = input_value  # 블라인드 처리된 부분을 입력한 글자로 변경
            # ブラインド処理された部分を入力された文字に変更

    # 맞춘 경우와 틀린 경우에 대한 피드백
    # 当てた場合と外れた場合のフィードバック
    if blind_index_length != len(list_blind_index):  # 맞춘 글자가 있을 경우
        # 当てた文字がある場合
        print(word_printed)  # 업데이트된 단어 출력
        # 更新された単語を表示
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")  # 틀린 글자일 경우 경고 메시지 출력
        # 単語に含まれていない文字です。警告メッセージを表示
    count += 1  # 시도 횟수 증가
    # 試行回数を増加

print(f"Clear - 선택된 단어: {word_printed}, 총 시도 횟수: {count-1}")  # 게임 종료 후 결과 출력
# クリア - 選ばれた単語: {word_printed}, 総試行回数: {count-1}