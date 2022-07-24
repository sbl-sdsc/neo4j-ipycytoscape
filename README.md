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

**2. Create a Conda environment**

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

**4. Deactivate the Conda environment**

When you are finished, deactivate the conda environment or close the terminal window.

```
conda deactivate
```

------
> To remove the Conda environment, run ```conda env remove -n neo4j-ipycytoscape```
------


## Run Jupyter Lab in your web browser using [Pangeo Binder](https://aws-uswest2-binder.pangeo.io/)

**NOTE:** Authentication is required to launch binder! Sign into GitHub from your browser, then click on the `launch binder` badge below to launch Jupyter Lab.

[![Binder](https://aws-uswest2-binder.pangeo.io/badge_logo.svg)](https://aws-uswest2-binder.pangeo.io/v2/gh/sbl-sdsc/neo4j-ipycytoscape/master)

**Pangeo Binder is unsupported and may not always be available or slow. Launching Jupyter Lab may take a few minutes.**


## Run Jupyter Lab on SDSC Expanse
------
Prerequisites:
* [XSEDE account](https://portal.xsede.org/my-xsede?p_p_id=58&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_58_struts_action=%2Flogin%2Fcreate_account)
* [Expanse allocation](https://portal.xsede.org/documentation-overview)
* Append ```export PATH="/cm/shared/apps/sdsc/galyleo:${PATH}"``` to your ```.bashrc``` on Expanse and run ```source ./.bashrc```

------

1. Log into the [Expanse Portal](https://portal.expanse.sdsc.edu/) with your XSEDE credentials.
    
2. Open a Terminal Window ("Shell Access") through the [Expanse Portal](https://portal.expanse.sdsc.edu/)

3. Clone the Git repository neo4j-ipycytoscape
```
git clone https://github.com/sbl-sdsc/neo4j-ipycytoscape.git
```
  
4. Launch Jupyter Lab using the Galyleo 

   Fill in the your project account number in the command below.

   This script will generate a URL for your Jupyter Lab session.
```
galyleo launch --account <account_number> --partition shared --cpus 4 --memory 8 --time-limit 00:30:00 --conda-env neo4j-ipycytoscape --conda-yml "${HOME}/neo4j-ipycytoscape/environment.yml" --mamba
```

5. Open a new tab in your web browser and paste the Jupyter Lab URL.

> You should see the Satellite Reserver Proxy Servive page launch in your browser.

    Wait until Jupyter Lab launches. This may take several minutes.

6. Run the example notebooks

   Navigate to the [`notebooks`](notebooks) directory to run the example Jupyter Notebooks.
   
7. Shutdown Jupyter Lab
   
   From the file menu select ```Shutdown``` to terminate the process.
   
> If you do not shutdown Jupyter Lab, the process will continue running and use up allocated resources.


## Citation
Peter W. Rose, David Valentine, Ilya Zaslavsky, COVID-19-Net: Integrating Health, Pathogen and Environmental Data into a Knowledge Graph for Case Tracking, Analysis, and Forecasting. Available online: https://github.com/covid-19-net/covid-19-community (2020).

## Funding
The Neo4j graph visualization for ipycytoscape is in part supported by the National Science Foundation under Award Numbers:

**NSF Convergence Accelerator Phase I (RAISE):** Knowledge Open Network Queries for Research (KONQUER) ([1937136](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1937136))

**NSF RAPID:** COVID-19-Net: Integrating Health, Pathogen and Environmental Data into a Knowledge Graph for Case Tracking, Analysis, and Forecasting ([2028411](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2028411))
