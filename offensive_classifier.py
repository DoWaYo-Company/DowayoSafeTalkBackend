from torchsummary import summary
from transformers import AutoModelForSequenceClassification, AutoTokenizer

access_token = "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"


model = AutoModelForSequenceClassification.from_pretrained("KoalaAI/OffensiveSpeechDetector", token=access_token)

tokenizer = AutoTokenizer.from_pretrained("KoalaAI/OffensiveSpeechDetector", token=access_token)

inputs = tokenizer("Hello my name is john", return_tensors="pt")
print(inputs)
print(type(model))
outputs = model(**inputs)
print(outputs)

summary(model, **inputs)

