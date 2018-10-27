def main():
    f = open('names.txt')
    print('---- Calling find_my_name ----')
    find_my_name(f)
    print('---- find_my_name finished ----')
    print('---- Calling appeared_first_in ----')
    print('Jessica first appeared in', appeared_first_in(f, ',Jessica,'))
    print('Kharmen first appeared in', appeared_first_in(f, ',Kharmen,'))
    print('Orchid first appeared in', appeared_first_in(f, ',Orchid,'))
    print('C3P0 first appeared in', appeared_first_in(f, ',C3P0,'))
    print('---- appeared_first_in finished ----')
    print('---- Calling get_summary_for_name ----')
    print(get_summary_for_name(f, 'Aragorn'))
    print(get_summary_for_name(f, 'Legolas'))
    print(get_summary_for_name(f, 'Leia'))
    print(get_summary_for_name(f, 'Kelly'))
    print('---- get_summary_for_name finished ----')


    f.close()


def find_my_name(f):
    name = 'Tricia'
    f.seek(0)
    for line in f:
        if name in line:
            print(line, end='')
        else:
            continue


def appeared_first_in(f, name):
    f.seek(0)
    found = False
    for line in f:
        position = line.find(name)
        if position > -1:
            return(line[0:4])
            found = True
            break
    #Loop through the file's lines.
    #If the name provided in the parameter is present in the line, return the year (first 4 characters of the line) to the caller.
    if not found:
        return -1

def get_summary_for_name(f, name):
    f.seek(0)
    first_year = 0 #the first year the name was observed
    count = 0 #the number of years the name appeared in the dataset
    total = 0 #the total number of occurrences of the name in the file
    for line in f:
        line_list = line.rstrip().split(',')
        if line_list[1] == name:
            if first_year == 0:
                first_year = int(line_list[0])
            count += 1
            total += int(line_list[3])
    return '{}: appears in {} years, first in {}, {:,} total babies'.format(
            name, count, first_year, total
        )

    

main()

