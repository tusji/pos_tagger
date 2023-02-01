# pos_tagger
## 訓練資料
    將訓練資料以json格式儲存
    儲存方式如下
```json=
[
    {
        "WS" : [中文斷詞]
        "POS" : [中文詞性]
    },
    {
        "WS" : [中文斷詞]
        "POS" : [中文詞性]
    }
    .
    .
    .
]
```
## 單機訓練
    執行 transMatrix.py
## 叢集訓練
    分別讓電腦執行 HMMTrainMapper.py 以及 HMMTrainReducer.py
## Decode
    訓練結果會以pickel格式儲存
```json=
{
    [
        {‘p2p’:{(pos,pos):詞性轉詞性機率}},
        {‘p2w’:{(pos,world):字轉詞性機率}},
        {‘initw’:{(pos,world):初始字相對應詞性的機率}}
    ],
    .
    .
    .
}
```
    測試訓練結果需先安裝ckiptagger來做斷詞
    執行 HMM.py 並輸入中文句子
    程式會以ckiptagger斷詞結果做詞性標記
