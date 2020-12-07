from manager import Task
import os
class Problem:
	def __init__(self, **argv):
		self.iolist = []
		self.codedic = {}
		# parse argv
		name, cdir, iodir = None, None, None
		if 'name' in argv:
			name = argv['name']
		if 'cdir' in argv:
			cdir = argv['cdir']
		if name != None and cdir != None:
			dirList = os.listdir(cdir)
			for folder in dirList:
				if os.path.isdir(cdir+'/'+folder):
					if os.path.isfile(cdir+'/'+folder+'/'+name+'.py'):
						self.codedic[folder] = cdir+'/'+folder+'/'+name+'.py'
			
		if 'iodir' in argv:
			iodir = argv['iodir']
			filelist = os.listdir(iodir)
			keydist = {}
			for file in filelist:
				parts = file.split('.')
				name, tail = parts[0], parts[1]
				if name not in keydist:
					keydist[name] = {'in':None, 'out':None}

				if tail == 'in' or tail == 'out':
					keydist[name][tail] = file
				
			for k, v in keydist.items():
				if v['in'] != None and v['out'] != None:
					self.iolist.append((iodir+'/'+v['in'], iodir+'/'+v['out']))

	def add_student_list(self, studentlist):
		pass
	def add_student_file(self, file):
		pass
	def add_io_list(self, iolist):
		pass
	def add_i_dir(self, idir):
		pass
	def add_o_dir(self, odir):
		pass
	def run(self):
		return Task(self.codedic, self.iolist, 1)

class Match:
	def __init__(self):
		self.problem_list = []
	def add_problem(self, problem):
		self.problem_list.append(problem)
	def run(self):
		pb_num = len(self.problem_list)
		whole_dic = {}
		for i in range(len(self.problem_list)):
			res = self.problem_list[i].run()
			#print(res)
			for k, v in res.items():
				if k not in whole_dic:
					whole_dic[k] = {'score':[0] * pb_num, 'tot':0, 'detail':[None] *pb_num}
				whole_dic[k]['score'][i] += v[0]
				whole_dic[k]['tot'] += v[0]
				whole_dic[k]['detail'][i] = v[1]
		return whole_dic
			
def parse_config(configFile):
	f = open(configFile, 'r')
	content = f.read().split('\n')
	f.close()

	pb_list = []
	pb_dic = {}
	# TODO parse config
	for line in content:
		parts = line.split('=')
		if parts[0] == 'problem':
			pb_dic['name']=parts[1]
		if parts[0] == 'code':
			pb_dic['cdir'] = parts[1]
		if parts[0] == 'io':
			pb_dic['iodir'] = parts[1]
		if parts[0] == 'end':
			pb_list.append(pb_dic)
			pb_dic = {}
	
	return pb_list

def build_from_config(config_file):
	#load config file
	config = parse_config(config_file)
	match = Match()
	for pb in config:
		prob = Problem(name=pb['name'], cdir = pb['cdir'], iodir = pb['iodir'])
		match.add_problem(prob)
	return match


