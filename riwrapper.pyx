# cython: language_level=3, boundscheck=True
# distutils: language = c++


from libcpp.string cimport string
cdef extern from "ritest.h":
   int is_subiso(int query_N, int * query_adj, int * query_vertlabel,               
                 int ref_N, int * ref_adj, int * ref_vertlabel, float maxtime) except +

   # int old_match(string referencefile,
   #               string queryfile);

def test():
    print("hello world")
    return 12345



        # wasiso, mapping = cythontest.lemon_subiso_vf2(
        #     gsub_adj, gmain_colors, 
        #     gmain_adj, gmain_colors, 
        #     weighted_edges=True, max_run_sec=max_run_sec)

# def old_match_call(reference_filename,
#                    query_filename):
#     return old_match(reference_filename, query_filename)

cpdef c_is_subiso(int[:, :] g_sub_adj, int[:] g_sub_colors,
                  int[:, :] g_main_adj, int[:] g_main_colors, float maxtime):
    """
    Note that non-zero values in the adjacency matrices 
    are treated as labeled edges and the adj matrix 
    is assumed to be symmetric (A.T = A)

    """
              
    assert g_sub_adj.shape[0] == g_sub_adj.shape[1]
    assert len(g_sub_colors) == g_sub_adj.shape[0]
    
    assert g_main_adj.shape[0] == g_main_adj.shape[1]
    assert len(g_main_colors) == g_main_adj.shape[0]

    return is_subiso( g_sub_adj.shape[0],
                      &g_sub_adj[0, 0],
                      &g_sub_colors[0],
                      g_main_adj.shape[0],
                      &g_main_adj[0,0],
                      &g_main_colors[0], maxtime)

                     
    
