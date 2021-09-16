Project Description
==============================

This is a data analytics / ML project that aims to understand the behavior of AWS spot instances. The relevance of this work is that spot instances cost a fraction of the on-demand ones, sometimes with discounts of 90%! Therefore, the business problem that we want to solve is to reduce the costs of cloud services.

Although spot instances are very appealing, they come with some caveats: there is no availability guarantee, i.e., the spot instance can be interrupted and you lose the resource (this process is called eviction). Therefore, what we want to know is if there is a minimum period of time that we can use the spot instance without being interrupted. If so, we could use that resource at a fraction of the on-demand one.

As an extra challenge, I would like to know if we can switch to other spot instances when one is going to expire. In that sense, I want to know which are the spot instances that can be good candidates to move to.

Some companies such as [Spot](https://spot.io) leverages spot instances to reduce the costs of cloud usage (and they have been bought by NetApp).

This first version contains the analytics of the AWS pricing data and the clustering of spot instances that have the same eviction pattern.

For this pet project, I used the following libraries:
- Pandas: nothing better than Pandas to do data wrangling =)
- Matplotlib: quick plot of results for analysis;
- Plotly: interactive 3D plots to see the distribution of clusters / instances;
- papermill: data pipeline create. It allowed me to organize all jupyter notebooks in a data pipeline, making it possible to repeat the process consistently (inspired by this [Netflix article](https://netflixtechblog.com/notebook-innovation-591ee3221233).
- cookiecutter: convention over configuration. This is important to have consistency across projects and this helped me to have a consistent project of all my data projects.

Running the Project
------------

1. Get to the notebooks folder, open `PM_main.ipynb`, and execute it. This will start the pipeline to generate all parsing, transformations, analytics and report generation.

If you want, it is possible to run each notebook individually. They have local parameters that enables them to work in a standalone way.

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
