#import libraries and dictionaries 
import json 
import matplotlib.pyplot as plt
import pprint
#pprint.pprint(what are you are trying to access)

#open black mirror data
with open('data/blackmirror.json','r') as f:
    black_mirror = json.load(f)
#with open('data/bigbang.json','r') as g:
    #big_bang = json.load(g)

#access list of season and runtime 
show_info = black_mirror['_embedded']

season_list = []
runtime_list = []
for i in range(len(black_mirror)):
    print('\n')
    season_num= black_mirror['_embedded']['episodes'][i]['season']
    runtime_num= black_mirror['_embedded']['episodes'][i]['runtime']
    season_list.append(season_num)
    runtime_list.append(runtime_num)

season2_list  = [1]
runtime2_list = [0]

for i in range(len(black_mirror)):
    if season_list [i] == season2_list [-1]:
        runtime2_list [-1] += runtime_list [i]
    else:
        season2_list.append(season_list[i])
        runtime2_list.append(runtime_list[i])
print(season2_list)
print(runtime2_list)


values = ('Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5')
fig, ax = plt.subplots()
ax.set(
    xlabel = 'Season',
    ylabel = 'Total Runtime (In Minutes)',
)
plt.bar(season2_list,runtime2_list)

plt.show()

