#This does not work in MicroPython. It works fine in regular Python.
asdf='jkl;'
match asdf:
    case 'jkl;':
        print('qwertyuiop')
    case 'dgfkjhsdfjh':
        print('dfhjssdfhkjsdfhk')