import matplotlib.pyplot as plt
import numpy as np
import os, time, glob


def compute_mean_std(filename=None):
    my_file = open(os.path.join('uploads', filename))
    my_file_contents = my_file.read()
    print(my_file_contents, '\n')
    my_file.close()
    # simplify the name, laziness
    file = my_file_contents
    a = file.split('\n')
    print(a, '\n')

    # get the top part of file by looking for the hash
    for index, item in enumerate(a):
        if '#' in a[index]:
            headers = item[1:]
            # take this and use for something
            print(headers, '\n')
            # convert to float: float(something): or whatever

    # split the lines into single values
    myList = []
    for index, item in enumerate(a):
        if '#' in a[index]:
            pass
        else:
            myList.append(a[index].split())

        print(myList)

    # a nested for loop could be used
    newList = []
    for index, item in enumerate(myList):
        newList.append(float(myList[0][index]))
    t = newList
    print('t     : ', t)
    newList_y = []
    for index, item in enumerate(myList):
        newList_y.append(float(myList[1][index]))
    y = newList_y
    print('y     : ', y)
    newList_err = []
    for index, item in enumerate(myList):
        newList_err.append(float(myList[2][index]))
    err = newList_err
    print('error : ', err)
    # plt.plot(t, t, label="t plotted against t")
    plt.plot(t, y, label='y plotted against t')
    plt.plot(t, err, label='error plotted against t')
    plt.xlabel('t label')
    plt.ylabel('y label')
    plt.title("Exercise Two Graph")
    plt.legend()

    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
        # Use time since Jan 1, 1970 in filename in order make
        # a unique filename that the browser has not chached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile


