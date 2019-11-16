from imthread.imthread import multi_threading, console_log
import time

__version__='1.1'
__author__='Nitin Rai'

st = 0
#default start function for spawning threads
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


result = {}
#decorator support function for quick launch
def run(*args, **kwargs):
    def inter(func, kwargs):
        global result
        data = kwargs['data'] if 'data' in kwargs else None
        repeat = kwargs['repeat'] if 'repeat'in kwargs else None
        assert data!=None or repeat!=None, "one or more arguments missing!"
        max_threads = kwargs['max_threads'] if 'max_threads' in kwargs else 10
        result[func.__name__] = start(func, data=data, repeat=repeat, max_threads=max_threads)

    return lambda func:inter(func, kwargs)

#decorator support function for setting up input function
def set(*args, **kwargs):
    def inter1(func, kwargs):
        def inter2(*args, **extra):
            max_threads =  kwargs['max_threads'] if 'max_threads' in kwargs else 10
            try:
                args = extra['repeat'] if len(args)==0 else args[0]
            except Exception as e:
                assert len(args)>0, func.__name__+' requires atleast one argument'
            res = start(func, data=args, max_threads=max_threads)
            return res
        return inter2
    return lambda func:inter1(func, kwargs)

def stop():
    raise Exception('stop')


def elapsed(output=False):
    tt = round((time.time()-st), 2)
    if output:
        print(f'>> Elapsed time: {tt} sec')
    return tt
