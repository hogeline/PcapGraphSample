# PcapGraphSample
pythonのdpktで通信状況を解析し，graphvizを使いツリー構造で出力するサンプルプログラム

### 実行方法
dpktインストール

```
$ wget https://github.com/kbandla/dpkt/archive/v1.9.0.tar.gz
$ tar zxvf v1.9.0.tar.gz
$ cd v1.9.0
$ sudo python3 setup.py build
$ sudo python3 setup.py install
```
graphvizインストール

```
$ pip install graphviz
```
サンプルプログラム実行

```
python3 pcapGraph.py
```
実行結果

```
> 172.16.11.12 to 74.125.19.17 : 1147 [Byte]
> 74.125.19.17 to 172.16.11.12 : 905 [Byte]
> 172.16.11.12 to 216.34.181.45 : 5019 [Byte]
> 216.34.181.45 to 172.16.11.12 : 129471 [Byte]
> 172.16.11.12 to 172.16.11.1 : 4771 [Byte]
> 172.16.11.1 to 172.16.11.12 : 4259 [Byte]
> 172.16.11.12 to 96.17.211.172 : 9180 [Byte]
> 96.17.211.172 to 172.16.11.12 : 16192 [Byte]
```
このように実行されれば成功です．  
また，カレントディレクトリにflow_tree.pngが作られ以下のような画像が生成されます．

![flow_tree.png](https://github.com/hogeline/PcapGraphSample/blob/master/flow_tree.png)
