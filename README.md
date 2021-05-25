# TwitterNLPDocker

Minimum example of running Ritter et al., 2011's [Twitter NER system](https://github.com/aritter/twitter_nlp) via Docker.

## Usage
```
docker build -t twitternlp:latest .
docker run -p 5000:5000 twitternlp
```

POST data to parse:
```
# via cURL
curl -X POST '0.0.0.0:5000/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "sents": ["The Horse raced past the barn fell"]
    }'
```
or
```
# via python
import requests
url = 'http://0.0.0.0:5000'
data = {"sents": ["The Horse raced past the barn fell"]}
res = requests.post(url, json=data)
```
Either should give the following response:
```
{
  "parsed": [
    "The/B-ENTITY Horse/I-ENTITY raced/O past/O the/O barn/O fell/O\n"
  ]
}
```