import threading
import judger
import time
class Result:
	def __init__(self):
		self.stat = []
		self.tot = 0
		self.lock = threading.Lock()
	def add(self, x, score):
		self.lock.acquire()
		x[0] *= score
		self.tot += x[0]
		self.stat.append(x[1])
		self.lock.release()
	def get(self):
		return self.tot, self.stat

class JobQueue(threading.Thread):
	def __init__(self):
		super(JobQueue, self).__init__()
		self.joblist = []
	def add(self, job):
		self.joblist.append(job)
	def run(self):
		#print('start run')
		for job in self.joblist:
			job.run()

class Job:
	def __init__(self, code, ins, outs, res, score, _id):
		self.code = code
		self.ins = ins
		self.outs = outs
		self.res = res
		self.score = score
		self.id = _id
	def run(self):
		#print('run job', self.id, 'code = ', self.code)
		x, info = judger.judge(self.code, self.ins, self.outs)
		self.res.add([x, info], self.score)
		#print('job', self.id, 'finish')
		

def Task(ProgramDic, IOList, threads=1):
	codeDic = {}
	for auther, prog in ProgramDic.items():
		f = open(prog, 'r')
		codeDic[auther] = f.read()
		f.close()
	sum, tt = 0, 0
	for io in IOList:
		try:
			sum += io[2]
		except:
			tt += 1
	avr = (100-sum)/tt
	iolist = []
	for io in IOList:
		fi = open(io[0], 'r')
		fo = open(io[1], 'r')
		#print(io[0], io[1])
		si = fi.read().split()
		so = fo.read()
		try:
			iolist.append((si, so, io[2]))
		except:
			iolist.append((si, so, avr))
		#print(iolist[-1])
		fi.close()
		fo.close()

	joblist = [JobQueue() for i in range(threads)]
	index = 0
	resDic = {}
	_id = 0
	for auther, code in codeDic.items():
		resDic[auther] = Result()
		#print('author:'+auther+'\n', code, '\n')
		for io in iolist:
			#print(io[0], io[1])
			joblist[index].add(Job(code, io[0], io[1], resDic[auther], io[2], _id))
			_id += 1
			index = (index+1) % threads
	for i in range(threads):
		joblist[i].start()
	for i in range(threads):
		joblist[i].join()
	for k, v in resDic.items():
		resDic[k] = v.get()
	return resDic

if __name__ == "__main__":
	proglist = {'std':'example/test/1volume/std.py', 'strange':'example/test/1volume/strange.py', 'wrong':'example/test/1volume/wrong.py'}
	iolist = [
		('example/test/1volume/0.in', 'example/test/1volume/0.ans'), 
		('example/test/1volume/1.in', 'example/test/1volume/1.ans'), 
		('example/test/1volume/2.in', 'example/test/1volume/2.ans'), 
		('example/test/1volume/3.in', 'example/test/1volume/3.ans'), 
		('example/test/1volume/4.in', 'example/test/1volume/4.ans'), 
	]
	#iolist = iolist 
	start = time.time()
	resFullDic = Task(proglist, iolist)
	print('time = ', time.time()-start)
	for k, v in resFullDic.items():
		print(k+' '*(10-len(k)), v[0])
	