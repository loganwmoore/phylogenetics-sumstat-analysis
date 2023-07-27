from ete3 import PhyloTree, TreeStyle
import os
import matplotlib.pyplot as plt
import numpy as np


#This function returns the root label according to the rules:
#A,A=A  B,B=B  A,B=?  A,?=A  B,?=B
def sumstat1(tree):
    tsum1 = tree.copy()
    for n in tsum1.traverse("postorder"):
        if len(n.children)!=0:
            numcountA=0
            numcountB=0
            numcountQ=0
            num_trav=0
            for leaf in n.iter_descendants(strategy='levelorder', is_leaf_fn=None):
                num_trav+=1
                if num_trav==3:
                    break
                if leaf.name==n1:
                    numcountA+=1
                if leaf.name==n2:
                    numcountB+=1
                if leaf.name=="?":
                    numcountQ+=1
                    
            if numcountA==0 and numcountB!=0:
                n.name=n2
            elif numcountA!=0 and numcountB==0:
                n.name=n1
            elif numcountA!=0 and numcountB!=0:
                n.name="?"
            elif numcountQ!=0 and numcountB!=0:
                n.name=n2
            elif numcountQ!=0 and numcountA!=0:
                n.name=n1
            elif numcountQ!=0 and (numcountA==0 and numcountB==0):
                n.name="?"
    return tsum1.name

#This function finds if a tree is MM, MP, or PP
#M=monphyletic   P=Polyphyletic
def sumstat2(tree):
    tsum2 = tree.copy()
    numa=0
    numb=0
    for n in tsum2.traverse("preorder"):
        if n.name==n1:
            numa+=1
        if n.name==n2:
            numb+=1
    anames = tsum2.search_nodes(name=n1)
    bnames = tsum2.search_nodes(name=n2)
    a_common_anc = tsum2.get_common_ancestor(anames)
    b_common_anc = tsum2.get_common_ancestor(bnames)
    aoutlier=0
    boutlier=0
    for ade in a_common_anc.iter_descendants():
        if ade.name==n2:
            aoutlier+=1
    for bde in b_common_anc.iter_descendants():
        if bde.name==n1:
            boutlier+=1
    if boutlier>0 and aoutlier>0:
        return "PP"
    if (boutlier==0 and aoutlier>0) or (boutlier>0 and aoutlier==0):
        if(boutlier>0):
            return ("MPDR")
        if(aoutlier>0):
            return ("MPRD")
    if boutlier==0 and aoutlier==0:
        return "MM"

#This function returns the minimum number of lineages that must have been
#transmitted when given the donor
def sumstat3(tree):
    tsum3=tree.copy()
    for n in tsum3.traverse("levelorder"):
        exepA=0
        exepB=0
        for chi in n.get_descendants():
            if chi.name==n1:
                exepA+=1
            elif chi.name==n2:
                exepB+=1
        if exepA==0 and exepB!=0:
            n.name=n2
            for chi in n.get_descendants():
                chi.detach()
        if exepB==0 and exepA!=0:
            n.name=n1
            for chi in n.get_descendants():
                chi.detach()
    lineage_transA=0
    lineage_transB=0
    for nd in tsum3.traverse("levelorder"):
        if nd.name==n2:
            lineage_transA+=1
    for nd2 in tsum3.traverse("levelorder"):
        if nd2.name==n1:
            lineage_transB+=1

    return (lineage_transA, lineage_transB)

#The following function finds the average distance between D and R nodes
def sumstat5(tree):
    numcount = 0
    nameA = tree.get_leaves_by_name(n1)
    total = 0
    name = tree.get_leaves_by_name(n2)
    for aname in nameA:
        for bname in name:
            numcount+=1
            total+= aname.get_distance(bname)
    return total/numcount

#This finds the average distance between D and other D nodes
def sumstat6(tree):
    
    numcount = 0
    nameA = tree.get_leaves_by_name(n1)
    total = 0
    for name in nameA:
        for aname in nameA:
            numcount+=1
            total+= name.get_distance(aname)
        numcount-=1
    return total/numcount

