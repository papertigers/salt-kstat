import logging
log = logging.getLogger(__name__)

LX_KSTAT = '/native/usr/bin/kstat'
KSTAT = 'kstat'

def _kstat(cmd, lx=False):
    kstat = LX_KSTAT if lx else KSTAT
    cmd = [ kstat, cmd]
    return __salt__['cmd.run'](' '.join(cmd))

def _process_kstat(kstat, cout, digitOnly):
    data = {}
    for line in cout.splitlines():
        key, value = line.split(":")[-1].split()
        if digitOnly:
            v = value
            try:
                v = float(value)
                v = long(value)
            except:
                pass
            if isinstance(v, long) or isinstance(v, float):
                data[key] = v
        else:
            data[key] = value
    return data



def memory_cap(lx=False, digitOnly=False):
    output = _kstat('-p -m memory_cap -c zone_memory_cap', lx)
    return _process_kstat('memory_cap', output, digitOnly)


def zone_zfs(lx=False, digitOnly=False):
    output = _kstat('-p -m zone_vfs -c zone_vfs', lx)
    return _process_kstat('memory_cap', output, digitOnly)
