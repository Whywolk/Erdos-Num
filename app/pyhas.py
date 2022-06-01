from subprocess import Popen, PIPE

def exec_haskell(db, scientist, res):
    proc = Popen(["stack", "ghci"], stdin=PIPE, stdout=PIPE)
    in_str = ':l ./course.hs' + '\n' + 'get_erdos_num ' + db + ' ' + scientist + '\n'
    out, err = proc.communicate(input=bytes(in_str, "UTF-8"), timeout=10)
    proc.kill()
    strs = str(out, 'UTF-8')
    strs = strs.split('Ok, one module loaded.\n')
    strs = strs[1].replace('ghci> Leaving GHCi.', '')
    res.append(strs)