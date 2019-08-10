## imthread [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

```python
pip install imthread
```

This tiny little python module is useful for creating multiple threads of any function in seconds.

#### Problem Statement

Let say  for example, we have a ``list`` of numbers from `1 to 10` and all we wanted to do is `multiply every number by 1000` but the  challenge is ``it takes 5 sec`` for multiplying a single number by 1000 from the list.

> I know its a arbitary condition, but we can create it with time.sleep(5) function.

#### Working

So what this module does is, at the time of object initialization it takes in the function which is used for processing data when running in multi threads, and as input it takes a list of arguments for which multiple threads will be created.

------

#### Example

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
multi_threading = imthread.multi_threading(my_func)

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

Now you can clearly see, if we do it without multi threading it would have taken around ``50 Seconds`` for processing the data while doing the task one by one and waiting for ``5 Sec`` after running the function each time.

But since we are doing it with multithreading it will take only ``5 Seconds``  for processing the same task with different data, in their individual threads.
