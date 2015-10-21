import logging
log = logging.getLogger(__name__)

LX_KSTAT = '/native/usr/bin/kstat'
KSTAT = 'kstat'

def _process_kstat(kstat, cout, digitOnly):
    data = {}
    for line in cout.splitlines():
        key, value = line.split(":")[-1].split()
        if digitOnly:
            if value.isdigit():
                data[key] = value
        else:
            data[key] = value
    return data



def memory_cap(lx=False, digitOnly=False):
    if lx:
        cmd = [ LX_KSTAT, '-p -m memory_cap -c zone_memory_cap']
    else:
        cmd = [ KSTAT, '-p -m memory_cap -c zone_memory_cap']
    output = __salt__['cmd.run'](' '.join(cmd))
    return _process_kstat('memory_cap', output, digitOnly)


def zone_zfs(lx=False, digitOnly=False):
    if lx:
        cmd = [ LX_KSTAT, '-p -m zone_vfs -c zone_vfs']
    else:
        cmd = [ KSTAT, '-p -m zone_vfs -c zone_vfs']
    output = __salt__['cmd.run'](' '.join(cmd))
    return _process_kstat('memory_cap', output, digitOnly)
