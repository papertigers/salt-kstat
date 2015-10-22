# salt-kstat
kstat module for saltstack


### Execution module functions:
#### `kstat.memory_cap(lx=False, digitOnly=False)`
`salt-call kstat.memory_cap`

```
# ./salt-call kstat.memory_cap --output json
[INFO    ] Executing command 'kstat -p -m memory_cap -c zone_memory_cap' in directory '/root'
{
    "local": {
        "execpgin": "4480",
        "n_pf_throttle_usec": "0",
        "anon_alloc_fail": "0",
        "pagedout": "0",
        "anonpgin": "0",
        "zonename": "2fc847b3-71bf-63c0-a300-94696208e311",
        "pgpgin": "46002",
        "nover": "0",
        "fspgin": "41522",
        "snaptime": "1672236.841528959",
        "swap": "690114560",
        "n_pf_throttle": "0",
        "swapcap": "2147483648",
        "physcap": "1073741824",
        "class": "zone_memory_cap",
        "crtime": "297.530764428",
        "rss": "550281216"
    }
}
```

#### `kstat.zone_zfs(lx=False, digitOnly=False)`
`salt-call kstat.zone_zfs`

```
# ./salt-call kstat.zone_zfs digitOnly=true --output json
[INFO    ] Executing command 'kstat -p -m zone_vfs -c zone_vfs' in directory '/root'
{
    "local": {
        "rtime": 124678894562,
        "nwritten": 2214408333,
        "1s_ops": 0,
        "delay_cnt": 333742,
        "wtime": 60587138454,
        "writes": 2432899,
        "wlentime": 61802862383,
        "rlentime": 164236155324,
        "snaptime": 1802471.837622232,
        "reads": 32886426,
        "nread": 222273156649,
        "delay_time": 19944140,
        "10s_ops": 0,
        "100ms_ops": 44,
        "10ms_ops": 1490,
        "crtime": 297.530752881
    }
}
```

### Example usage in a pillar
```
schedule:
    diskusage:
        function: kstat.zone_zfs
        seconds: 30
        kwargs:
            {% if grains['os'] != 'SmartOS' %}
            lx: True
            {% endif %}
            digitOnly: True
        returner: carbon
    memoryusage:
        function: kstat.memory_cap
        seconds: 30
        kwargs:
            {% if grains['os'] != 'SmartOS' %}
            lx: True
            {% endif %}
            digitOnly: True
        returner: carbon
```
