import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError("List must contain nine numbers.")
  else:
    lst1 = [[list[0], list[1], list[2]], [list[3], list[4], list[5]], [list[6], list[7], list[8]]]
  ar = np.array(lst1)
  calculations = {}
  calculations["mean"] = [np.mean(ar, axis=0).tolist(), np.mean(ar, axis=1).tolist(), np.mean(ar.flatten())]
  calculations["variance"] = [np.var(ar, axis=0).tolist(), np.var(ar, axis=1).tolist(), np.var(ar.flatten())]
  calculations["standard deviation"] = [np.std(ar, axis=0).tolist(), np.std(ar, axis=1).tolist(), np.std(ar.flatten())]
  calculations["max"] = [np.max(ar, axis=0).tolist(), np.max(ar, axis=1).tolist(), np.max(ar.flatten())]
  calculations["min"] = [np.min(ar, axis=0).tolist(), np.min(ar, axis=1).tolist(), np.min(ar.flatten())]
  calculations["sum"] = [np.sum(ar, axis=0).tolist(), np.sum(ar, axis=1).tolist(), np.sum(ar.flatten())]
  return calculations