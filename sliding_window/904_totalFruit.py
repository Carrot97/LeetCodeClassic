"""
在一排树中，第 i 棵树产生tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：
把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，
然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。
你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
"""


def totalFruit(tree: list) -> int:
    voc = {}
    n = len(tree)
    start = type = ans = 0
    for end in range(n):
        if tree[end] not in voc:
            voc[tree[end]] = 1
            type += 1
        else:
            if voc[tree[end]] == 0:
                type += 1
            voc[tree[end]] += 1
        if type > 2:
            while True:
                voc[tree[start]] -= 1
                start += 1
                if voc[tree[start-1]] == 0:
                    type -= 1
                    break
        ans = max(ans, end - start + 1)
    return ans


print(totalFruit([1,2,1]))
