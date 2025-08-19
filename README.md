# Emnati2022 — Data Preparation for Cyclone Emnati Displacement Study

## Overview
This repository accompanies my Master's project on **flood-induced displacement during Cyclone Emnati (2022) in Madagascar**.  
It contains the **input files** and **data preparation scripts** I used to set up simulations in the [Flee/DFlee](https://github.com/djgroen/flee) agent-based modeling framework.  

**Note**: This repository is not intended to be a standalone, reusable package. The files here document the workflow and inputs I used for my research.

---

## Contents

Emnati2022/
├── dataprep.ipynb # Notebook used to clean and process raw data
├── NNroutes.py # Helper script for route network construction
├── mdg_admpop_adm2_2018.csv # Population by ADM2 (2018), used in preprocessing
├── base/ # Contains all the files related to the base and extended simulation
├── extraCamp/ # Contains all the files related to the extra camp scenario
├── removedCamp/ # Contains all the files related to the removed camp scenario
└── README.md # This document

---

## Purpose of This Repository
- Provide transparency about how raw data were processed into simulation-ready input files.  
- Store the exact input datasets that fed into the Flee/DFlee simulations used in my study.  

This repository **does not**:  
- Include the Flee/DFlee codebase itself.  
- Provide a general-purpose preprocessing pipeline.  
- Aim to be directly runnable by external users.  

---

## Related Work
The simulation results generated with these inputs are discussed in my research on **Simulation of forced displacements in response tocyclone Emnati in Madagascar**.

---

## Author
**Luke Kraakman**  
---
