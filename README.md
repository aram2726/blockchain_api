# Blockchain Flask API

#### Development requirements

* python3.6

```bash
$ sudo apt install python3.6
$ sudo apt install python3.6-dev
$ sudo apt install python3-pip
$ pip3 install --user pipenv
$ echo "PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
```

* create a GENESIS block in blockchain directory
 and name it as 1
```bash
$ mkdir blockchain && cd blockchain
$ pipenv install
$ echo { "id": 1, "name": "string", "amount": 10, "to_whom": "string", "hash": ""} > 1
```

* License
[MIT](https://github.com/alkhachatryan/spyonspies/blob/master/LICENSE "MIT")
