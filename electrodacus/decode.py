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
        if "all" in what: print(key, "length", len(val), val)

        val = val.replace('\\\\', '\\')

        if key == "sbms":
            assert len(val) == 59
            if "all" in what: print("soc", decode_base91(val[6:8]))
            batt_volt = 0
            for i in range(8):
                cv = decode_base91(val[8 + 2*i:10 + 2*i])
                if "volt" in what: print("cell%d.value" % (i + 1), cv / 1000)
                batt_volt += cv

            if "all" in what: print("batt volt", batt_volt)
            batt_ma = decode_base91(val[29:32]) * (1 if val[28] == "+" else -1)
            pv_ma = decode_base91(val[32:35])
            if "amp" in what: print("batt.value", batt_ma / 1000)
            if "amp" in what: print("pv.value", pv_ma / 1000)
            if "amp" in what: print("load.value", (pv_ma - batt_ma) / 1000)
            if "all" in what: print("Status", decode_base91(val[56:59]))
            if "temp" in what: print("temp.value", decode_base91(val[24:26])/10-45)
            if "temp" in what: print("batt.value", decode_base91(val[26:28])/10-45)
            soc = decode_base91(val[6:8])
            if "all" in what: print("SOC", soc)
        if key == "xsbms":
            assert len(val) == 11
            if "all" in what: print("cvmin", decode_base91(val[5:7]))
            if "all" in what: print("cvmax", decode_base91(val[3:5]))
            if "all" in what: print("type", decode_base91(val[7:8]))
            cap = decode_base91(val[8:11])
            if "all" in what: print("Cap", cap)
        if key == "eW":
            assert len(val) == 42
            for i in range(8):
                if "all" in what: print("enW", i, decode_base91(val[6*i:6+6*i]))
            unit = 360  # .1 Wh to Joule
            if "watt" in what: print("batt.value", unit * decode_base91(val[0:6]))
            if "watt" in what: print("pv.value", unit * decode_base91(val[6:12]))
            if "watt" in what: print("load.value", unit * decode_base91(val[30:36]))
        if key == "eA":
            assert len(val) == 42
            for i in range(8):
                if "all" in what: print("enA", i, decode_base91(val[6*i:6+6*i]))
            unit = 3.6  # mAh to Coulomb
            if "amp" in what: print("batt_coulomb.value", unit * decode_base91(val[0:6]))
            if "soc" in what: print("soc2.value", .001 * decode_base91(val[0:6]))
            if "amp" in what: print("pv_coulomb.value", unit * decode_base91(val[6:12]))
            if "amp" in what: print("load_coulomb.value", unit * decode_base91(val[30:36]))
    if "soc" in what:
        # 8000 mAh * 7p = 56 Ah capacity
        print("soc.value", cap * soc / 100 - cap + 56)

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
        for i in range(8):
            if i != 4:
                print("cell%d.label Cell %d" % (i+1, i+1))
    elif "amp" in what:
        print("graph_title Solar currents")
        print("graph_vlabel Ampere")
        print("graph_category Solar")
        print("batt.label Battery Instant")
        print("pv.label Panel Instant")
        print("load.label Load Instant")
        print("batt_coulomb.type DDERIVE")
        print("pv_coulomb.type DDERIVE")
        print("load_coulomb.type DDERIVE")
        print("batt_coulomb.label Battery Average")
        print("pv_coulomb.label Panel Average")
        print("load_coulomb.label Load Average")
        print("batt_coulomb.max 70000")
        print("pv_coulomb.max 70000")
        print("load_coulomb.max 70000")
    elif "temp" in what:
        print("graph_title Solar temperature")
        print("graph_vlabel Celcius")
        print("graph_category Solar")
        print("temp.label Attic")
        print("batt.label Battery")
    elif "soc" in what:
        print("graph_title Solar coloumb")
        print("graph_vlabel Ah")
        print("graph_category Solar")
        print("soc.label Battery State of Charge")
        print("soc2.label Battery Net Charge")
    elif "watt" in what:
        print("graph_title Solar energy")
        print("graph_vlabel W")
        print("graph_category Solar")
        print("batt.type DDERIVE")
        print("pv.type DDERIVE")
        print("load.type DDERIVE")
        print("batt.label Battery Average")
        print("pv.label Panel Average")
        print("load.label Load Average")
        print("batt.max 70000")
        print("pv.max 70000")
        print("load.max 70000")


if __name__ == '__main__':
    what = os.path.basename(sys.argv[-1])
    if what == "config":
        print_header(os.path.basename(sys.argv[0]))
        exit(0)
    if what.endswith(".py"):
        main("allvoltamptempsoc", sys.stdin)
    else:
        web_main(what)
