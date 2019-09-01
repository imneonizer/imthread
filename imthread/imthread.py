import threading

t_index = 0
class multi_threading():
    def __init__(self, processing_func, max_threads=4):
        assert type(max_threads) == int, 'max_threads value should be a integer'
        assert max_threads >0, 'max_threads Cannot be less than 1'
        if max_threads < 4:
            print('Warning! max_threads < 4 is not advisable to use')
        self.process = processing_func
        self.max_threads = max_threads
        self.threads_ended = False

    def start(self, data):
        index_processed_data = {}
        def process_frames(data):
            global t_index
            #do some processing stuff============================
            self.threads_ended = False #informing new thread has started
            t_index = data[0]+1
            processed_data = self.process(data[1]) #actually processing the data
            #====================================================

            #adding processed data to a list=====================
            index_processed_data.update({data[0]:processed_data})
            #====================================================

            #only setting thread ended to True when the last of
            #maximum number of threads has finished
            if data[0]%self.max_threads == 0:
                self.threads_ended = True

        threads = []
        for i in range(0,len(data)):
            # creating threads=================================================
            index_data = data[i]
            args = (i,index_data)
            t = threading.Thread(target=process_frames, name='t', args=(args,))
            #==================================================================

            # starting threads=================================================
            threads.append(t)
            t.start()

            #checking if max number of threads has been created
            if i%self.max_threads == 0:
                #checking if threads has finished
                if not i == 0: #skipping first batch
                    while self.threads_ended == False:
                        pass
            #==================================================================

        #waiting for all the
        #threads to finish
        for t in threads:
            t.join()
        #=====================================

        #sorting in the order the data was received====
        index = sorted(index_processed_data.keys())
        sorted_data = []
        for i in range(0, len(index)):
            #print(processed_frames[i])
            sorted_data.append(index_processed_data[i])
        #==============================================

        return sorted_data

def console_log():
    global t_index
    print(f'>> Creating Threads {t_index}')
    return t_index

def thread_idx():
    global t_index
    return t_index
