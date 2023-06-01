# AuthentiChain: Ethereum Gas Price Prediction

Purpose/Objective:
Build a Prophet model to predict a forecast of the daily Ethereum gas price based on historical data.
Compare the forecasted values to the actual values in a simulated forecast.

# Technical Approach:

Leverage on year of historical Ethereum gas prices sampled as daily last values
Split historical data into training and test datasets using 80/20.
Conduct an initial data exploration to discover general trends and fluctuations.
Fit a model using Prophet using default and tuned hyperparameters.
Make a future dataset for the prediction forecasts based on a 7-day rolling window.
Analyze the predictions on the test data and calculate performance metrics.
Compare the forecasted values to the actual values in the simulated forecast for the time horizon.

## Technologies

Describe the technologies required to use your project such as programming languages, libraries, frameworks, and operating systems. Be sure to include the specific versions of any critical dependencies that you have used in the stable version of your project.

Python 3.7 - 3.9
Prophet
Pandas
sklearn

## Installation Guide

Clone the repo.
Navigate to local directory.
Run Jupyter notebooks:  prophet.ipynb, prophet_tuning.ipynb

## License

MIT License


---