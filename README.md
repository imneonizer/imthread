## imthread [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

```python
pip install imthread
```

This tiny little python module is useful for creating multiple threads of any function in seconds.

#### What's new in v1.0

A quick launch mode is added, just type ``imthread.start(func_name, repeat=10)`` and it will execute the given function given number of times in parallel. A standard way of measuring elapsed time is added as well. see examples below to understand how to use quick launch mode.

After using this library for a number of times in various projects i found that if you pass in lots of data say ``1000`` data in a list, it was creating ``1000`` threads to do it all once, how ever in the practical world most of the times cpu's are not capable of creating so many threads at once or worse it eats up all resources at once. To prevent this problem now you can pass in ``max_threads`` value by default if you don't pass in the value it will automatically be set equal to 4 just for the safety purpose, and passing a `0` value will throw an error  while creating a ``imthread`` object this way it will only create specified number of threads at once and will wait untill the previously started threads has finished their job.

Other than that to keep a track on how many threads are been created in real time you can push in a new log method inn you processing function so that whenever a new thread is created you can see it, there ar two methods of tracking them.

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

#the function for processing data
def my_func(data):
    print(f'>> Running Thread {imthread.console_log()}')
    data = data*1000
    time.sleep(5)
    return data

#list of input data for processing
raw_data = [1,2,3,4,5,6,7,8,9,10]

#sending arguments for asynchronous multi thread processing
processed_data = imthread.start(my_func, data=raw_data, max_threads=10)

#printing the synchronised received results
print()
print(f'>> Input: {raw_data}')
print(f'>> Result: {processed_data}')
print(f'>> Elapsed time: {imthread.elapsed()} sec')
```

#### output

```python
>> Running Thread 1
>> Running Thread 2
>> Running Thread 3
>> Running Thread 4
>> Running Thread 5
>> Running Thread 6
>> Running Thread 7
>> Running Thread 8
>> Running Thread 9
>> Running Thread 10

>> Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>> Result: [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
>> Elapsed time: 5.0 sec
```

Now you can clearly see, if we do it without multi threading it would have taken around ``50 Seconds`` for processing the data while doing the task one by one and waiting for ``5 Sec`` after running the function each time. but since we are doing it with multithreading it will take only ``5 Seconds``  for processing the same task with different data, in their individual threads.

#### Example 2

````python
import imthread
import requests

#the function for processing data
def my_func(data):
    imthread.console_log(output=True)
    data = requests.get("http://httpbin.org/get")
    return data

#sending arguments for asynchronous multi thread processing
processed_data = imthread.start(my_func, repeat=20, max_threads=20)

#printing the synchronised received results
print()
print(f'>> Result: {processed_data}')
imthread.elapsed(output=True)
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
>> Elapsed time: 0.55 sec
````

In this example we didn't used time.sleep() instead we make a request to the webserver and it took ``0.5 seconds`` to get the result back so we did it 20 times with multi threading and were able to receive the results in less time in a synchronous order.

> Lets try to do it without multithreading and see how it affects the processing time.

So in this new update ``imthread v1.0``  we can specify that at once how many threads should be created so lets change the input parameter as ``max_threads = 1``  this way it will only create one thread at a time and will wait until the previous thread has finished properly.

#### output

````python
.
.
.
>> Elapsed time: 6.43 sec
````

It is clear that every request to the server was taking approx. ``0.5 seconds`` so while making one request at a time it took ``6.43 seconds`` as expected.

### Example 3

Quick Launch mode, a new feature is added where you can directly use imthread to pass in the repetitive function, input data for those functions and how many threads you want it to create at a time. other than that if you just want it to repeat the function without any inputs you can do that too.

````python
import imthread
import time
import random

names = ['April', 'May']

#the function for processing data
def my_func(data):
    imthread.console_log(output=True)
    time.sleep(1)
    name = random.choice(names)
    return f'{name} says, Hello World!'

processed_data = imthread.start(my_func, repeat=4)

print(processed_data)
imthread.elapsed(output=True)
````

### output

````
>> Creating Threads 1
>> Creating Threads 2
>> Creating Threads 3
>> Creating Threads 4
['May says, Hello World!', 'April says, Hello World!', 'May says, Hello World!', 'April says, Hello World!']
>> Elapsed time: 1.0 sec
````

we kept a time gap of 1 sec inside the function still it repeated the task 4 times in same time. since it can access the global variables we can assign certain tasks that don't need different inputs every time.

#### Decorators support

Apart from calling the ``start()`` attribute we can also use decorators to explicitly make our functions for concurrent execution.

**Example 1**

````python
import imthread
import time

@imthread.run(repeat=5, max_threads=5)
def my_func(i):
    time.sleep(1)
    return i*2

print(imthread.result['my_func'])
````

**Output**

````python
[0, 2, 4, 6, 8]
````

This will execute the function as soon as you run your python code, in this case we are trying to perform the same task five times in a row concurrently. The final output of all the function can be accessed by ``imthread.result['function_name']``. Notice if you set your function on repeat it will always receive a parameter which is it's thread number.

----

**Example 2**

````python
import imthread
import time

@imthread.run(data=[1,2,3,4,5,6], max_threads=5)
def my_func(i):
    time.sleep(1)
    return i*2

print(imthread.result['my_func'])
````

**Output**

````python
[2, 4, 6, 8, 10, 12]
````

In this case we are directly passing our arguments in a list via decorator and receiving the result same way as we did in previous example.

----

**Exampe 3**

````python
import imthread
import time

@imthread.set(max_threads=10)
def my_func(i):
    time.sleep(1)
    return i*2

result = my_func(repeat=7)
print(result)
````

**Output**

````python
[0, 2, 4, 6, 8, 10, 12]
````

This is an another cool way to first convert your function in concurrent function and then passing the argument as how many time you want to execute that function all in parallel.

----

**Example 4**

````python
import imthread
import time

@imthread.set()
def my_func(i):
    time.sleep(1)
    return i*2

result = my_func([5,6,7])
print(result)
````

**Output**

````python
[10, 12, 14]
````

Again we can also specify what arguments we want to pass to the function to process it concurrently. if in the ``@imthread.set()`` decorator you won't pass any ``max_threads`` argument ``max_threads=10`` will be set.

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

if you don't use ``imthread.stop()`` function then the threads will keep on running and filling ``None`` in place of returned data. if you used the ``imthread.stop()`` it will kill all active threads immediately and will return the data that were processed by your function so far.
