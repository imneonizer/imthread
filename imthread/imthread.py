import threading, time

t_index = 0
class multi_threading():
    def __init__(self, processing_func, max_threads=10):
        assert type(max_threads) == int, 'max_threads value should be an integer'
        assert max_threads >0, 'max_threads value cannot be less than 1'
        self.process = processing_func
        if max_threads == 1:
            self.max_threads = max_threads
        else:
            self.max_threads = max_threads -1
        self.threads_ended = False
        self.stop_execution = False

    def start(self, data):
        if type(data) == int:
            pseudo_infinity = data
        else:
            pseudo_infinity = len(data)

        index_processed_data = {}
        def process_frames(data):
            global t_index

            #do some processing stuff============================
            self.threads_ended = False #informing new thread has started
            t_index = data[0]+1

            #handling threads which are asked to stop but are still running
            if self.stop_execution:
                return None

            try:
                processed_data = self.process(data[1]) #actually processing the data

            except Exception as e:
                processed_data = None
                if str(e) == 'stop': #if manually stop exception raised
                    if not self.stop_execution:
                        self.stop_execution = True
                        print('Exception: Stop All Threads')
                else:
                    print(e)

            finally:
                #adding processed data to a list=====================
                index_processed_data.update({data[0]:processed_data})
                #====================================================

                #only setting thread ended to True when the last of
                #maximum number of threads has finished
                if data[0]%self.max_threads == 0:
                    self.threads_ended = True
            #====================================================

        threads = []
        for i in range(0, pseudo_infinity):
            # creating threads=================================================
            try:
                index_data = data[i]
            except Exception:
                index_data = i

            args = (i,index_data)
            t = threading.Thread(target=process_frames, name='t', args=(args,))
            #==================================================================

            # starting threads=================================================
            if self.stop_execution:
                break

            threads.append(t)
            t.daemon = True
            t.start()

            #checking if max number of threads has been created
            if i%self.max_threads == 0:
                #checking if threads has finished
                if not i == 0: #skipping first batch
                    while self.threads_ended == False:
                        if self.stop_execution:
                            break
                        pass
            #==================================================================

        #waiting for all the
        #threads to finish
        for t in threads:
            if self.stop_execution:
                break
            t.join()
        #=====================================

        #sorting in the order the data was received====
        index = sorted(index_processed_data.keys())
        sorted_data = []
        for i in range(0, len(index)):
            #print(processed_frames[i])
            try:
                sorted_data.append(index_processed_data[i])
            except Exception as e:
                print(e)
        #==============================================

        return sorted_data

def console_log(output=False):
    global t_index
    data = t_index
    if output:
        print(f'>> Creating Threads {data}')
    return data
