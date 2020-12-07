import time

class IO:
	def __init__(self, data):
		self.data = data
		self.index = 0
		self.ret = ''
	def step(self,*args):
		print(*args, end='')
		if self.index < len(self.data):
			ret = self.data[self.index]
			self.index += 1
			return ret
		else:
			return ''
	
	def output(self, *args, **argv):
#		print('args = ', args)
#		print('argv = ', argv)
		argd = {'sep':' ', 'end':'\n'}
		for k, v in argv.items():
			argd[k] = v
		data = [str(x) for x in list(args)]
		self.ret += argd['sep'].join(data)+argd['end']
		#print(self.ret)

	def result(self):
		return self.ret

def runner(input, print, program):
	#print('code:',program)
	start_time = time.time()
	try:
		exec(program)
		return 1, '%.3f'%(time.time()-start_time)
	except Exception as e:
		return 0, 'code:'+program+'error:'+str(e)


def judge(program, stdin, stdout):
	io = IO(stdin)
	i, o, r = io.step, io.output, io.result
	flag, info = runner(i, o, program)
	out = r()
	while len(stdout) > 0 and stdout[-1] == '\n':
		stdout = stdout[:-1]
	while len(out) > 0 and out[-1] == '\n':
		out = out[:-1]
	
	if flag == 1:
		if out == stdout:
			return 1, {'stat': 'accpet', 'time':info, 'info':""}
		else:
			return 0, {'stat': 'wrong answer', "info":out+'!='+stdout}
	return 0, {'stat': 'runtime error', 'info':info}
	# TODO TLE and MLE

def exam(pfile, ifile, ofile):
	pf = open(pfile, 'r')
	program = pf.read()
	pf.close()
	inf = open(ifile, 'r')
	stdin = inf.read().split()
	inf.close()
	outf = open(ofile, 'r')
	stdout = outf.read()
	outf.close()

	return judge(program, stdin, stdout)

if __name__ == '__main__':
	print(exam('example/test/1volume/std.py', 'example/test/1volume/1.in', 'example/test/1volume/1.ans'))
