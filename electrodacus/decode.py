#!/usr/bin/env python3

import sys
import os
import socket

def decode_base91(s):
    return sum(91**z * (ord(c) - 35) for z, c in enumerate(reversed(s)))


def main(what, lines):
    for line in lines:
        if not line.startswith("var ") or not line.endswith('";\n'):
            continue
        key, val = line[4:-3].split('="')
        if "all" in what: print(key, val)
        if key == "sbms":
            if "all" in what: print("soc", decode_base91(val[6:8]))
            batt_volt = 0
            for i in range(8):
                cv = decode_base91(val[8 + 2*i:10 + 2*i])
                if "volt" in what: print("cell%d" % (i + 1), cv / 1000)
                batt_volt += cv

            if "all" in what: print("batt volt", batt_volt)
            batt_ma = decode_base91(val[29:32]) * (1 if val[28] == "+" else -1)
            pv_ma = decode_base91(val[32:35])
            if "amp" in what: print("batt", batt_ma / 1000)
            if "amp" in what: print("pv", pv_ma / 1000)
            if "amp" in what: print("load", (pv_ma - batt_ma) / 1000)
            if "all" in what: print("Status", decode_base91(val[56:59]))
            if "temp" in what: print("temp", decode_base91(val[24:26])/10-45)

        if key == "xsbms":
            if "all" in what: print("cvmin", decode_base91(val[5:7]))
            if "all" in what: print("cvmax", decode_base91(val[3:5]))
            if "all" in what: print("type", decode_base91(val[7:8]))
            if "all" in what: print("Cap", decode_base91(val[8:11]))
        if key == "eW":
            for i in range(8):
                if "all" in what: print("enW", i, decode_base91(val[6*i:6+6*i]))
        if key == "eA":
            for i in range(8):
                if "all" in what: print("enA", i, decode_base91(val[6*i:6+6*i]))


def web_main(what):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.4.1", 80))
    main(what, s.makefile())
    s.close()


def print_header(what):
    if "volt" in what:
        print("graph_title Solar voltages")
        print("graph_vlabel Volt")
        print("graph_category Solar")
        #print("graph_args -u 15 -l 11 --rigid")
        #print("bat.label Battery")
    elif "amp" in what:
        print("graph_title Solar currents")
        print("graph_vlabel Ampere")
        print("graph_category Solar")
        print("bat.label Battery")
        print("pv.label Panel")
        print("load.label Load")
    elif "temp" in what:
        print("graph_title Solar temperature")
        print("graph_vlabel Celcius")
        print("graph_category Solar")
        print("temp.label Attic")


if __name__ == '__main__':
    what = os.path.basename(sys.argv[-1])
    if what == "config":
        print_header(os.path.basename(sys.argv[0]))
        exit(0)
    if what.endswith(".py"):
        main("all", sys.stdin)
    else:
        web_main(what)