#This finds the average distance between R and other R nodes
def sumstat7(tree):
    numcount = 0
    nameB = tree.get_leaves_by_name(n2)
    total = 0
    for name in nameB:
        for bname in nameB:
            numcount+=1
            total+= name.get_distance(bname)
        numcount-=1
    return total/numcount

st = ['setA','setB','setC','setD','setE','setF','setG','setH','setI','setJ','setK','setL','setM','setN','setO','setP','setQ','setR','setS','setT','setU','setV','setW']

newicks = []
DRoot=[]
RRoot=[]
QRoot=[]
MMTotal=[]
MPDRTotal=[]
MPRDTotal=[]
PPTotal=[]
diff_list=[]
dd_rr_list=[]
dr_dd_list=[]
dr_rr_list=[]

for i in range(23):
    newicks = []
    fil = os.path.join('simulated_trees/',st[i])
    for filename in os.listdir(fil):
        if filename.endswith('.txt'):
            with open(os.path.join(fil, filename)) as f:
                nw = ((f.read()).split("D_1 ")[0])
                newicks.append(nw)
    #t = PhyloTree("INPUT NEWICK HERE")
    t1= PhyloTree(newicks[0])
    t2= PhyloTree(newicks[1])
    t3= PhyloTree(newicks[2])
    t4= PhyloTree(newicks[3])
    t5= PhyloTree(newicks[4])
    t6= PhyloTree(newicks[5])
    t7= PhyloTree(newicks[6])
    t8= PhyloTree(newicks[7])
    t9= PhyloTree(newicks[8])
    t10= PhyloTree(newicks[9])
    t11= PhyloTree(newicks[10])
    t12= PhyloTree(newicks[11])
    t13= PhyloTree(newicks[12])
    t14= PhyloTree(newicks[13])
    t15= PhyloTree(newicks[14])
    t16= PhyloTree(newicks[15])
    t17= PhyloTree(newicks[16])
    t18= PhyloTree(newicks[17])
    t19= PhyloTree(newicks[18])
    t20= PhyloTree(newicks[19])
    t21= PhyloTree(newicks[20])
    t22= PhyloTree(newicks[21])
    t23= PhyloTree(newicks[22])
    t24= PhyloTree(newicks[23])
    t25= PhyloTree(newicks[24])
    t26= PhyloTree(newicks[25])
    t27= PhyloTree(newicks[26])
    t28= PhyloTree(newicks[27])
    t29= PhyloTree(newicks[28])
    t30= PhyloTree(newicks[29])
    t31= PhyloTree(newicks[30])
    t32= PhyloTree(newicks[31])
    t33= PhyloTree(newicks[32])
    t34= PhyloTree(newicks[33])
    t35= PhyloTree(newicks[34])
    t36= PhyloTree(newicks[35])
    t37= PhyloTree(newicks[36])
    t38= PhyloTree(newicks[37])
    t39= PhyloTree(newicks[38])
    t40= PhyloTree(newicks[39])
    t41= PhyloTree(newicks[40])
    t42= PhyloTree(newicks[41])
    t43= PhyloTree(newicks[42])
    t44= PhyloTree(newicks[43])
    t45= PhyloTree(newicks[44])
    t46= PhyloTree(newicks[45])
    t47= PhyloTree(newicks[46])
    t48= PhyloTree(newicks[47])
    t49= PhyloTree(newicks[48])
    t50= PhyloTree(newicks[49])
    tree_list = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33,t34,t35,t36,t37,t38,t39,t40,t41,t42,t43,t44,t45,t46,t47,t48,t49,t50]

    n1 = "D"
    n2= "R"
    for t in tree_list:
        for node in t.get_leaves():
            node.name= (node.name).split("_")[0]
        for leaf in t.get_leaves():
            n1=leaf.name
            break
        for n in t.get_leaves():
            if(n.name!=n1 and n.name!=n2):
                n2=n.name
    total_sum1D=0
    total_sum1R=0
    total_sum1Q=0
    total_sum2MM=0
    total_sum2MPDR=0
    total_sum2MPRD=0
    total_sum2PP=0
    for tr in tree_list:
        if(sumstat1(tr)=="D"):
            total_sum1D+=1
        elif(sumstat1(tr)=="R"):
            total_sum1R+=1
        elif(sumstat1(tr)=="?"):
            total_sum1Q+=1
        if(sumstat2(tr)=="MM"):
            total_sum2MM+=1
        elif(sumstat2(tr)=="MPDR"):
            total_sum2MPDR+=1
        elif(sumstat2(tr)=="MPRD"):
            total_sum2MPRD+=1
        elif(sumstat2(tr)=="PP"):
            total_sum2PP+=1
    
    DRoot.append(total_sum1D)
    RRoot.append(total_sum1R)
    QRoot.append(total_sum1Q)
    MMTotal.append(total_sum2MM)
    MPDRTotal.append(total_sum2MPDR)
    MPRDTotal.append(total_sum2MPRD)
    PPTotal.append(total_sum2PP)
    dif = []
    ddrr_total_diff = []
    drdd_total_diff = []
    drrr_total_diff = []
    for tre in tree_list:
        sumdif = (sumstat3(tre)[0]-sumstat3(tre)[1])
        dif.append(sumdif)
        ddrrdif = (sumstat6(tre)-sumstat7(tre))
        ddrr_total_diff.append(ddrrdif)
        drdddif = (sumstat5(tre)-sumstat6(tre))
        drdd_total_diff.append(drdddif)
        drrrdif = (sumstat5(tre)-sumstat7(tre))
        drrr_total_diff.append(drrrdif)
    diff_list.append(dif)
    dd_rr_list.append(ddrr_total_diff)
    dr_dd_list.append(drdd_total_diff)
    dr_rr_list.append(drrr_total_diff)


