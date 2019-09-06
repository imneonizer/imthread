## imthread [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

```python
pip install imthread
```

This tiny little python module is useful for creating multiple threads of any function in seconds.

#### What's new in v0.2.1

After using this library for a number of times in various projects i found that if you pass in lots of data say ``1000`` data in a list, it was creating ``1000`` threads to do it all once, however in the practical world most of the times cpu's are not capable of creating so many threads at once or worse it eats up all resources at once. To prevent this problem now you can pass in ``max_threads`` value by default if you don't pass in the value it will automatically be set equal to 4 just for the safety purpose, and passing a `0` value will throw an error  while creating a ``imthread`` object this way it will only create specified number of threads at once and will wait untill the previously started threads has finished their job.

Other than that to keep a track on how many threads are been created in real time you can push in a new log method inn you processing function so that whenever a new thread is created you can see it. there ar two methods of tracking them.

- just to print out the thread number which is being created, use: `` imthread.console_log(output=True)``
- if you want to store it in some variable you can use: ``thread_number = imthread.console_log()``
- in case some error occurs, the thread will keep on running
- if you want to kill all the threads use ``imthread.stop()`` inside your processing function while handling errors.

#### Problem Statement

- Let say  for example, we have a ``list`` of numbers from `1 to 10` and all we wanted to do is `multiply every number by 1000` but the  challenge is ``it takes 5 sec`` for multiplying a single number by 1000 from the list, I know its an arbitary condition, but we can create it with ``time.sleep(5)`` function.
- Or you want to make a web request million times, without waiting for the server to respond you to make the next request.

#### Working

So what this module does is, at the time of object initialization it takes in the function which is used for processing data and max number of thread which can be created at once, when running in multi threads, and as input it takes a list of arguments for which multiple threads will be created.

------

#### Example 1

```python
import imthread
import time

st = time.time()
#the function for processing data
def my_func(data):
    print('>> Running Thread {}...'.format(data))
    data = data*1000
    time.sleep(5)
    return data

#building a imthreading object
multi_threading = imthread.multi_threading(my_func, max_threads=10)

#list of input data for processing
raw_data = [1,2,3,4,5,6,7,8,9,10]

#sending arguments for asynchronous multi thread processing
processed_data = multi_threading.start(raw_data)

#printing the synchronised received results
print()
print('>> Input: {}'.format(raw_data))
print('>> Result: {}'.format(processed_data))
print('>> Elapsed time: {} sec'.format(round((time.time()-st),2)))
```

#### output

```python
>> Running Thread 1...
>> Running Thread 2...
>> Running Thread 3...
>> Running Thread 4...
>> Running Thread 5...
>> Running Thread 6...
>> Running Thread 7...
>> Running Thread 8...
>> Running Thread 9...
>> Running Thread 10...

>> Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>> Result: [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
>> Elapsed time: 5.0 sec
```

Now you can clearly see, if we do it without multi threading it would have taken around ``50 Seconds`` for processing the data while doing the task one by one and waiting for ``5 Sec`` after running the function each time. but since we are doing it with multithreading it will take only ``5 Seconds``  for processing the same task with different data, in their individual threads.

#### Example 2

````python
import imthread
import time
import requests

st = time.time()
#the function for processing data
def my_func(data):
    imthread.console_log()
    data = requests.get("http://httpbin.org/get")
    return data

#building a imthreading object
multi_threading = imthread.multi_threading(my_func, max_threads=20)

#list of input data for processing
raw_data = []
for i in range(1,21):
    raw_data.append(i)

#sending arguments for asynchronous multi thread processing
processed_data = multi_threading.start(raw_data)

#printing the synchronised received results
print()
#print('>> Input: {}'.format(raw_data))
print('>> Result: {}'.format(processed_data))
print('>> Elapsed time: {} sec'.format(round((time.time()-st),2)))

````

#### output

````python
>> Creating Threads 1
>> Creating Threads 2
>> Creating Threads 3
>> Creating Threads 4
>> Creating Threads 5
>> Creating Threads 6
>> Creating Threads 7
>> Creating Threads 8
>> Creating Threads 9
>> Creating Threads 10
>> Creating Threads 11
>> Creating Threads 12
>> Creating Threads 13
>> Creating Threads 14
>> Creating Threads 15
>> Creating Threads 16
>> Creating Threads 17
>> Creating Threads 18
>> Creating Threads 19
>> Creating Threads 20

>> Result: [<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]
>> Elapsed time: 0.5 sec
````

In this example we didn't used time.sleep() instead we make a request to the webserver and it took ``0.5 seconds`` to get the result back so we did it 20 times with multi threading and were able to receive the results in less time in a synchronous order.

> Lets try to do it without multithreading and see how it affects the processing time.

So in this new update ``imthread v0.2.0``  we can specify that at once how many threads should be created so lets change the input parameter as ``max_threads = 2``  while creating the imthread object, this way it will only create one thread at a time and will wait until the previous thread has finished properly.

#### output

````python
.
.
.
>> Elapsed time: 9.64 sec
````

It is clear that every request to the server was taking approx. ``0.5 seconds`` so while making one request at a time it took ``9.4 seconds`` as expected.



#### Handling errors and killing all threads

So, by default if any error occurs the threads will keep on running, in case if you want to ignore some errors but if you want to kill all the thread at once you can use ``imthread.stop()`` while handling errors.

```python
#the function for processing data
def my_func(data):
    thread_number = imthread.console_log(output=True)
    try:
        data = requests.get("http://httpbin.org/get")
        return data
    except Exception as e:
        print(e) #printing other errors
        #killing all active threads
        imthread.stop() #use to kill all threads
```

if you don't use ``imthread.stop()`` function then the threads will keep on running and filling ``None`` inplace of returned data. if you used the ``imthread.stop()`` it will kill all active threads immediately and will return the data that were processed by your function so far.
