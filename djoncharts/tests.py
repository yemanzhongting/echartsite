# -*- coding: utf-8 -*-
import jieba,json
def ststistic(txt):
    words = jieba.lcut_for_search(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    #
    # print(counts.items())
    items = list(counts.items())

    items.sort(key=lambda x: x[1], reverse=True)
    # items.sort(reverse = True)
    # for i in range(20):
    #     word, count = items[i]
    #     print(word, count)
    # jsonArr = json.dumps(items, ensure_ascii=False)
    # print(jsonArr)
    # print(items)
    # print(type(items))

    all_list=[]
    for i in range(len(items)):
        all_item = {}
        word, count = items[i]
        if '全文' not in word:
            all_item['name']=word
            all_item['value'] = count
            all_list.append(all_item)

    print(all_list)
    return all_list[0:50]

# names=[]
# values=[]
# for i in all_list:
#     names.append(i['name'])
#     values.append(i['value'])
# import pandas as pd
# df=pd.DataFrame(
#     {'name':names,
#     'value':values}
# )
# a=df.to_json(orient='records')
# print(a)

