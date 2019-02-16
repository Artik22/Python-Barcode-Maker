"""
upc.py
=====
Implement the following two functions as specified in the docstrings:

1. generate_bar_widths(s)
2. valid_barcode(s)

Some resources that may help with your implementation:

* https://en.wikipedia.org/wiki/Universal_Product_Code#Encoding
* http://electronics.howstuffworks.com/gadgets/high-tech-gadgets/upc3.htm
* http://www.adams1.com/upccode.html

"""
def generate_bar_widths(s):
    """Takes a barcode number as a string and translates it to a series
    of bar widths (a string that consists of 1's, 2's, 3's and 4's with
    each number corresponding to a width of a bar). For example, a
    series of bar widths starting with '1113 ... ' would consists of
    a black single width bar, a white single width bar, a black single
    width bar... and then a white triple width bar'.

    generate_bar_widths('043000181706')
    # --> '111>3211>1132>1411>3211>3211>3211>11111>2221>1213>2221>1312>3211>1114>111'
    # --> '111>3211>1132>1411>3211>3211>3211>11111>2221>1213>2221>1312>32111114111'
    # --> '3211>1132>1411>3211>3211>3211>2221>1213>2221>1312>3211>1114'

    :param s: the number to be translated to a series of bar widths
    :type s: str
    :return: a string representing the width of each bar, including the
    start, middle and end patterns (111, 11111, and 111)
    :rtype: str
    """
    # implement this function!

    newstr = s[3:27] + s[32:56]

    translation = ''

    for num in s:
        if num == '0':
            translation += '3211'
        elif num == '1':
            translation += '2221'
        elif num == '2':
            translation += '2122'
        elif num == '3':
            translation += '1411'
        elif num == '4':
            translation += '1132'
        elif num == '5':
            translation += '1231'
        elif num == '6':
            translation += '1114'
        elif num == '7':
            translation += '1312'
        elif num == '8':
            translation += '1213'
        elif num == '9':
            translation += '3112'
        else:
            print('Error: invalid character in the string; cannot create barcode.')

    final_translation = '111' + translation[0:24] + '11111' + translation[24:] + '111'
    return final_translation



def valid_barcode(s):
    """Determines whether a barcode is valid or not based on length and
    the check digit. A "UPC-A" barcode consists of 12 digits, with the
    last digit being the check digit. Some examples:

    valid_barcode('036000291452') # --> True
    valid_barcode('036000291450') # --> False
    valid_barcode('075678164125') # --> True
    valid_barcode('')            # --> False

    :param s: barcode number
    :type s: str
    :return: true if the barcode is valid, false otherwise
    :rtype: bool
    """
    # implement this function!

    sum_odd = 0
    sum_even = 0

    if len(s) != 12:
        return False
    else:

        for i in range(0, 12, 2):
            sum_odd += int(s[i])

            if i >= 10:
                sum_even += 0
            else:
                sum_even += int(s[i+1])

        mult_odd = sum_odd * 3
        add_and_modulo = (mult_odd + sum_even) % 10
        final_answer = 10 - add_and_modulo

    if len(s) == 12 and int(s[11]) == final_answer:
        return True
    else:
        return False



if __name__ == '__main__':
    print(generate_bar_widths('043000181706'))
    print(valid_barcode('036000291452'))