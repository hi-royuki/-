open_file = open('point.txt') #open()関数でpoint.txt開く
data = open_file.read() #read()メソッドでデータを読み込む
open_file.close() #close()メソッドでファイル閉じる
point_data = data.splitlines() #splitlines()メソッドwp使用して行ごとのリストに変換する


point_dict = {} #空の辞書
for line in point_data: #１行ずつ処理する
    student_name, points_str = line.split(':') #コロンで分割
    point_dict[student_name] = points_str #辞書にデータを追加


score_dict = {} #空の辞書（合計点と平均点を保存しておくための辞書）
for student_name in point_dict: #点数データを繰り返し
    point_list = point_dict[student_name].split(',') #点数リストを作成
    subject_number = len(point_list) #点数を計算(len()関数＝リストに入っている値の個数や)
    total = 0

# 点数リスト(point_list)から教科数(subject_number)、合計点(total)と平均点(average)を算出する
    for point in point_list:
        total = total + int(point) #int()関数 = 整数に直す
    average = total / subject_number
    score_dict[student_name] = (total, average, subject_number) #計算したものを辞書(score_dict)にデータを保存


# 合計点を元に条件分岐で評価結果となる文字列を取得
evaluation_dict = {} #評価を保存するための空の辞書を作成
for student_name in score_dict:
    score_data = score_dict[student_name]
    total = score_data[0]
    average = score_data[1]
    subject_number = score_data[2]

    excellent = subject_number * 100 * 0.8
    good = subject_number * 100 * 0.65
    if total >= excellent:
        evaluation = 'Excellent!!!'
    elif total >= good:
        evaluation = 'Good!'
    else:
        evaluation = 'Bad'
    evaluation_dict[student_name] = evaluation #評価結果を辞書に追加

# 結果をファイルに出力する
# ↓ファイルを開く（書き込み可）
file_name = 'evaluation.txt'
output_file = open(file_name, 'w')
# ↑ここまで
for student_name in score_dict: # 合計点や平均点を記録した辞書(score_dict)に対して繰り返し処理を行う。
    score_data = score_dict[student_name]
    total = score_data[0]

    evaluation = evaluation_dict[student_name] # 評価(evaluation_dict)から取り出す

    text = f'[{student_name}] total:{total},evaluation:{evaluation}\n'
    output_file.write(text)
output_file.close()

print(f'評価結果を{file_name}に出力しました。')
