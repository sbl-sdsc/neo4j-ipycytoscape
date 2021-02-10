# neo4j-ipycytoscape

This repo demonstrates how to use the [ipycytoscape widget](https://github.com/QuantStack/ipycytoscape) to visualize a Neo4j subgraph with cytoscape.js in JupyterLab and the Jupyter notebook.

### Launch Jupyter Lab on [Pangeo Binder](https://binder.pangeo.io/)

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/sbl-sdsc/neo4j-ipycytoscape/master)

|Notebook|Description|
|:-------|:----------|
|[Neo4j_Example1](notebooks/Neo4j_Example1.ipynb)| Creates a small Neo4j graph locally and demonstrates how to display a Neo4j subgraph|
|[Neo4j_Example2](notebooks/Neo4j_Example2.ipynb)| Accesses the  COVID-19-Net Knowledge Graph server and demonstrates how to display a Neo4j subgraph|

When running this project on [Pangeo Binder](https://binder.pangeo.io/), a Neo4j database server is [setup](../binder/postBuild) and [started](../binder/start). This may take a few minutes.

#### Local Neo4j installation
When running Neo4j_Example1.ipynb locally, you need to install and start the Neo4j database:

1. [Download Neo4j](https://neo4j.com/download/)
2. Launch Neo4j Browser
3. Create a new database
4. Set password to "neo4jbinder"
5. Start database

## Citation
Peter W. Rose, David Valentine, Ilya Zaslavsky, COVID-19-Net: Integrating Health, Pathogen and Environmental Data into a Knowledge Graph for Case Tracking, Analysis, and Forecasting. Available online: https://github.com/covid-19-net/covid-19-community (2020).

## Funding
The Neo4j graph visualization for ipycytoscape is in part supported by the National Science Foundation under Award Numbers:

**NSF Convergence Accelerator Phase I (RAISE):** Knowledge Open Network Queries for Research (KONQUER) ([1937136](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1937136))

**NSF RAPID:** COVID-19-Net: Integrating Health, Pathogen and Environmental Data into a Knowledge Graph for Case Tracking, Analysis, and Forecasting ([2028411](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2028411))
