# neo4j-ipycytoscape

This repo demonstrates how to use the [ipycytoscape widget](https://github.com/QuantStack/ipycytoscape) to visualize a Neo4j subgraph with cytoscape.js in JupyterLab and the Jupyter notebook.

|Notebook|Description|
|:-------|:----------|
|[Neo4j_Example1](notebooks/Neo4j_Example1.ipynb)| Creates a small Neo4j graph locally and demonstrates how to display a Neo4j subgraph|
|[Neo4j_Example2](notebooks/Neo4j_Example2.ipynb)| Accesses the  COVID-19-Net Knowledge Graph server and demonstrates how to display a Neo4j subgraph|

## Run Jupyter Lab locally
Follow the steps below to setup and run the example notebooks on Mac, Linux, or Windows.

------
Prerequisites: Miniconda3 (light-weight, preferred) or Anaconda3 and Mamba

* Install [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)
* Update an existing miniconda3 installation: ```conda update conda```
* Install Mamba: ```conda install mamba -n base -c conda-forge```
* Install Git (if not installed): ```conda install git -n base -c anaconda```
------

**1. Clone this Git repository**

```
git clone https://github.com/sbl-sdsc/neo4j-ipycytoscape.git
cd neo4j-ipycytoscape
```

**2. Create a conda environment**

The file `environment.yml` specifies the Python version and all packages required by the tutorial. 
```
mamba env create -f environment.yml
```

Activate the conda environment
```
conda activate neo4j-ipycytoscape
```

**3. Launch Jupyter Lab**
```
jupyter lab
```

Navigate to the [`notebooks`](notebooks) directory to run the example Jupyter Notebooks.

**4. Deactivate the conda environment**

When you are finished, deactivate the conda environment or close the terminal window.

```
conda deactivate
```

> To remove the CONDA environment, run ```conda env remove -n neo4j-ipycytoscape```


## Run Jupyter Lab in your web browser using [Pangeo Binder](https://aws-uswest2-binder.pangeo.io/)

**NOTE:** Authentication is required to launch binder! Sign into GitHub from your browser, then click on the `launch binder` badge below to launch Jupyter Lab.

[![Binder](https://aws-uswest2-binder.pangeo.io/badge_logo.svg)](https://aws-uswest2-binder.pangeo.io/v2/gh/sbl-sdsc/neo4j-ipycytoscape/master)

**Pangeo Binder is unsupported and may not always be available or slow. Launching Jupyter Lab may take a few minutes.**



## Citation
Peter W. Rose, David Valentine, Ilya Zaslavsky, COVID-19-Net: Integrating Health, Pathogen and Environmental Data into a Knowledge Graph for Case Tracking, Analysis, and Forecasting. Available online: https://github.com/covid-19-net/covid-19-community (2020).

## Funding
The Neo4j graph visualization for ipycytoscape is in part supported by the National Science Foundation under Award Numbers:

**NSF Convergence Accelerator Phase I (RAISE):** Knowledge Open Network Queries for Research (KONQUER) ([1937136](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1937136))

**NSF RAPID:** COVID-19-Net: Integrating Health, Pathogen and Environmental Data into a Knowledge Graph for Case Tracking, Analysis, and Forecasting ([2028411](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2028411))
