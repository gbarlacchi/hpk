This repo contains the code to reproduce all the experiments described in the paper `Hierarchical Point-Of-Interest Kernels for Analysis andClassification of Urban Areas (Barlacchi et al., 2018)` submitted for the Research Track at [KDD](http://www.kdd.org/kdd2018/).

## Requirements

* Install a Python Virtual Environment using python>=3.3. Then install the required packages from the provided `requirements.txt`

```python
pip install -r requirements.txt
```

* To run the experiments you will need HPK. We implemented HPK as an additional kernel in [Kelp](https://github.com/SAG-KeLP/), a java machine learning framework focusing on kernel machines for structured data. HPK can be installed with the provided `kelp-classify.jar` file.

You will also need `GeoL, The [Geospatial Library](https://github.com/gbarlacchi/GeoL) developed for running generic data cleaning and pre-processing tasks when using geographic data with Machine Learning.


## Project Structure

The project is organised as follows:

* `notebooks` = This folder contains the notebooks used to prepare and run the experiments. There are three notebooks: two for pre-processing respectively the Urban Atlas and Foursquare datasets, and a third one to run the experiments which should be run last.

* `scripts` = Simple Python executables to perform generic operations (e.g. prepare the folder structure etc...)

* `data` = Test and Train datasets available for all the analysed cities.

#### A note on the datasets:

Due to legal constrains, we could not provide the data as they are. Both Urban Atlas and Foursquare require in fact a registration and forbid a straightforward re-use.

* Urban Atlas can be freely downloaded through [its portal](https://land.copernicus.eu/local/urban-atlas/urban-atlas-2012).
* Foursquare data can be retrieved using GeoL's crawler. It requires an appropriate API key.
