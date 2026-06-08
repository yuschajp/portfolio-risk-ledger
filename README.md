# Automated Multi-Asset Portfolio Risk Ledger & Valuation Engine

A quantitative middle-office analytics pipeline engineered in Python 3.12 utilizing vectorized data arrays to calculate multi-asset exposures, fixed-income interest rate sensitivities, and historical market risk thresholds.

## Core Financial Framework & Analytics
* **Systemic Risk Modeling (Beta):** Computes a dynamic, weighted portfolio equity beta against benchmark historical vectors to assess systematic market sensitivity.
* **Interest Rate Volatility (DV01):** Implements a fixed-income pricing framework to calculate the strict Dollar Value of a Basis Point ($DV01$), measuring immediate capital exposure to parallel yield curve shifts.
* **Downside Risk Estimation (1D VaR):** Utilizes `numpy` matrix mathematics to execute a Parametric Value at Risk ($VaR$) calculation at a 95% confidence interval, mapping expected maximum threshold losses over a 24-hour trading horizon.

## Architecture & Tooling
* **Vectorized Data Arrays:** Powered by `pandas` and `numpy` to eliminate iterative looping loops and optimize high-dimensional financial array calculations.
* **Modular Pipeline Design:** Structured into distinct decoupled components (Valuation, Sensitivity, and Statistical Estimators) to allow seamless integration into enterprise relational databases or live reporting dashboards.

A high-performance, event-driven trade simulator engineered to model concurrent institutional execution gateways, enforce thread-safe multi-threaded order processing, and maintain real-time pre-trade risk thresholds.

## 💡 Business Context & Impact
In institutional execution environments, electronic trading desks process a continuous influx of concurrent orders across multiple asset classes. If the system's infrastructure cannot handle high-concurrency safely, data race conditions can occur. This leads to inaccurate risk tracking, unauthorized capital exposure, or breaches of regulatory risk limits. 

This project implements a **Modern Core Infrastructure approach**: utilizing asynchronous execution gateways and robust mutual exclusion locks (`threading.Lock`) to ensure that real-time portfolio balance and risk limits are validated deterministically before an order is safely routed to an exchange gateway.

## 🏗️ Core Engine Architecture

```mermaid
graph TD
    %% Define Styles
    classDef source fill:#f9f9f9,stroke:#333,stroke-width:1px;
    classDef pipeline fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef math fill:#fff3e0,stroke:#f57c00,stroke-width:2px;
    classDef report fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;

    %% Workflow Nodes
    A[Raw Book of Record / Multi-Asset Position Data] --> B(Data Ingestion Pipeline)
    
    subgraph "Data Transformation Layer"
        B --> C[Pandas DataFrame Cleaning & Alignment]
        C --> D[Map Security Master Reference Data]
    end
    
    D --> E[Vectorized Mathematical Analytics Engine]
    
    subgraph "Quantitative Core (NumPy & Matrix Math)"
        E --> F{Asset Class Routing}
        
        F -- Fixed Income --> G[Yield Curve Tracking Engine]
        G --> H["Calculate Absolute Dollar Value of a Basis Point (DV01)"]
        
        F -- Equities / Blended --> I[Historical Returns Covariance Matrix]
        I --> J["Compute 1-Day Historical Value at Risk (VaR) @ 95% CI"]
    end
    
    H --> K(Consolidate Risk Metrics)
    J --> K
    
    subgraph "Output Analytics Layer"
        K --> L[Generate Systemic Portfolio Risk Report]
        L --> M[(Export CSV / JSON Risk Ledger State)]
    end

    %% Apply Styles
    class A source;
    class B,C,D pipeline;
    class E,F,G,H,I,J math;
    class K,L,M report;
