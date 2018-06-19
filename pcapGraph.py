import dpkt # version 1.9.0
import socket
from graphviz import Digraph

# 解析したいpcapファイル
pcapfile = './test.pcap'
# ツリー構造Gを宣言
# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G = Digraph(format='png')
G.attr('node', shape='circle')

# pcapファイル読み込み
with open(pcapfile, "rb") as f:
    pcr = dpkt.pcap.Reader(f)
    frame_count = 0
    flow_list = {}
    for t, buf in pcr:
        frame_count += 1
        try:
            eth = dpkt.ethernet.Ethernet(buf)
        except:
            print("Fail parse FrameNo: ", frame_count, '...skipped')
            continue
        # 型がIPアドレスなら
        if type(eth.data) == dpkt.ip.IP:
            ip = eth.data
            # 送信元IPアドレス
            src = socket.inet_ntoa(ip.src)
            # 送信先IPアドレス
            dst = socket.inet_ntoa(ip.dst)
            flow_word = src + " to " + dst
            # 同じipアドレスがflow_listにあれば
            if  flow_word in flow_list:
                # パケットサイズを更新
                flow_list[flow_word] += len(str(buf))
            else:
                # グラフに辺を追加
                G.edge(src, dst)
                # パケットサイズの初期値を代入
                flow_list[flow_word] = len(str(buf))

    # 結果の表示
    for k,v in flow_list.items():
        print(k, ':', v, '[Byte]')

# 構築したツリー構造をflow_tree.pngで保存
G.render('flow_tree')
