#%% 
from transformers import pipeline

#%%
pipe = pipeline("question-answering")
answer = pipe(
    context = "The Big Apple is a nickname for New York City.",
    question = "What is the Big Apple?"
)

answer