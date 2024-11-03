# LED-APP

個人的に LED マトリックスパネルで遊ぶ用のレポジトリです。

## 環境構築

### 使用ハードウェア

- Raspberry Pi 4B
  - 5 ではまだ動かないらしい
  - メモリの要件としては、画像のビルドにどれくらいメモリ使うか次第だと思う。どの機種でも依存関係のインストールはできると思う。
  - OS: Raspberry Pi OS (Raspbian) Lite 64bit
  - MicroSD カードは 1GB くらい空いてたら動くと思う。
- [HUB75 規格のパネル(P4, 1/16)](https://ja.aliexpress.com/item/1005004775953349.html)
  - アリエクで仕入れ。1 枚 800 円+送料 2000 円くらい。
  - 日本だと大体 1 週間で届きます。
- ジャンパケーブル 16~20 本くらい
  - [この要項](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md/)の通り配線
  - 市販の基盤で代用可能（というかその方がいい）
    - Adafruit の[2345 基板](https://www.marutsu.co.jp/pc/i/574341/)
    - [この基盤](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/adapter/passive-3)を自作しても良い
      - 基盤のファイルを JLCPCB に突っ込んだらできる
      - 部品は以下の部品を使用(1 枚あたり。大体 500 円/枚くらいで作れる。)
        | 品名 | 個数 |
        | -- | -- |
        | [【C0805C104K5RACTU】積層セラミックコンデンサ(MLCC) 100nF 50V dc 0805 (2012M)](https://www.marutsu.co.jp//pc/i/2570000/) | 4 |
        | [【RK73B2ATTD103J】チップ抵抗 10kΩ 5% 1/4W 0805](https://www.marutsu.co.jp//pc/i/856915/) | 1 |
        | [【21602X20GSE】40 ピン基板用ピンソケット[20 ピン ×2 列]](https://www.marutsu.co.jp//pc/i/19385/) | 1 |
        | [【EEUFC1J220】アルミニウム電解コンデンサ(22μF/63V)](https://www.marutsu.co.jp//pc/i/2572024/) | 1 |
        | [uxcell ピンヘッダ(8x2) 10 個入り](https://www.amazon.co.jp/dp/B0192RBXLQ) | 3 |

### 設定手順

> [!NOTE]
> この文書は Raspberry Pi Imager でヘッドレス運用するための情報が書き込まれた Raspberry Pi OS 使用を前提とします。  
> 事前に ssh 許可、ログイン作成、ネット接続などを済ませてください。

#### 依存関係のインストール

- Python 3.11 以前
  - 3.12 だと依存関係が合わないっぽい
  - [pyenv とかで入れればいいと思う](https://www.kkaneko.jp/tools/raspbian/rasppyenv.html)
- Git
  - ライブラリ落としてくるのに使う。
  - `sudo apt install git`
- python3-dev
  - ライブラリをビルドするのに使う
  - `sudo apt install python3-dev`
- cython3
  - ライブラリをビルドするのに使う
  - `sudo apt install cython3`

#### Python 用に RGB LED Matrix 制御ライブラリをインストール

`hzeller/rpi-rgb-led-martix`で作成できる Python 用ライブラリを使用する。

```bash
$ git clone https://github.com/hzeller/rpi-rgb-led-matrix.git ~/rpi-rgb-led-matrix
$ cd ~/rpi-rgb-led-matrix/bindings/python
$ make build-python
$ sudo make install-python
```

#### フォントとかをダウンロード

```bash
$ git clone https://github.com/mizphses/led-app.git
$ bash ./download-noto-jp.sh
```

#### Python 上の依存関係のインストール

```bash
$ pip install -r requirements.txt
```

## 参考

- [https://www.led-apps.com/](https://www.led-apps.com/)
  - 部品調達とかで参考にしました
- [https://github.com/hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix)
  - この repo がないと動かないです
