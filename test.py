from tradingBot.connectors.binance_futures import BinanceFuturesClient
client = BinanceFuturesClient("hoUL9VOrAORK2GN5sDejUl7j6hOTBcXAZaIr0f1njCLPs4TZPHS6KCTL6PQZbpi9",
                              "5JSm571NyCDeCaURZQOz0C7dT5JPFg6eB7sKnHFMzsGcZhCTq07JVyYxhfnR8t22",
                              True)
import time
import win32api
gt = client.get_server_time()
tt=time.gmtime(int((gt["serverTime"])/1000))
win32api.SetSystemTime(tt[0],tt[1],0,tt[2],tt[3],tt[4],tt[5],0)