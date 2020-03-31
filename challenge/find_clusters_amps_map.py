def find_cluster_amps_map(vprocmanager_content):
    list_cproc_contnet = vprocmanager_content.splitlines()
    new_list_cproc_contnet=[]
    for i in range(len(list_cproc_contnet)):
        new_list_cproc_contnet.append(list_cproc_contnet[i].split())
    check = "Cluster"
    from_num=int(["{} {}".format(index1, index2) for index1, value1 in enumerate(new_list_cproc_contnet) for index2, value2 in
           enumerate(value1)
           if value2 == check][0].split()[0])
    print from_num

    untill=new_list_cproc_contnet.index(['------------------------------------------------------------------------------'])
    required_list=new_list_cproc_contnet[from_num+3:untill]
    return required_list

def get_AMP_list_slot_0_list(cluster_amp_map):
    amp_list=[]
    cluster_list=[]
    for i in range(len(cluster_amp_map)):
        amp_list.append(cluster_amp_map[i][0])
        cluster_list.append(cluster_amp_map[i][1])
    return amp_list,cluster_list

def final_step(amp_list,cluster_list):
    final_dict={}
    set_final_list2=sorted(map(int,list(set(cluster_list))))
    list_tuples=list(zip(map(int,cluster_list),map(int,amp_list)))
    for i in range(len(set_final_list2)):
        new_sublist=[]
        for j in range(len(list_tuples)):
            if list_tuples[j][0]==set_final_list2[i]:
                new_sublist.append(list_tuples[j][1])
        final_dict[set_final_list2[i]]=new_sublist

    return final_dict

def main():
    with open('output.txt', 'r') as vprocmanager_output:
        vprocmanager_content = vprocmanager_output.read()

    cluster_amp_map = find_cluster_amps_map(vprocmanager_content)
    amp_list,cluster_list=get_AMP_list_slot_0_list(cluster_amp_map)
    final_result=final_step(amp_list,cluster_list)

    print  final_result


main()
