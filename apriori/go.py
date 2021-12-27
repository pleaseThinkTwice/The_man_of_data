# from efficient_apriori import apriori
# # # data=[[1,2,3],[2,3,4],[3,4,5],[1,2,3,5],[1,1,1]]
# # import pandas as pd
# # import numpy as np
# # from pandas import Series
# # all_data=pd.read_csv("final_all_data.csv")
# # del all_data['Unnamed: 0']
# # all_data.index=Series(np.arange(all_data.shape[0])).index
# # for i in all_data:
# #     print(i)
# if 0:
#     print(2)
# elif 0:
#     pass
# else:
#     print(0)
# # del all_data
# # data=[]
# # itemsets, rules = apriori(data, min_support=0.5,  min_confidence=0.8)
# # print('频繁项集：', itemsets)
# # print('关联规则：', rules)
# a={1:{'a':1,'b':2},2:{'b':2,'b':2},3:{'c':3,'b':2}}
# print(len(a))
# def itemsets_length(itemsets):
#     l = 0
#     for i in itemsets:
#         l += len(itemsets[i])
#     return l
# def rules_lenth(rules):
#     return len(rules)
# def final_result():
#     result=[]
#     for i in range(0,1,0.05):
#         for j in range(0,1,0.05):
#             itemsets, rules = apriori(go_2, min_support=i, min_confidence=j)
#             result.append([i,j,itemsets_length(itemsets),rules_lenth(rules)])
#     return result
#
# result=final_result()
# print(result)
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
data=read_csv("result4.csv")
# print(data)
xs=data["0"].to_list()
ys=data["1"].to_list()
zs=data["3"].to_list()
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(xs, ys, zs, s=zs, c=zs)
ax.set_xlabel('min_support')
ax.set_ylabel('min_confidence')
ax.set_zlabel('number_of_rules')

plt.show()


