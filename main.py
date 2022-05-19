def strip_comments(string, markers):
    lines = False
    if '\n' in string:
        lines = string.splitlines(True)

    string_to_return = ''
    if lines:
        line_counter = 1
        for line in lines:
            line = line.strip('\n')
            stripped_line = ""
            for marker in markers:
                if marker in line:
                    stripped_line = line.split(marker, 1)[0]
                    for marker in markers:
                        if marker in stripped_line:
                            stripped_line = line.split(marker, 1)[0]
                        stripped_line = stripped_line.replace(marker, '')
                    print("for line {} and marker {}, stripped line {}".format(line, marker, stripped_line))
                    line = stripped_line
            if stripped_line == "" and not any(marker in line for marker in markers):
                stripped_line = line
            stripped_line = stripped_line.rstrip()
            if line_counter < len(lines):
                stripped_line = stripped_line + "\n"
                line_counter = line_counter + 1
            string_to_return = string_to_return + stripped_line
    else:
        for marker in markers:
            string = string.split(marker, 1)[0]
            string_to_return = string

    return string_to_return

if __name__ == '__main__':
    #print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !#apples", ['#', "!"]))
    print(strip_comments("\tbananas avocados\nbananas ! oranges apples -\n^ @ pears cherries\n' -\n' = pears avocados", ['-', '=', '?', "'", '!']))
