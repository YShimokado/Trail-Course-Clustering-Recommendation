from selenium import webdriver
from time import sleep
import pandas as pd

url_login = "https://www.yamareco.com/user.php"
USER = "XXXXXX"
PASS = "XXXXXX"

#ダウンロードファイル保存先の指定
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "./gpx"}
chromeOptions.add_experimental_option("prefs",prefs)

#ドライバーを得る
browser = webdriver.Chrome(chrome_options=chromeOptions)
#browser = webdriver.Chrome()
#3秒待機
browser.implicitly_wait(3)
#URL読み込み
browser.get(url_login)
print("ログインページにアクセスしました")

#テキストボックスに文字を入力
e = browser.find_element_by_name("uname")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_name("pass")
e.clear()
e.send_keys(PASS)

#フォームを送信
frm = browser.find_element_by_css_selector("#centercolumn form")
frm.submit()
print("情報を入力してログインボタンを押しました")

#山行記録のURLを得る
a = browser.find_element_by_css_selector(".menu_record a")
url_records = a.get_attribute('href')
print("山行記録のURL=", url_records)

#山行記録を表示
browser.get(url_records)

#トレイルランを選択
run = browser.find_element_by_link_text("トレイルラン")
run.click()
print("トレイルランをクリックしました")

#「最近の記録」プルダウンから「2017年」を選択
btn = browser.find_element_by_xpath("//*[@id='pagelist']/div[1]/button")
btn.click()
btn = browser.find_element_by_xpath("//*[@id='pagelist']/div[1]/ul/li[6]/a")
btn.click()

#2ページ目以降を取得
link_list = []
m = [0,1,2,3,4,5,6,7,8]
for i in m:
	#次のページへ移動
	nextpage = browser.find_element_by_class_name("pager_arrow_next01")
	nextpage.click()
	print("次のページへ遷移しました")
	if(i < 2):
		continue
	#山行記録の詳細ページのリンクを取得
	links = browser.find_elements_by_css_selector("#reclist .title > a")
	for a in links:
		href = a.get_attribute('href')
		title = a.text
		link_list.append((href,title))
print("詳細ページ一覧を取得しました", len(link_list), "件")

#山行記録詳細ページ1つずつへアクセス
result = []
for href, title in link_list:
#	href = a.get_attribute('href')
#	title = a.text
	browser.get(href)
	print(title,"にアクセス")
	try:
		#マップ機能ボタンを押してプルダウンを開く
		mapbtn = browser.find_element_by_xpath("//*[@id='record_detail']/div[2]/div[2]/div[2]/div[2]/button")
		mapbtn.click()
		print("マップ機能をクリックしました")
		#GPXファイルのパスを取得
		ele = browser.find_element_by_xpath("//*[@id='record_detail']/div[2]/div[2]/div[2]/div[2]/ul/li[2]/a")
		#print(ele.text)
		gpxlink = ele.get_attribute('href')
		ele.click()
		print("地名入りのGPX linkを取得!",gpxlink)
		#result.append((title, gpxlink))
		sleep(3)
	except:
		print("NG:マップ機能ボタンがありませんでした")
		pass

browser.close()