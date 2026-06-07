# Automated Multi-Asset Portfolio Risk Ledger & Valuation Engine

A quantitative middle-office analytics pipeline engineered in Python 3.12 utilizing vectorized data arrays to calculate multi-asset exposures, fixed-income interest rate sensitivities, and historical market risk thresholds.

## Core Financial Framework & Analytics
* **Systemic Risk Modeling (Beta):** Computes a dynamic, weighted portfolio equity beta against benchmark historical vectors to assess systematic market sensitivity.
* **Interest Rate Volatility (DV01):** Implements a fixed-income pricing framework to calculate the strict Dollar Value of a Basis Point ($DV01$), measuring immediate capital exposure to parallel yield curve shifts.
* **Downside Risk Estimation (1D VaR):** Utilizes `numpy` matrix mathematics to execute a Parametric Value at Risk ($VaR$) calculation at a 95% confidence interval, mapping expected maximum threshold losses over a 24-hour trading horizon.

## Architecture & Tooling
* **Vectorized Data Arrays:** Powered by `pandas` and `numpy` to eliminate iterative looping loops and optimize high-dimensional financial array calculations.
* **Modular Pipeline Design:** Structured into distinct decoupled components (Valuation, Sensitivity, and Statistical Estimators) to allow seamless integration into enterprise relational databases or live reporting dashboards.
