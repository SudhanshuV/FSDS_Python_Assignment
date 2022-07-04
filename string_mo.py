import logging
logging.basicConfig(filename='string.log',level=logging.INFO,format= '%(levelname)s,%(asctime)s,%(name)s,%(message)s')

class stringu:
    logging.info('----inside user defined string class ----')
    def __init__(self,element):
        logging.info('---inside __init__ fuction---')
        self.element=element

    def extract_list(self):
        '''extract list from given list of element'''
        logging.info('---inside extract_list function---')
        l=list()
        try:
            for i in self.element:
                if type(i)==list:
                    l=l+i
            print(l)
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function is available')

    def dic_ele(self):
        '''fetches elements of dicts'''
        logging.info('---inside dict_ele function---')
        try:
            for i in self.element:
                if type(i)==dict:
                    for k,v in i.items():
                        print(k,v)
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function available')

    def tup_ele(self):
        '''extract tuple from given list of element'''
        logging.info('----inside tuple_ele function---')
        t=tuple()
        try:
            for i in self.element:
                if type(i)==tuple:
                    t=t+i
            print(t)
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function available')

    def num_data(self):
        '''extract all numeric data from'''
        logging.info('---inside num_data function---')
        l=list()
        try:
            for i in self.element:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==int:
                            l.append(j)
                else:
                    if type(i)==dict:
                        for k,v in i.items():
                            if type(k)==int or type(v)==int:
                                l.append(k)
                                l.append(v)
            print(l)
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function is available')

    def sum_all_num(self):
        '''sum of all numeric data from given list'''
        logging.info('---inside sum_all_data function---')
        l=list()
        try:
            for i in self.element:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==int:
                            l.append(j)
                else:
                    if type(i)==dict:
                        for k,v in i.items():
                            if type(k)==int or type(v)==int:
                                l.append(k)
                                l.append(v)
            print(sum(l))
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function is available')

    def odd_fetch_list(self):
        '''extract odd from given list of element'''
        logging.info('---inside odd_fetch_list function---')
        l=list()
        q=list()
        try:
            for i in self.element:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==int:
                            l.append(j)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int:
                            l.append(k)
                        if type(v)==int:
                            l.append(v)
                    for m in l:
                        if m%2==1:
                            q.append(m)
            print(q)
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function is available')

    def extract_ineuron(self):
        """extract ineuron from given data"""
        logging.info('inside extaract_ineuron function')
        l = list()
        try:
            for i in self.element:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str and j=='ineuron':
                            l.append(j)
                else:
                    if type(i) == dict:
                        for k, v in i.items():
                            if type(k) == str and k=='inueron':
                                l.append(k)
                            if type(v) == str and v=='ineuron':
                                l.append(v)
            print(l)
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function is available')

    def ele_count(self):
        '''count the occurance of every element in given data'''
        logging.info('inside ele_count')
        l=list()
        try:
            for i in self.element:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        l.append(j)
                elif type(i)==dict:
                    for k,v in i.items():
                        l.append(k)
                        l.append(v)
            for m in set(l):
                print('{} occured for {} times'.format(m,l.count(m)))
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function is available')

    def count_key(self):
        '''count the number of keys in dict'''
        logging.info('----inside count_keys----')
        l=list()
        count=0
        try:
            for i in self.element:
                if type(i)==dict:
                    for j in i:
                        count=count+1
            print(count)
        except Exception as e:
            logging.info(e)
        else:
            logging.info('function available')

    def filter_str(self):
        '''filter string element from given data'''
        logging.info('----inside filter_str---')
        l=list()
        try:
            for i in self.element:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==str:
                            l.append(j)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==str:
                            l.append(k)
                        if type(v)==str:
                            l.append(v)
            print(l)
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function is available')

    def alpha_num(self):
        '''filters alphanum character'''
        logging.info('----inside alpha_num----')
        l=list()
        try:
            for i in self.element:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==str and j.isalnum():
                            l.append(j)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==str and k.isalnum():
                            l.append(k)
                        if type(v)==str and v.isalnum():
                            l.append(v)
            print(l)
        except Exception as e:
            logging.exception(e)
        else:
            logging.info('function available')

    def multi_within_collection(self):
        '''multiplication of all numeric element within collection'''
        logging.info('----multi_within_collection----')
        try:
            for i in self.element:
                m=1
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j)==int or type(j)==float:
                            m=m*j
                    print(m)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k) == int or type(k) == float:
                            m = m * k
                        if type(v) == int or type(v) == float:
                            m = m * v
                    print(m)
        except Exception as e:
            logging.info(e)
        else:
            logging.info('function available')


    def flat_list(self):
        '''coverting to list'''
        logging.info('---inside flat|_list---')
        l=list()
        try:
            for i in self.element:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        l.append(j)
                elif type(i)==dict:
                    for k,v in i.items():
                        l.append(k)
                        l.append(v)
            print(l)
        except Exception as e:
            logging.info(e)
        else:
            logging.info('function available')
