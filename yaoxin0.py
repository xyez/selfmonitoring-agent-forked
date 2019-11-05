from eval import Evaluation
eva=Evaluation(['test'])
a,b=eva.score('results/cogrounding-selfmonitoring-agent_test_epoch_320.json')

# eva=Evaluation(['val_seen'])
# a,b=eva.score('results/cogrounding-selfmonitoring-agent_val_seen_epoch_320.json')
print('heer')