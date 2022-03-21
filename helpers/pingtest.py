import speedtest

def test_ping():
    s = speedtest.Speedtest()
    print("Testing speed")
    ping = s.get_best_server().get('latency')
    print(f"ping is : {ping}ms")
    ping = str(ping) + "ms"
    return ping

