import glob, os
lattice = "Xsquare"
id = "99173"

rfile = "out/" + lattice + '/' + "slurm-" + id + ".out"
line = 0
Js_str = "hoge"

with open(rfile) as rf:
    for s_line in rf:
        line += 1
        if line % 52 == 1:
            Js_raw = [float(s) for s in s_line[5:-2].split(", ")]
            Js_str = '_'.join([str(int(J) if J.is_integer() else J) for J in Js_raw])
        if line % 4 == 3:
            with open("out/" + lattice + '/' + Js_str + '/' + Js_str + "_all.txt", mode='a') as wf:
                wf.write(s_line)