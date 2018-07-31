# coding:utf-8
# created by ada_magicjay at 2018.07.26 

'''
数据输入要求
Input:
csv格式的文件
    1.用户对电影的rating数据路径: rating_path 
        数据格式： 
            user_id,item_id,rating,timestamp
            1,1,1,1162160236000
            1,2,4.5,1162160624000
    2.电影的对应分类标签数据路径： movie_tags_path
        数据格式：
            item_id,tagID1,tagID2
            1,1,12
            2,3,5
    3.标签数据路径： tags_path
        数据格式：
            id,value
            1,earth
            2,police

数据输出
Output:
function1:  return counts
    输出数据类型：
        <class 'pandas.core.series.Series'>
    输出数据格式：
        1    6
        9    1
        5    1
        3    1
        2    1
        Name: tagID1, dtype: int64
function2: return top_dict
    输出数据类型：
        <class 'dict'>
    输出数据格式：
        {1: [1, 12], 2: [1, 2], 3: [1, 12], 4: [1, 12], 5: [1, 5]}
'''

'''
所用库： numpy pandas  collections.Counter
'''
import numpy as np 
import pandas as pd 

rating_path = './test_ml_ratings.csv'
movie_tags_path = './test_movie_tags.csv'
tags_path = './test_tags.csv'


# function1 统计每部电影被观看了多少次
def count_data_1():
    # header = ['user_id', 'item_id', 'rating', 'timestamp']
    # df = pd.read_csv(rating_path, sep = '\t', names = header)

    # users = df.user_id.unique()
    # items = df.item_id.unique()

    # n_users = users.shape[0]
    # n_items = items.shape[0]

    # print("Nums of users:\t%d\tNums of items:\t%d"%(n_users,n_items))


    # counts = df[u'item_id'].value_counts()
    # print("\n")
    # print(counts)
    df_rating = pd.read_csv(rating_path)

    counts = df_rating['item_id'].value_counts()
    # print(counts)
    return counts

# function2 统计每个用户观看的top2的电影类型
def count_data_2():
    df_rating = pd.read_csv(rating_path)

    df_tag = pd.read_csv(tags_path)

    df_movietag = pd.read_csv(movie_tags_path)

    # 根据两张表的共同的列名，两表的列名必须相同，参数"item_id"
    df_merge = df_rating.merge(df_movietag, on = "item_id")

    df_sorted = df_merge.sort_values(by=['user_id','item_id'])

    # 将每个用户每次观看的类型都放到dict里
    count_dict = {}
    user_set = set()

    for index,row in df_sorted.iterrows():
        # print(type(int(row['user_id'])))
        # print(int(row['user_id']),int(row['tagID1']),int(row['tagID2']))
        if int(row['user_id']) not in user_set:
            user_set.add(int(row['user_id']))
            count_dict[int(row['user_id'])]=[]
        count_dict[int(row['user_id'])].append(int(row['tagID1']))
        count_dict[int(row['user_id'])].append(int(row['tagID2']))

    # 遍历dict将出现次数top2的类型使用Counter统计 最后放入top_dict
    from collections import Counter
    top_dict = {}
    for key in count_dict:
        # print(Counter(count_dict[key]))
        obj=Counter(count_dict[key])
        # print(obj.most_common(2))
        top_list=obj.most_common(2)
        tmp_list=[]
        for top_tuple in top_list:
            x,y=top_tuple
            tmp_list.append(x)
        top_dict[key]=tmp_list

    # print(top_dict)
    return top_dict

# function1 统计每部电影被观看了多少次
count_data_1()

# function2 统计每个用户观看的top2的电影类型
count_data_2()