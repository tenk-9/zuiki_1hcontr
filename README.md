# zuiki_1hcontr
## はじめに
ZUIKI製の電車でGO!！専用コントローラをJR EAST Train Simulatorで使用するためのpythonスクリプトです．
詳細はQiitaに置いてあります．
- 1/2: https://qiita.com/10_tenk/items/973d78eff7bb3d9de3a2
- 2/2: https://qiita.com/10_tenk/items/f21203d7c55fd3b19d62
## ライセンス
MITライセンスに準拠しています．
## 使い方
python3の実行環境が整っていることを想定しています．
#### プログラム起動方法
1. コントローラをパソコンに接続します．
2. main.pyを実行します．
3. 接続されているコントローラが列挙されるので，`Nintendo Switch Pro Controller`の番号を入力します．
4. `Running...`が表示されたらプログラムが実行されているので，コントローラを動かすとゲーム内のマスコンが操作できます．
5. `control`+`c`でプログラムを終了します．
#### 操作方法
コントローラの操作をマウスホイールの回転及び押下に対応させています．

コントローラとゲーム内のハンドル位置にずれが生じた場合，コントローラのハンドル位置をNかEBにすると同期されます．

また，警笛やEBリセットなどの操作とコントローラのボタンは以下の表のとおりに対応しています．

記載のない操作は対応していません．
|操作|ボタン|
|:--:|:--:|
|警笛1|A|
|警笛2|X|
|EBリセット|Y|
|連絡ブザー|B|
|レバーサ前|↑|
|レバーサ後|↓|
|ATS確認|→|
|警報持続|←|
|定速/抑速|CAPTURE|
|勾配起動|L|
|TASK切|-|
## 対応車両
以下の車両で正常に動作することを確認しています．
- E233系0番台
- E233系3000番台
- 211系
## 上手く動かないとき
環境によって異なる可能性がある値は以下のものです．上の物から順に変更してみてください．
- `keymouse.py`内の`Mouse_scroll_delta`(整数)
  - コントローラのハンドル変化量 > ゲーム内の変化量のとき，値を少し減らす
  - コントローラのハンドル変化量 < ゲーム内の変化量のとき，値を少し増やす
- `keymouse.py`内の`EBscroll`(整数)
  - コントローラのハンドルをEB位置にしてもゲーム内でEBが投入されない(B8以下になる)場合，値を増やす
- `main.py`内の`notch_table_axes`内の各値
  - [Qiita記事のプログラム](https://qiita.com/10_tenk/items/973d78eff7bb3d9de3a2#%E3%83%9E%E3%82%B9%E3%82%B3%E3%83%B3%E4%BD%8D%E7%BD%AE%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B)を参考に，計測した値を設定してください．

以上の設定を変更しても正常に動作しない場合，[Twitter](https://twitter.com/10_tenk)にDMを飛ばしてください．可能であれば対応します．

その他ご意見・ご要望等あれば[Twitter](https://twitter.com/10_tenk)にDMを飛ばしてください．よろしくお願いします．
