"""Simple function based on multi(thread, process and async).

Function:
    compare_thread_process_async:
        compare thread, process and async with a
        simple IO bound(request)
Third party imports:
    aiohttp (pip install aiohttp)
"""

import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import requests

import aiohttp


def _get(url):
    return requests.get(url, timeout=5)


def compare_thread_process_async(links: list) -> None:
    """Get links and measure time of completion each request function.

    Args:
        links (list): urls as string to request.
    Returns:
        None
    Use to compare.
    """

    def _timing(func):
        def wrapper():
            start = time.time()
            func()
            print(
                f"{func.__name__} took {round(time.time() - start, 2)} seconds."
            )

        return wrapper

    @_timing
    def _simple_request():
        print(*[_get(url) for url in links], end=", ")

    @_timing
    def _using_thread():
        with ThreadPoolExecutor(max_workers=5) as excuter:
            print(*list(excuter.map(_get, links)), end=", ")

    @_timing
    def _using_process():
        with Pool(processes=5) as pool:
            print(*pool.map(_get, links), end=", ")

    @_timing
    def _using_async():
        async def fetch(session, url):
            async with session.get(url) as resp:
                return resp.status

        async def fetch_all(session, links):
            tasks = [asyncio.create_task(fetch(session, url)) for url in links]
            results = await asyncio.gather(*tasks)
            return results

        async def main():
            async with aiohttp.ClientSession() as session:
                responses = await fetch_all(session, links)
                print(*responses, end=", ")

        asyncio.run(main())

    _simple_request()
    time.sleep(5)
    # This 5 seconds sleep is to avoid getting blocked.
    _using_thread()
    time.sleep(5)
    _using_process()
    time.sleep(5)
    _using_async()


# Test
if __name__ == "__main__":
    compare_thread_process_async(
        [
            "https://www.google.com/",
            "https://www.digikala.com/",
            "https://www.python.org/",
            "https://divar.ir/",
            "https://jobinja.ir/",
        ]
    )

# Test Result
# <Response [200]> <Response [200]> <Response [200]> <Response [200]> <Response [200]>, _simple_request took 2.42 seconds.
# <Response [200]> <Response [200]> <Response [200]> <Response [200]> <Response [200]>, _using_thread took 0.6 seconds.

# I HAVEN'T FIGURED OUT WHY IS THE WARNING BELOW HAPPENING WITH MULTI_PROCESSING:
# ---------------------------------------------------------------------
# 0.02s - Debugger warning: It seems that frozen modules are being used, which may
# 0.00s - make the debugger miss breakpoints. Please pass -Xfrozen_modules=off
# 0.00s - to python to disable frozen modules.
# 0.00s - Note: Debugging will proceed. Set PYDEVD_DISABLE_FILE_VALIDATION=1 to disable this validation.
# ---------------------------------------------------------------------
# <Response [200]> <Response [200]> <Response [200]> <Response [200]> <Response [200]>, _using_process took 1.89 seconds.
# 200 200 200 200 200, _using_async took 0.59 seconds.
