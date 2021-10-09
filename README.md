# rosettafold-local-server

It is a simple local server of rosettafold based on python.

## Requirement:

```
pandas
remi
```

## Context:

There are three files:

`web.py`: The website of the server. It will receive the amino acid sequence and write to `apply.csv`.

`background_server.py`: The background running program of the server.  When `apply.csv` is not empty, it will create the run indicator file `test.fa` and start calculation. When finish indicator file `model5.pdb` exist, it will shear the imformation from `apply.csv` to `result.csv`. The results will be  compressed into a `tar.gz` file and transferred to the `result` folder for `web.py` retrieval.

`apply.sh` The running file. It will execute the rosettafold run command and place the completed file in a specific location.
