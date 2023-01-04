# calculate sum of priorities of all common letters
def calc_priority_sum(file):
    sum = 0
    for line in file:
        seq = line.rsplit("\n")[0]
        seq1 = seq[:int(len(seq)/2)]
        seq2 = seq[int(len(seq)/2):]
        sum += calc_priority_from_letter(get_common_letter_of_strings(seq1, seq2))
    return sum
    
    
# calculate priority of letter depending if it is lower or upper case
def calc_priority_from_letter(letter):
    if letter.isupper():
        return ord(letter) - 64 + 26
    else:
        return ord(letter) - 96


# determine common letter of strings
def get_common_letter_of_strings(str1, str2, str3 = ""):
    if str3 == "":
        for letter in str1:
            if letter in str2:
                return letter
    else:
        for letter in str1:
            if letter in str2 and letter in str3:
                return letter
    return ""


# group each three lines of string sequences 
def group_elves(file):
    groups = list()
    data = file.readlines()
    for i in range(0, len(data),3):
        group = list()
        for j in range (0,3):
            group.append(data[i+j])
        groups.append(group)
    return groups


# calculate sum of priorities of all common letters which appear in all three strings of one group
def calc_group_priority_sum(file):
    groups = group_elves(file)
    priority = 0
    for group in groups:
        priority += calc_priority_from_letter(get_common_letter_of_strings(group[0],group[1],group[2]))
    return priority


def main():
    file = open("task3.txt", "r")
    print(f'Priority sum star one: {calc_priority_sum(file)}')
    file = open("task3.txt", "r")
    print(f'Priority sum star two: {calc_group_priority_sum(file)}')


if __name__ == "__main__":
    main()