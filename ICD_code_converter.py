import re
import streamlit as st


def list_code_range(start, end, letter):
    code_range = []
    for i in range(start, end + 1):
        if i != end:
            i = str(i)
            code_range.append((letter + i))
        else:
            i = str(i)
            code_range.append((letter + i))
    return code_range


def clean_codes(codes):
    ranges = []
    codes = re.sub(r'(\d)\s+(\d)', r'\1\2', codes)
    codes = codes.replace(",", "")
    codes = codes.replace(".", "")
    codes = codes.replace("x", "")
    codes = codes.replace("Procedures:", "")
    codes = codes.replace("Procedure:", "")
    codes = codes.replace("Diagnosis:", "")
    clean_codes = codes.replace("X", "")
    output = ' '.join('"{}",'.format(word) for word in clean_codes.split(' '))

    for code in output.split():
        if '-' in code:
            temp_range = []
            if len(re.findall('[A-Za-z]', code)) > 0:
                output = output.replace(code, "")
                letter = re.findall('[A-Za-z]', code)[0]
                code = code.replace(letter, "")
                code = code.replace('"', "")
                code = code.replace("''", "")
                code = code.replace(",", "")
                firstLast = re.split(r'-', code)
                if firstLast[0][0] == '0':
                    leadingZero = True
                    num = int(firstLast[0])
                    num_length = str(num)
                    num_length = len(num_length)
                    print(num_length)
                    if firstLast[0][1] == '0':
                        leadingZero2 = True
                    else:
                        leadingZero2 = False
                else:
                    leadingZero = False
                    leadingZero2 = False
                start = int(firstLast[0])
                end = int(firstLast[1])
                temp_range = list_code_range(start, end, letter)
                for i in temp_range:
                    i_length = len(str(i)) - 1  # -1 to account for leading character (ie. A)
                    if leadingZero and leadingZero2:
                        if i_length == num_length:
                            ranges.append(str(i[0] + '0' + '0' + str(i[1:])))
                        elif i_length == num_length + 1:
                            ranges.append(str(i[0] + '0' + str(i[1:])))
                        else:
                            ranges.append(str(i))
                    elif leadingZero:
                        ranges.append(str(i[0] + '0' + str(i[1:])))
                    else:
                        ranges.append(i)
                leadingZero = False
                leadingZero2 = False
            else:
                # Ranges without a character
                output = output.replace(code, "")
                code = code.replace('"', "")
                code = code.replace("''", "")
                code = code.replace(",", "")
                firstLast = re.split(r'-', code)
                if firstLast[0][0] == '0':
                    leadingZero = True
                    num = int(firstLast[0])
                    num_length = str(num)
                    num_length = len(num_length)
                    print(num_length)
                    if firstLast[0][1] == '0':
                        leadingZero2 = True
                    else: leadingZero2 = False
                else:
                    leadingZero = False
                    leadingZero2 = False
                start = int(firstLast[0])
                end = int(firstLast[1])
                temp_range = list_code_range(start, end, "")
                for i in temp_range:
                    i_length = len(str(i))
                    if leadingZero and leadingZero2:
                        if i_length == num_length:
                            ranges.append('0' + '0' + str(i))
                        elif i_length == num_length + 1:
                            ranges.append('0' + str(i))
                        else:
                            ranges.append(str(i))
                    elif leadingZero:
                        ranges.append(str(i[0] + '0' + str(i[1:])))
                    else:
                        ranges.append(i)
                leadingZero = False
                leadingZero2 = False

    code_list = re.sub("[^\w]", " ", output).split()
    for i in ranges:
        i = i.replace('"', "")
        code_list.append(i)
    return code_list


def print_codes(clean_codes):
    to_print = ["("]
    for i in range(len(clean_codes)):
        if i % 10 != 0:
            to_print.append('"' + clean_codes[i] + '",')
        if i % 10 == 0:
            to_print.append("\n")
            to_print.append('"' + clean_codes[i] + '",')
        if i == len(clean_codes) - 1:
            to_print[-1] = to_print[-1].replace(",", "")
            codes = ' '.join([str(item) for item in to_print])
            close = "\n );"
            final_list = [codes, close]
            final_string = "".join(final_list)
    return final_string
