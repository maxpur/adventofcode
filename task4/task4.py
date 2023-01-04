# calculate number of fully overlapping sections in one file
def calculate_num_of_fully_overlapping_sections(file):
    no_of_fully_overlapping_sections = 0
    for line in file:
        sections = line.rsplit("\n")[0].split(",")
        if section_fully_overlaps_section(split_sections_to_list(sections[0]), split_sections_to_list(sections[1])):
            no_of_fully_overlapping_sections += 1
    return no_of_fully_overlapping_sections
        

# split section into list of section id
# for example '3-6' will be parsed to [3,4,5,6]
def split_sections_to_list(section):
    sections = section.rsplit("-")
    list_of_sections = list()
    for id in range(int(sections[0]), int(sections[1]) + 1):
        list_of_sections.append(id)
    return list_of_sections


# check if one section fully contains the other section
def section_fully_overlaps_section(sec1, sec2):
    return set(sec1).issubset(sec2) or set(sec2).issubset(sec1)


# check if one section overlaps another section
def section_overlaps_section(sec1, sec2):
    return set(sec1).intersection(set(sec2)) != set()


# calculate number of pairs of sections which overlaps 
def calculate_num_of_overlapping_sections(file):
    no_of_overlapping_sections = 0
    for line in file:
        sections = line.rsplit("\n")[0].split(",")
        if section_overlaps_section(split_sections_to_list(sections[0]), split_sections_to_list(sections[1])):
            no_of_overlapping_sections += 1
    return no_of_overlapping_sections


def main():
    file = open("task4.txt", "r")
    print(f'Number of fully overlapping pairs: {calculate_num_of_fully_overlapping_sections(file)}')
    file = open("task4.txt", "r")
    print(f'Number of overlapping pairs: {calculate_num_of_overlapping_sections(file)}')


if __name__ == "__main__":
    main()