import numpy as np

import riwrapper
import time
import pickle


def test1():


    riwrapper.test()


    x = np.zeros((3, 3), np.int32)
    c = np.zeros(3, np.int32)

    x[0, 1] = 1
    x[1, 2] = 1
    x = x + x.T
    print(x)

    t1 = time.time()
    is_subiso = riwrapper.c_is_subiso(x, c, x, c)
    t2 = time.time()

    print("was it subiso?", is_subiso)


#print("old_match_call=", riwrapper.old_match_call("target.geu".encode(), "target.geu".encode()))


def test2():

    df = pickle.load(open("res_df.pickle", 'rb'))

    # only get the subiso ones
    #df = df[df.our_subiso >0]
    tgt_idx = 437

    tgt_row = df.iloc[tgt_idx]

    g_true_adj = (tgt_row.g_true_adj * 2).astype(np.int32)
    g_state_adj = (tgt_row.g_state_adj * 2).astype(np.int32)
    colors = tgt_row.colors.astype(np.int32)

    print("this took", tgt_row.runtime, "secs via the call-out")
    
    
    t1 = time.time()
    #is_subiso = riwrapper.c_is_subiso(g_state_adj, colors, g_true_adj, colors)
    is_subiso = riwrapper.c_is_subiso(g_state_adj, colors, g_true_adj, colors, 1)
    t2 = time.time()
    print("And this time it took", t2-t1)

    print("source subiso:", tgt_row.ri_subiso)
    
    print("did we think it subiso?", is_subiso)

    
    
def test3():

    df = pickle.load(open("res_df.pickle", 'rb'))

    # only get the subiso ones
    #df = df[df.our_subiso >0]
    tgt_idx = 1

    for tgt_row_i, tgt_row in  df.iterrows():
        

        g_true_adj = (tgt_row.g_true_adj * 2).astype(np.int32)
        g_state_adj = (tgt_row.g_state_adj * 2).astype(np.int32)
        colors = tgt_row.colors.astype(np.int32)

        #print("this took", tgt_row.runtime, "secs via the call-out")


        t1 = time.time()
        #is_subiso = riwrapper.c_is_subiso(g_state_adj, colors, g_true_adj, colors)
        timeout = False
        try:
            is_subiso = riwrapper.c_is_subiso(g_state_adj, colors, g_true_adj, colors, 1)
        except Exception as e:
            is_subiso = False
            timeout = True
        t2 = time.time()
        #print("And this time it took", t2-t1)

        #print("source subiso:", tgt_row.ri_subiso)

        #print("did we think it subiso?", is_subiso)
        if t2 - t1 > 0.01:
            print(f"{tgt_row_i:3d} {tgt_row.ri_subiso} {is_subiso} {timeout} this time: {t2-t1:3.4f}s other time: {tgt_row.our_runtime:3.4f}s")

test3()
