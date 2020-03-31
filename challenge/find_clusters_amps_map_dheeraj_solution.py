from collections import defaultdict

def find_cluster_amps_map(vprocmanager_content):
    try:
        list_cproc_contnet = vprocmanager_content.splitlines()
        start_index = 0
        end_index = 0
        for line_no, line in enumerate(list_cproc_contnet):
            if 'AMP' in line and 'Cluster' in line:
                start_index = line_no
                break
        for line_no, line in enumerate(list_cproc_contnet[start_index:]):
            if '---------------------------------' in line:
                end_index = line_no
                break
        cluster_amp_map = defaultdict(list)
        for line in list_cproc_contnet[start_index+3:start_index+end_index]:
            split_line = list(map(int, line.split()))
            cluster_amp_map[split_line[1]].append(split_line[0])
        return cluster_amp_map
    except Exception as e:
        print('Unexpected exception occured '+str(e))
        raise Exception(e)


def main():
    with open('output.txt', 'r') as vprocmanager_output:
        vprocmanager_content = vprocmanager_output.read()

    cluster_amp_map = find_cluster_amps_map(vprocmanager_content)

    print  cluster_amp_map


main()
