from string_mo import stringu as s

l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
     {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
exe = s(l)
exe.extract_list()
exe.dic_ele()
exe.tup_ele()
exe.num_data()
exe.sum_all_num()
exe.odd_fetch_list()
exe.extract_ineuron()
exe.ele_count()
exe.count_key()
exe.filter_str()
exe.alpha_num()
exe.multi_within_collection()
exe.flat_list()