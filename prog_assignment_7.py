import logging
logging.basicConfig(filename='pr_as7.log',level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')

def sum_array(l):
    s=0
    logging.info('---inside sum_of_array---')
    try:
        for i in l:
            s=s+i
    except Exception as e:
        logging.error(e)
    else:
        logging.info('success')
    return s

print(sum_array([1,2,3,2,6,'ewd',43,4,23]))
print(sum_array([32,76,34,9,64]))

def largest(l):
    logging.info('---inside largest function---')
    big=None
    try:
        big=max(l)
    except Exception as e:
        logging.error(e)
    else:
        logging.info('successful')
    return big

print(largest([1,2,3,2,6,'ewd',43,4,23]))
print(largest([1,2,3,2,6,43,4,23]))


def array_rotation(l,n):
    shift=input('enter R (right) or L (left) :')
    if shift=='R' or shift=='r':
        while(n):
            j=l[-1]
            for i in range(len(l)-1,-1,-1):
                if i>0:
                    l[i]=l[i-1]
                else:
                    l[i]=j
            n=n-1
        return l
    if shift=='L' or shift=='l':
        while(n):
            j=l[0]
            for i in range(len(l)):
                if i<len(l)-1:
                    l[i]=l[i+1]
                else:
                    l[i]=j
            n=n-1
        return l

print(array_rotation([54,32,78,1,9,24],2))


def spl_ad_end(l):
    li=[]
    for i in range(1,len(l)):
        li.append(l[i])
    li.append(l[0])
    return li

print(spl_ad_end([23,13,45,67]))


def mono_check(l):
    o=l.copy()
    m=l.copy()
    o.sort()
    m=o.copy()
    m.reverse()
    if l==o or l==m:
        print('list is monotonic')
    else:
        print('non-monotonic')

mono_check([1,2,3,4,5,6,7])
mono_check([3,4,5,1,2,6,7])
mono_check([7,6,5,4,3,2,1])

