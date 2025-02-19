import pygame
import random
import time

# 初期化
pygame.init()

# 画面設定
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("韓国語→漢字クイズ")

# フォントと色
FONT = pygame.font.Font(None, 48)
SMALL_FONT = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 問題データ
questions = [
    {"korean": "사랑", "correct": "愛", "options": ["愛", "友", "和", "心"]},
    {"korean": "평화", "correct": "平和", "options": ["平和", "協力", "勝利", "友情"]},
    {"korean": "마음", "correct": "心", "options": ["心", "体", "道", "天"]},
    {"korean": "친구", "correct": "友", "options": ["友", "家", "学", "親"]},
    {"korean": "희망", "correct": "希望", "options": ["希望", "勝利", "努力", "成功"]},
]

# 状態
score = 0
current_question_index = 0
feedback = ""
feedback_color = BLACK
time_limit = 10  # 問題ごとの制限時間 (秒)
start_time = time.time()

# メインループ
running = True
while running:
    screen.fill(WHITE)

    # ゲーム終了条件
    if current_question_index >= len(questions):
        end_text = FONT.render(f"ゲーム終了！スコア: {score}", True, BLACK)
        screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    # 現在の問題データ
    current_question = questions[current_question_index]

    # タイマー計算
    elapsed_time = time.time() - start_time
    remaining_time = max(0, time_limit - int(elapsed_time))

    # 時間切れ
    if remaining_time == 0:
        feedback = "時間切れ！"
        feedback_color = RED
        current_question_index += 1
        start_time = time.time()

    # 問題の韓国語を表示
    korean_text = FONT.render(f"韓国語: {current_question['korean']}", True, BLACK)
    screen.blit(korean_text, (50, 50))

    # 選択肢を表示
    options = current_question["options"]
    random.shuffle(options)  # ランダム化
    option_positions = []
    for i, option in enumerate(options):
        option_text = FONT.render(option, True, BLACK)
        x, y = (50, 150 + i * 70)
        screen.blit(option_text, (x, y))
        option_positions.append((x, y, option_text.get_width(), option_text.get_height()))

    # タイマー表示
    timer_text = SMALL_FONT.render(f"残り時間: {remaining_time}秒", True, BLACK)
    screen.blit(timer_text, (WIDTH - 250, 50))

    # フィードバック表示
    feedback_text = SMALL_FONT.render(feedback, True, feedback_color)
    screen.blit(feedback_text, (50, 500))

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i, (opt_x, opt_y, opt_w, opt_h) in enumerate(option_positions):
                if opt_x <= x <= opt_x + opt_w and opt_y <= y <= opt_y + opt_h:
                    if options[i] == current_question["correct"]:
                        feedback = "正解！"
                        feedback_color = GREEN
                        score += 1
                    else:
                        feedback = "不正解…"
                        feedback_color = RED
                    current_question_index += 1
                    start_time = time.time()  # タイマーをリセット
                    break

    # スコア表示
    score_text = SMALL_FONT.render(f"スコア: {score}", True, BLACK)
    screen.blit(score_text, (WIDTH - 250, 100))

    pygame.display.flip()

pygame.quit()
