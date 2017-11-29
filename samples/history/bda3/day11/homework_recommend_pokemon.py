# recommend_pokemon_byname(pokemon_name):
#  1   100
# recommend_pokemon_byattr(hp,
#       attack,defense,spatk,spdef,speed)
# 推荐属性相似的3个pokemon
# 只考虑HP Attack  Defense Sp. Atk Sp. Def Speed

# 返回3个类似属性的pokemon

#1,2,5,56   3  4
import random
def _random_choose(lst, n=3):
    '''不重复的从一个容器中选择n个返回
    lst = [1,2,3,4,5,6,7,8]
    _random_choose(lst, n=3)
    返回 随机n个
    '''
    lst = lst.copy()
    chosed_elements = []
    while n: 
        element = random.choice(lst)#随机选一个
        lst.remove(element) # 原列表中移除此元素
        chosed_elements.append(element) #
        n -= 1
        #print(lst,chosed_elements)

    return chosed_elements

def recommend_pokemon_byname(pokemon_name):
    '''
     推荐属性相似的3个pokemon
     只考虑HP Attack  Defense Sp. Atk Sp. Def Speed
     返回3个类似属性的pokemon
    '''
    pass



print('文件名',__name__)
if __name__ == '__main__':
    print('文件名', __name__) # module
    lst = [1,2,3,4,5,6,7]
    #_random_choose(lst, 3)
    
    [print(_random_choose(lst, 3)) for n in range(10)]