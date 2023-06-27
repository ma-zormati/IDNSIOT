#!/usr/bin/python

from mininet.topo import Topo
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.log import setLogLevel
from graphplot import plotgr
from mininet.node import RemoteController

REMOTE_CONTROLLER_IP = "127.0.0.1"


class SimpleTopo(Topo):

    def __init__(self, lst):
        # Initialize topology
        Topo.__init__(self)
        switches = []
        hosts = []
        for i in lst:
            #Create node
            if 'H' in i[0]:
                hosts.append(self.addHost(i[0]))
            elif 'S' in i[0]:
                switches.append(self.addSwitch(i[0]))
            else:
                exit(0)
            #Create link
            if 'S' in i[1]:
                self.addLink(switches[switches.index(i[1])], switches[switches.index(i[0])])
            else:
                exit(0)


topos = {'simpletopo': (lambda: SimpleTopo())}

if __name__ == '__main__':
    lst=[("S0", "S1"), ("S1", "S2"), ("S2", "S0"), ("S3", "S0"), ("S3", "S1"), ("S4", "S0"), ("S4", "S1"), ("S5", "S1"), ("S5", "S2"), ("S6", "S1"), ("S6", "S2"), ("S7", "S2"), ("S7", "S0"), ("S8", "S2"), ("S8", "S0"), ("S9", "S3"), ("S9", "S4"), ("S10", "S3"), ("S10", "S4"), ("S11", "S5"), ("S11", "S6"), ("S12", "S5"), ("S12", "S6"), ("S13", "S7"), ("S13", "S8"), ("S14", "S7"), ("S14", "S8"), ("H1", "S9"), ("H2", "S10"), ("H3", "S11"), ("H4", "S12"), ("H5", "S13"), ("H6", "S14")]
    plotgr(lst)
    setLogLevel('info')
    topo=SimpleTopo(lst)
    net = Mininet(topo=topo)
    #net = Mininet(topo=topo, controller=None, autoStaticArp=True)
    # net.addController("c0", controller=RemoteController, ip=REMOTE_CONTROLLER_IP)
    net.start()
    CLI(net)
    net.stop()