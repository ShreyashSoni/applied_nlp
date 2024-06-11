#%%
from transformers import pipeline

#%%
pipe = pipeline(task="ner")
named_enitites = pipe("Apple Inc. was founded by Steve Jobs, Steve Wozniack, and Ronald Wayne on April 1, 1976, in Cupertino, California.")
named_enitites
# %%
