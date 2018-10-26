# Blockchain Flask API

#### Development requirements

* python3.6

```bash
$ virtualenv <YourVenvName>
$ pip install -r requirements.txt
```

* create a GENESIS block in blockchain directory
 and name it as 1
```bash
$ mkdir blockchain && cd blockchain
$ echo { "id": 1, "name": "string", "amount": 10, "to_whom": "string", "hash": ""} > 1
```
