#Here is the example of LRC cache.

def least_recently_used(a, cache_size=3):
    b = []
    page_fault = 0
    page_hit = 0
    for i, j in enumerate(a):
        if len(b) < cache_size and j not in b:
            page_fault = page_fault + 1
            b.append(j)
        else:
            if j in b:
                page_hit = page_hit + 1
                b.remove(j)
                b.append(j)
            else:
                page_fault = page_fault + 1
                b.remove(b[0])
                b.append(j)

        print(b)
    print("page_fault {x}".format(x=page_fault))
    print("page_hit {x}".format(x=page_hit))
    return b


if __name__ == "__main__":
     x = [1,2,3,2,5,3,4,5,8,9]
     #x = [2,3,4,2,1,3,7,5,4,3]
     #x = [0,1,2,1,4,2,3,7]
     least_recently_used(x, 4)
