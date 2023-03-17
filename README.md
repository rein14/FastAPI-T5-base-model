# T5-base-model FastAPI
The model t5 base is a Natural Language Processing (NLP) Model implemented in Transformer library, generally using the Python programming language. More on this at: https://huggingface.co/t5-base.
What we are doing here is bascially translate languages suppport by the model.

Build and run the Docker image locally, as follows:

```
docker build -t image .
docker run -d --name container 80:80 image
```
## Requirements
This was built on 8gb of ram and 2.3ghz cpu speed
