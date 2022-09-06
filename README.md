# RoseTTAFold-local-server

It is a simple local server of [RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold) based on python and ubuntu 20.04. Change the file path in the code before running it.


## Requirement:

```
python = 3.8.10
pandas
remi
```

## Context:

There are three files:

`web.py`: The website of the server. It will receive the amino acid sequence and write to `apply.csv`. The conda or python environment need `remi` library.

`background_server.py`: The background running program of the server.  When `apply.csv` is not empty, it will create the run indicator file `test.fa` and start calculation. When finish indicator file `model5.pdb` exist, it will shear the imformation from `apply.csv` to `result.csv`. The results will be  compressed into a `tar.gz` file and transferred to the `result` folder for `web.py` retrieval. Remember activate `RoseTTAFold` environment of conda before running it. The environment could refer to the github of [RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold).

`apply.sh` The running file. It will execute the RoseTTAFold run command and place the completed file in a specific location.

## Citing this work

If you use the code or data in this package, please cite:

Fei Liu et.al, A chronotherapeutics-applicable multi-target therapeutics based on AI: the example of therapeutic hypothermia, Briefings in Bioinformatics, DOI:10.1093/bib/bbac365.

# Screenshot

![Screenshot](Figure/Screenshot.png)
