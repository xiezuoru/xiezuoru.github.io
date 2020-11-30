#读取传感器编号为1的json数据，并绘图
import sys, urllib.request, json
import pandas as pd
import matplotlib.pyplot as plt
url = 'http://127.0.0.1:8080/get?id=1'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
content = resp.read().decode('utf-8')
#content=open('new-json.txt').read()
if (content):
    #print(content)
    data = json.loads(content)
    #节点可以这样读出
    print(data['sensorid'])
    val=data["value"]
    #print(val[0])
    df=pd.DataFrame(val)
    #print(df)
    #绘图，默认是折线图
    ax=df.plot()
    #显示图形 
    plt.show()
