def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


exit_or_not = ''
while exit_or_not != 'y':
    in_num = int(input("enter any even number ..."))
    for index in range(1, int(in_num/2)+1):
        if is_prime(index):
            sep = in_num - index
            if is_prime(sep):
                print("%d + %d = %d" % (index, sep, in_num))
    exit_or_not = input("exit? y/n")
    if exit_or_not == 'y':
        break
        
