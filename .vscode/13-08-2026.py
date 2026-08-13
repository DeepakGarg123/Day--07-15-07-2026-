from datasets import load_dataset
import torch 
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

# 1. Load and subset the dataset
dataset = load_dataset("stanfordnlp/imdb")
train_dataset = dataset['train'].shuffle(seed=42).select(range(2000))
test_dataset = dataset['test'].shuffle(seed=42).select(range(500))

# 2. Setup the Tokenizer
model_name = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Quick sanity check prints
text = 'I really enjoyed this movie'
print("Tokens:", tokenizer.tokenize(text))
print("Input IDs:", tokenizer(text)['input_ids'])

# 3. Tokenize the entire dataset
def tokenize_function(examples):
    return tokenizer(
        examples['text'],
        truncation=True,
        max_length=128,
        padding='max_length'
    )

tokenized_train = train_dataset.map(tokenize_function, batched=True)
tokenized_test = test_dataset.map(tokenize_function, batched=True)

# 4. Load the Model
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, 
    num_labels=2
)

# 5. Define Training Arguments
training_args = TrainingArguments(
    output_dir='./sentiment_model',
    eval_strategy='epoch',
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,
    weight_decay=0.01,
    report_to='none'
)

# 6. Initialize the Trainer (Fixed train_dataset here)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train, # Changed from tokenized_test to tokenized_train
    eval_dataset=tokenized_test,
)

# 7. Train and Evaluate
trainer.train()
results = trainer.evaluate()
print("Evaluation Results:", results) 

# 8. Define Prediction Function (Fixed indentation and the 'input' typo)
def predict_sentiment(text):
    inputs = tokenizer(
        text, 
        return_tensors='pt', 
        truncation=True,
        padding=True
    )
    
    # Move inputs to the same device as the model (CPU or GPU)
    inputs = {key: value.to(model.device) for key, value in inputs.items()} # Fixed 'input' to 'inputs'
    
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()
        
    if prediction == 1:
        return "Positive"
    else:
        return "Negative"

# 9. Test your final trained model!
print("Prediction:", predict_sentiment("This film was absolutely terrible."))
print("Prediction:", predict_sentiment("I loved every single second of it!"))
print("Prediction:", predict_sentiment("This film was boring") )
print("Prediction:" , predict_sentiment("I will not ever see this movie again"))
