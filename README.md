This repo contains the code to reproduce all the experiments described in the paper `Hierarchical Point-Of-Interest Kernels for Analysis andClassification of Urban Areas (Barlacchi et al., 2018)` submitted for the Research Track at [KDD](http://www.kdd.org/kdd2018/).

## Requirements

Install a Python Virtual Environment using python>=3.3. Then install the required packages from the provided `requirements.txt` 

- JAVA???

```python
pip install -r requirements.txt
```

## Project Structure

The project is organised as follows:

* `GeoL` = The Geospatial Library developed for running menial and generic data cleaning and pre-processing tasks when using geographic data for Machine Learning.

* `notebooks` = This folder contains two notebooks used to prepare and then run the experiments on the Urban Atlas and Foursquare datasets respectively.

* `scripts` = Simple Python executables to perform generic operations (e.g. prepare the folder structure etc...)

#### A note on the datasets:

Due to legal constrains, we could not provide the data as they are. Both Urban Atlas and Foursquare require in fact a registration and forbid a straightforward re-use. They can both be freely downloaded at their respective websites.
