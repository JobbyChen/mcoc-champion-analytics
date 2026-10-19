# MCOC Champion Analytics Dashboard

An interactive web dashboard for exploring and analyzing champion data from **Marvel Contest of Champions (MCOC)**.

**[View Live Dashboard](https://jobbychen.github.io/mcoc-champion-analytics/frontend/index.html)** | **[Explore API](https://mcoc-champion-api.onrender.com/champions)**

## Project Overview

This project demonstrates an end-to-end data management workflow, from collecting and validating raw data to storing structured records and presenting them through an interactive website.

The dashboard allows users to explore a dataset of **332 champion records**, search for individual champions, filter by class and tier, and visualize class distributions.

I built this project to strengthen my practical skills in Python, SQL, data quality assurance, API development, and data visualization.

## Features

- **Champion Explorer:** Browse and search champion records.
- **Interactive Filters:** Filter champions by class and tier.
- **Data Visualization:** View champion distributions using Chart.js.
- **Data Validation:** Check for duplicate records, missing values, and invalid classifications.
- **Automated Collection:** Collect champion information with progress saving and failed-request tracking.
- **REST API:** Retrieve structured champion information through FastAPI.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data collection and processing |
| Pandas | Data cleaning, transformation, and validation |
| SQLite / SQL | Structured data storage and querying |
| FastAPI | Backend API development |
| HTML, CSS, JavaScript | Frontend dashboard |
| Chart.js | Interactive visualizations |
| GitHub Pages | Frontend hosting |
| Render | Backend hosting |

## Data Pipeline

1. **Collection:** Retrieve champion information from the source website.
2. **Processing:** Convert raw information into a structured dataset.
3. **Validation:** Check uniqueness, completeness, and valid classifications.
4. **Storage:** Load champion records into SQLite.
5. **API:** Use FastAPI to retrieve and filter stored data.
6. **Visualization:** Display champion information through an interactive dashboard.

## Data Sources and Attribution

Champion information and community tier rankings are sourced from [MCOC.app](https://mcoc.app/), with permission for collection and public display.

Tier rankings represent community opinions rather than objective performance measurements. Marvel Contest of Champions and associated intellectual property belong to their respective owners. This is an independent fan-made analytics project.

## What I Learned

This project helped me develop practical experience with:

- Designing and maintaining structured datasets.
- Identifying and handling common data quality issues.
- Automating repetitive data collection tasks.
- Using SQL to retrieve and aggregate information.
- Connecting a database-backed API to a user-facing dashboard.
- Deploying and troubleshooting a full-stack web application.

A major takeaway was understanding that **data reliability matters just as much as data collection**. Building a useful dashboard requires not only gathering information, but also checking its accuracy, consistency, and accessibility.

## Deployment

The frontend is hosted on GitHub Pages, while the FastAPI backend is hosted on Render.

The backend runs on a free hosting instance, so the first request after inactivity may take additional time.

## Future Improvements

- Add more detailed champion statistics.
- Expand analytics and comparisons between classes and tiers.
- Add automated data refresh and validation workflows.
- Improve dashboard responsiveness and user experience.