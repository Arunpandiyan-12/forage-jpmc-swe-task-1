# JP Morgan Chase Software Engineering Virtual Experience - Task 1

This repository contains my solution for Task 1 of the JP Morgan Chase Software Engineering Virtual Experience. The task involves working with a simulated stock trading environment and making necessary adjustments to the provided client and server scripts.

## Task Description

The task aims to enhance a trader's dashboard by adding the functionality to monitor two historically correlated stocks and visualize when the correlation between them weakens. This information can help identify potential trade strategies.

The task involves:
- Setting up a local development environment
- Fixing the broken client datafeed script
- Implementing a chart to visualize stock correlations

## Getting Started

1. Clone the repository to your local machine.
2. Set up your local development environment by following the instructions in the provided guide.
3. Make the necessary changes in the `client3.py` script to calculate stock prices and ratios.
4. Run the server and client scripts to observe the changes in the trader's dashboard.

## Code Overview

- `client3.py`: This script contains the functions to calculate stock prices and ratios based on the provided data.
- `server3.py`: This script simulates a stock trading environment and provides data to the client.
- `client_test.py`: This script contains unit tests for the functions in `client3.py`.

## Usage

1. Run the server by executing `python server3.py` in your terminal.
2. In a separate terminal, run the client by executing `python client3.py`.
3. Observe the output of the client to see the calculated stock prices and ratios.

## Unit Tests

Unit tests are provided in the `client_test.py` script. These tests ensure that the functions in `client3.py` are working as expected. To run the tests, execute `python client_test.py`.

## Acknowledgements

This project is part of the JP Morgan Chase Software Engineering Virtual Experience provided by Forage. The code templates and task instructions were provided by JP Morgan Chase and Forage.



