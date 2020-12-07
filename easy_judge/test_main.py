from servant import build_from_config
match = build_from_config('../example/config.txt')
res = match.run()
for k, v in res.items():
	print(k, ': score =', v['score'], 'tot =', v['tot'])