if not os.path.isdir("sumstat_graphs"):
    os.makedirs("sumstat_graphs")
script_dir = os.path.dirname('sumstat_graphs/')

X = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']
X_axis=np.arange(len(X))
plt.bar(X_axis+0.2, DRoot, 0.4, label = 'D Root Label')
plt.bar(X_axis-0.2, RRoot, 0.4, label = 'R Root Label')
plt.bar(X_axis, QRoot, 0.4, label = '? Root Label')
plt.xticks(X_axis, X)
plt.xlabel("Set")
plt.ylabel("Trees")
plt.title("Sumstat 1")
plt.legend()
file_name = 'sumstat1graph'
results_dir = os.path.join(script_dir, 'sumstat12graphs/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)
plt.savefig(results_dir+file_name)
plt.clf()

plt.figure(figsize=(16, 9))
plt.bar(X_axis+0.15, MMTotal, 0.3, label = 'MM')
plt.bar(X_axis-0.15, MPDRTotal, 0.3, label = 'MPDR')
plt.bar(X_axis, MPRDTotal, 0.3, label = 'MPRD')
plt.bar(X_axis+0.3, PPTotal, 0.3, label = 'PP')
plt.xticks(X_axis, X)
plt.xlabel("Set")
plt.ylabel("Trees")
plt.title("Sumstat 2")
plt.legend()
file_name = 'sumstat2graph'
plt.savefig(results_dir+file_name)
plt.clf()
Tr = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50"]
st3range = [-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
Y_axis = np.arange(len(Tr))
X_axis = np.arange(len(st3range))
bins = np.arange(-11,8)-0.5
results_dir = os.path.join(script_dir, 'sumstat3_histograms/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)
filenames = ["st3AGraph","st3BGraph","st3CGraph","st3DGraph","st3EGraph","st3FGraph","st3GGraph","st3HGraph","st3IGraph","st3JGraph","st3KGraph","st3LGraph","st3MGraph","st3NGraph","st3OGraph","st3PGraph","st3QGraph","st3RGraph","st3SGraph","st3TGraph","st3UGraph","st3VGraph","st3WGraph"]
for i in range(23):
    file_name = filenames[i]
    plt.hist(diff_list[i], bins, range=[-11, 8], edgecolor = 'black', linewidth=1)
    plt.yticks(Y_axis, Tr)
    plt.xticks(range(-11, 8))
    plt.ylabel("Trees")
    plt.xlabel("Difference in Lineage if D is Donor vs if R is Donor")
    graph_title = ("Sumstat3",st[i])
    plt.title(graph_title)
    plt.savefig(results_dir+file_name)
    plt.clf()


bins = np.arange(-3,5)-0.5
results_dir = os.path.join(script_dir, 'dd-rrdistance/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)
filenames = ["dd-rrA","dd-rrB","dd-rrC","dd-rrD","dd-rrE","dd-rrF","dd-rrG","dd-rrH","dd-rrI","dd-rrJ","dd-rrK","dd-rrL","dd-rrM","dd-rrN","dd-rrO","dd-rrP","dd-rrQ","dd-rrR","dd-rrS","dd-rrT","dd-rrU","dd-rrV","dd-rrW"]
for i in range(23):
    file_name = filenames[i]
    plt.hist(dd_rr_list[i], bins, range=[-3,5], edgecolor = 'black', linewidth=1)
    plt.yticks(Y_axis, Tr)
    plt.xticks(range(-3, 5))
    plt.ylabel("Trees")
    plt.xlabel("Difference in Distance between D Nodes and R Nodes")
    graph_title = ("DD-RR Distance", st[i])
    plt.title(graph_title)
    plt.savefig(results_dir+file_name)
    plt.clf()

bins = np.arange(-3,5)-0.5
results_dir = os.path.join(script_dir, 'dr-dddistance/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)
filenames = ["dr-ddA","dr-ddB","dr-ddC","dr-ddD","dr-ddE","dr-ddF","dr-ddG","dr-ddH","dr-ddI","dr-ddJ","dr-ddK","dr-ddL","dr-ddM","dr-ddN","dr-ddO","dr-ddP","dr-ddQ","dr-ddR","dr-ddS","dr-ddT","dr-ddU","dr-ddV","dr-ddW"]
for i in range(23):
    file_name = filenames[i]
    plt.hist(dr_dd_list[i], bins, range=[-3,5], edgecolor = 'black', linewidth=1)
    plt.yticks(Y_axis, Tr)
    plt.xticks(range(-3, 5))
    plt.ylabel("Trees")
    plt.xlabel("Difference in Distance between D and R Nodes and D Nodes")
    graph_title = ("DR-DD Distance",st[i])
    plt.title(graph_title)
    plt.savefig(results_dir+file_name)
    plt.clf()

bins = np.arange(-3,5)-0.5
results_dir = os.path.join(script_dir, 'dr-rrdistance/')
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)
filenames = ["dr-rrA","dr-rrB","dr-rrC","dr-rrD","dr-rrE","dr-rrF","dr-rrG","dr-rrH","dr-rrI","dr-rrJ","dr-rrK","dr-rrL","dr-rrM","dr-rrN","dr-rrO","dr-rrP","dr-rrQ","dr-rrR","dr-rrS","dr-rrT","dr-rrU","dr-rrV","dr-rrW"]
for i in range(23):
    file_name = filenames[i]
    plt.hist(dr_rr_list[i], bins, range = [-3,5], edgecolor = 'black', linewidth=1)
    plt.yticks(Y_axis, Tr)
    plt.xticks(range(-3, 5))
    plt.ylabel("Trees")
    plt.xlabel("Difference in Distance between D and R Nodes and R Nodes")
    graph_title = ("DR-RR Distance", st[i])
    plt.title(graph_title)
    plt.savefig(results_dir+file_name)
    plt.clf()


