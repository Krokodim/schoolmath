# -*- coding: utf-8 -*-

import numpy as np

arg_counts = (2,3,4,5)
arg_range = np.hstack([np.arange(-70,-1), np.arange(2,50)])

bad_reps = [
    u'кто у мамы дурачок?',
    u'неправильно, попробуй еще',
    u'ну блин, внимательнее',
    u'вот балбес',
    u'садись, два',
    u'позор джунглям',
    u'глупышка'
]

good_reps = [
    u'отлично',
    u'в точку',
    u'умница, верно',
    u'молодец, правильно',
    u'о, круто, угадал',
    u'держи медаль',
    u'вау...точно'
]

def get_expr(args):
    res = ""
    for arg in args:
        arg_str = str(arg)
        if res !="":
            if arg < 0:
                if np.random.randint(-5,5) > 0:
                    arg_str = ' + (' + arg_str + ')'
                else:
                    arg_str = ' - ' + str(abs(arg))
            else:
                arg_str = ' + ' + arg_str
        res = res + arg_str
    return(res)

done = False
nexpr = 0
results = list()

while not done:
    nexpr += 1
    arg_count = np.random.choice(arg_counts,1, p=[.2,.5,.2,.1])
    args = np.random.choice(arg_range,arg_count)

    expr = get_expr(args)

    answered = False

    ntry = 0

    print u"-------------------------------------------------"
    print u"ЗАДАНИЕ №{0}:\n".format(nexpr)

    while not answered:
        ntry += 1
        answer = raw_input("{0} = ".format(expr))

        if answer == "q":
            file = open('results.txt', 'w')
            file.writelines(["%s  (%s attempts)\n" % result  for result in results])
            exit()


        try:
            answer = int(answer)
            answered = (answer == args.sum())
        except:
            pass

        if not answered:
            print '  ' + np.random.choice(bad_reps) + '...'
        else:
            print '  ' + np.random.choice(good_reps) + '!!!'
            results.append((expr, str(ntry)))
