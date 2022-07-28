import csv

def hellogui(d, s, o):

    a = 0

    with open(d) as f:
        for row in f:
            a = a + 1
        

    print('--------------------------')
    print('WebPerfCli Started')
    print('')
    print('')
    print('Developed by cosmicpb')
    print('github.com/cosmicpb')
    print('--------------------------')
    print('Data: ' + d)
    print('Strategy: ' + s)
    print('Output: ' + o)
    print('Number of tests: ' + str(a))
    print('The test has been Started')
    print('--------------------------')
    