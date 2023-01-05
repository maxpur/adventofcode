# check if character sequence corresponds to defined marker
def is_start_marker(sliding_window):
    return len(set(sliding_window)) == len(sliding_window)


# get sliding window data from data
def sliding_window(data, start_id, window_size):
    return data[start_id:start_id + window_size]


# get position of packet/message marker
def get_position_of_start_of_packet_marker(data, marker_len):
    for id in range(len(data) - marker_len):
        window_data = sliding_window(data, id, marker_len)
        if is_start_marker(sliding_window(data, id, marker_len)):
            return id + marker_len 
    return -1


def main():
    file = open("task6.txt", "r")
    print(f'Position of start marker star one: {get_position_of_start_of_packet_marker(file.readlines()[0], 4)}')
    file = open("task6.txt", "r")
    print(f'Position of start marker star two: {get_position_of_start_of_packet_marker(file.readlines()[0], 14)}')


if __name__ == "__main__":
    main()