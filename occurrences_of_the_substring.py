def count_substring(string,sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

string = "ABCDCDC"
sub_string = "CDC"

print(count_substring(string,sub_string))