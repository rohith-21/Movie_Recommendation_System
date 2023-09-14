import gzip
import pickle

inp = 'similarity.pkl'
out = 'comp.pkl.gz'

with open(inp, 'rb') as inp_file:
    data = pickle.load(inp_file)

with gzip.open(out, 'wb') as out_file:
    pickle.dump(data, out_file)

print("Out")
