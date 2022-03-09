<code class="language-git" lang="git">$ git checkout -b test</code>
open_file = open('point.txt') #open()関数でpoint.txt開く
data = open_file.read() #read()メソッドでデータを読み込む
open_file.close() #close()メソッドでファイル閉じる
point_data = data.splitlines() #splitlines()メソッドwp使用して行ごとのリストに変換する


point_dict = {} #空の辞書
for line in point_data: #１行ずつ処理する
    sutdent_name, points_str = line.splist(':') #コロンで分割
    point_dict[student_name] = points_str #辞書にデータを追加


score_dict = {} #空の辞書（合計点と平均点を保存しておくための辞書）
for student_name in point_dict: #点数データを繰り返し
    point_list = point_dict[student_name].splist(',') #点数リストを作成
    subject_number = len(point_list) #点数を計算(len()関数＝リストに入っている値の個数や)
    total = 0
