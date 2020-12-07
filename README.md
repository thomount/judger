# Auto Judger Library

## introduction

A library that allow you to judge python codes.

## requirements

## installation

	git clone https://github.com/thomount/judger.git
	cd judger
	python3 setup.py install

## usage

	from judger import build_from_config
	match = build_from_config(config_file_full_path)
	result = match.run()

Result is a dict where key is name and value is status;

Status is also a dict with total score as 'tot', scores for each problem as 'score', and details as 'detail';

Details is a list of details for each problem;

In each problem, details is a list of details for each testcase;

In each testcase, details is a combination of status(accept, wrong answer, runtime error) as 'stat' and detail information(correct answer and wrong answer) as 'info' and running time(only for correct cases).

Here is an example for whole result structure:

	{'std': {'score': [100.0, 100.0], 'tot': 200.0, 'detail': [[{'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}], [{'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}]]}, 'strange': {'score': [40.0, 80.0], 'tot': 120.0, 'detail': [[{'stat': 'wrong answer', 'info': '1!=0'}, {'stat': 'wrong answer', 'info': '1001!=1000'}, {'stat': 'wrong answer', 'info': '513!=512'}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}], [{'stat': 'wrong answer', 'info': '0!=wrong'}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'accpet', 'time': '0.000', 'info': ''}]]}, 'wrong': {'score': [0.0, 20.0], 'tot': 20.0, 'detail': [[{'stat': 'wrong answer', 'info': '1!=0'}, {'stat': 'wrong answer', 'info': '1001!=1000'}, {'stat': 'wrong answer', 'info': '513!=512'}, {'stat': 'wrong answer', 'info': '2!=1'}, {'stat': 'wrong answer', 'info': '970300!=970299'}], [{'stat': 'accpet', 'time': '0.000', 'info': ''}, {'stat': 'wrong answer', 'info': 'wrong!=10'}, {'stat': 'wrong answer', 'info': 'wrong!=5050'}, {'stat': 'wrong answer', 'info': 'wrong!=1'}, {'stat': 'wrong answer', 'info': 'wrong!=55'}]]}}

To write a config file, follow the formate below:

	problem=name_for_problem1
	code=path_for_codes
	io=path_for_io_files
	end
	problem=name_for_problem2
	...
	end

Notice that, your codes should be put like this:

	codes/
		student_name1/
			name_for_problem1.py
			name_for_problem2.py
			...
		student_name2/
			...
		...

Please take folder like ```codes``` as ```path_for_codes```

And your input and output files should be put like this:
	
	io/
		0.in
		0.out
		1.in
		1.out
		...

Each pair of input and output should have the same prefix with different suffix where '.in' for input and '.out' for output.

Please take folder like ```io``` as ```path_for_io_files```

Here is some well-designed codes and datas in folder ```example```, you can try the function on this folder.

