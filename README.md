# Trail Course Clustering and Recommendation
トレイルコースのGPXファイルデータを使って、クラスタリングとレコメンデーションを実施。
基本的にはPythonにてデータ収集〜前処理〜特徴量作成〜クラスタリング〜レコメンデーションを行った。
主成分分析のみRを利用。
詳細内容はPresentation.pdfに記載。

## 1.データ収集
ヤマレコ（yamareco.com）のWebサイトから、データをダウンロードさせていただきました。
手順：会員サイトログイン→山行記録ページへ遷移→一覧から1ファイルずつ右クリック選択にてダウンロードする

＜手法＞ Python + Selenium + ChromeDriver にてスクレイピング&ダウンロード
コード：download-gpx.py

## 2.前処理①データ抽出
GPXファイルから、必要な値を抽出し、DataFrameに格納する。
コード：Trail-Course-Clustering&Recommendation.ipynb

## 3.前処理②特徴量作成
抽出した緯度・経度・標高のデータから、距離、累積標高、勾配などを計算。
コード：Trail-Course-Clustering&Recommendation.ipynb

## 4.前処理③名寄せ
同一コースはレコメンド時に必要ないため、ここで省く。
スタート、ゴールの緯度経度、全長距離、最高地点の標高の差分が誤差の範囲内であれば同一と定義。
コード：Trail-Course-Clustering&Recommendation.ipynb

## 5.主成分分析 (R)
Rのprcomp関数を利用しPCAを実施。10の特徴量を2次元で表現。
コード：pca_graph.R

## 6.K-means法によるクラスタリング
PCAで次元圧縮した第1主成分、第2主成分を使い、クラスタリング。
クラスター数はElbow Methodで決定。
コード：Trail-Course-Clustering&Recommendation.ipynb

## 7.協調フィルタリングでレコメンデーション
コースIDを1つ渡すと、類似し、何らかの指標がレベルアップする想定のコースをレコメンドする関数を作成。
コード：Trail-Course-Clustering&Recommendation.ipynb


