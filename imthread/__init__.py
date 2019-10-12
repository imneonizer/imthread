from imthread.imthread import multi_threading, console_log
import time

st = 0
def start(processing_func, data=None, repeat=None, max_threads=10):
    assert type(max_threads) == int, 'max_threads value should be an integer'
    assert max_threads>0, 'max_threads value cannot be less than 1'
    mt_local = multi_threading(processing_func, max_threads=max_threads)
    global st
    st = time.time()

    if data:
        processed_data = mt_local.start(data)
        return processed_data

    elif repeat:
        assert type(repeat) == int, 'repeat value should be an integer'
        assert repeat>0, 'repeat value cannot be less than 1'
        processed_data = mt_local.start(repeat)
        return processed_data
    else:
        print(f'data: {data}, repeat: {repeat}')

def stop():
    raise Exception('stop')

def elapsed(output=False):
    tt = round((time.time()-st), 2)
    if output:
        print(f'>> Elapsed time: {tt} sec')
    return tt
