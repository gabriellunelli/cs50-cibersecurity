# The example code of David to show how password can be strong or weak. The code will generate all possible combinations of 4 characters using letters, digits, and punctuation.

from string import digits, ascii_letters, punctuation

for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i, j, k, l)