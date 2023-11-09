# RoseTTAFold-local-server

It is a simple local server of [RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold) or [RoseTTAFold2](https://github.com/uw-ipd/RoseTTAFold2). Ubuntu ≥ 20.04 is recommended. Remember change the folder path in the code before running it.


## Environment:

```
python = 3.8.10
pandas
remi
```

The environment required `pandas` and `remi` based on python3. We recommend conda environment of [RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold) or [RoseTTAFold2](https://github.com/uw-ipd/RoseTTAFold2). Just need install `remi` by `conda install -c conda-forge remi`. Then `conda activate RoseTTAFold` or `conda activate RF2` and `python Code/web.py`. The webpage is start in `http://0.0.0.0:46429`.


You can install from requirement file:

```
conda install --yes --file RF_requirements.txt`  # RoseTTAFold
conda install --yes --file RF2_requirements.txt`  # RoseTTAFold2
```

Or, you can also create the environment by conda command:

```
conda env create -f RF_environment.yaml  # RoseTTAFold
conda env create -f RF2_environment.yaml  # RoseTTAFold2
```

Then

```
conda activate RFlocalserver # RoseTTAFold
conda activate RF2 # RoseTTAFold2
```

Lastly, set up the server:

`python Code/web.py`

It's important to note that, `background_service.py` need [RoseTTAFold environment](https://github.com/RosettaCommons/RoseTTAFold):
```shell
conda activate RoseTTAFold # RoseTTAFold
conda activate RF2         # RoseTTAFold2
python Code/background_service.py`
```

## Context:

There are 2 parts: codes and running data.

### Codes include 3 files:

`Code/web.py`: The website of the server. It will receive the amino acid sequence and write to `apply.csv`. The conda or python environment need `remi` library.

`Code/background_server.py`: The background running program of the server.  When `apply.csv` is not empty, it will create the run indicator file `test.fa` and start calculation. When finish indicator file `model5.pdb` exist, it will shear the imformation from `apply.csv` to `result.csv`. The results will be  compressed into a `tar.gz` file and transferred to the `result` folder for `web.py` retrieval. Remember activate `RoseTTAFold` environment of conda before running it. The environment could refer to the github of [RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold).

`Code/apply.sh` The running file. It will execute the RoseTTAFold run command and place the completed file in a specific location. We prefer pyrosetta than e2e.

### Running data includes 3 files and 1 folder:

`RunningData/running` folder include the calculating amino acid chain. After calculating, all the files in the folder will be compressed and move to specific folder.

`RunningData/apply.csv` includes the applied mission from web. When calculation finishes, the first line would be move to `result.csv`.

`RunningData/result.csv` records completed calculations. It includes the position of compressed file in specific folder.

## Citing this work

Fei Liu, Xiangkang Jiang, Jingyuan Yang, Jiawei Tao, Mao Zhang, A chronotherapeutics-applicable multi-target therapeutics based on AI: Example of therapeutic hypothermia, Briefings in Bioinformatics, 2022;, bbac365, https://doi.org/10.1093/bib/bbac365

M. Baek, et al., Accurate prediction of protein structures and interactions using a three-track neural network, Science (2021). 

I.R. Humphreys, J. Pei, M. Baek, A. Krishnakumar, et al, Computed structures of core eukaryotic protein complexes, Science (2021). 

## License

The license of the project is MPL-2.0.

## Screenshot

![Screenshot](Figure/Screenshot1.png)
