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
        global index
        Topo.__init__(self)
        switches = []
        hosts = []
        #Create nodes
        for i in lst:
            try:
                if 'S' in i[0]:
                    switches.index(i[0])
                elif 'H' in i[0]:
                    hosts.index(i[0])
            except:
                if 'S' in i[0]:
                    switches.append(self.addSwitch(i[0]))
                elif 'H' in i[0]:
                    hosts.append(self.addHost(i[0]))

            try:
                if 'S' in i[1]:
                    switches.index(i[1])
                elif 'H' in i[1]:
                    hosts.index(i[1])
            except:
                if 'S' in i[1]:
                    switches.append(self.addSwitch(i[1]))
                elif 'H' in i[1]:
                    hosts.append(self.addHost(i[1]))

        #Create links
        for i in lst:
            if 'S' in i[0]:
                if 'S' in i[1]:
                    self.addLink(switches[switches.index(i[0])], switches[switches.index(i[1])])
                else:
                    self.addLink(switches[switches.index(i[0])], hosts[hosts.index(i[1])])
            elif 'H' in i[0]:
                if 'S' in i[1]:
                    self.addLink(hosts[hosts.index(i[0])], switches[switches.index(i[1])])
                else:
                    self.addLink(hosts[hosts.index(i[0])], hosts[hosts.index(i[1])])


topos = {'simpletopo': (lambda: SimpleTopo())}

if __name__ == '__main__':
    lst=[("S0", "S1"), ("S1", "S2"), ("S2", "S0"), ("S3", "S0"), ("S3", "S1"), ("S4", "S0"), ("S4", "S1"), ("S5", "S1"), ("S5", "S2"), ("S6", "S1"), ("S6", "S2"), ("S7", "S2"), ("S7", "S0"), ("S8", "S2"), ("S8", "S0"), ("S9", "S3"), ("S9", "S4"), ("S10", "S3"), ("S10", "S4"), ("S11", "S5"), ("S11", "S6"), ("S12", "S5"), ("S12", "S6"), ("S13", "S7"), ("S13", "S8"), ("S14", "S7"), ("S14", "S8"), ("H1", "S9"), ("H2", "S10"), ("H3", "S11"), ("H4", "S12"), ("H5", "S13"), ("H6", "S14")]
    plotgr(lst)
    setLogLevel('info')
    topo=SimpleTopo(lst)
    net = Mininet(topo=topo, autoStaticArp=True)
    net.start()
    CLI(net)
    net.stop()