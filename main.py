from dataclasses import dataclass, replace
from helper import *

SYSLOG = '/data/syslog'
HTML = './html/active-tunnels.html'
# SYSLOG = 'host.syslog.log'
# HTML = 'tunnels.html'

if __name__ == '__main__':

    tunnels = {}
    with open(SYSLOG, 'r') as f:
        for line in f:
            if all([w in line for w in ['started tunnel', 'ngrok.io']]):
                tunnel_desc = line.strip().split(': ')[1]
                tn = Tunnel()
                for kv in tunnel_desc.split():
                    if '=' in kv:
                        k, v = kv.split('=')
                        tn = replace(tn, **{k: v})

                tunnels.update({tn.name: tn})

    with open(HTML, 'w') as f:
        f.writelines(tunnel_toHTML(tunnels))

    # for tn_name, tn in tunnels.items():
    #     print(f'Tunnel info {tn_name}: since {tn.t}, {tn.url} => {tn.addr}')
