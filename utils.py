import os
import subprocess

def mkdir(name):
    try: os.mkdir(name)
    except FileExistsError: pass

def execute(file_name, inp, code = 'position'):
    mkdir('results')
    mkdir("results/{}".format(file_name))
    f_in_n = inp
    f_out_n = 'results/{}/{}.txt'.format(file_name, file_name)
    f_in = open(f_in_n, 'r')
    f_out = open(f_out_n, 'w')
    command = ['./{}'.format(code)]
    subprocess.run(command, stdin = f_in, stdout = f_out)
    f_in.close()
    f_out.close()
