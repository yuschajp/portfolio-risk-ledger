import numpy as np
import pandas as pd
from datetime import datetime

class PortfolioRiskLedger:
    def __init__(self):
        # 1. Mock Book of Record (Position Array)
        self.portfolio = pd.DataFrame([
            {'security': 'AAPL', 'asset_class': 'Equity', 'sector': 'Technology', 'quantity': 5000, 'market_price': 175.00, 'beta': 1.2, 'duration': 0.0},
            {'security': 'MSFT', 'asset_class': 'Equity', 'sector': 'Technology', 'quantity': 3000, 'market_price': 420.00, 'beta': 1.1, 'duration': 0.0},
            {'security': 'JPM', 'asset_class': 'Equity', 'sector': 'Financials', 'quantity': 4500, 'market_price': 190.00, 'beta': 1.3, 'duration': 0.0},
            {'security': 'US10Y_BOND', 'asset_class': 'Fixed Income', 'sector': 'Government', 'quantity': 10000, 'market_price': 98.50, 'beta': 0.0, 'duration': 7.4},
            {'security': 'CORP_BOND', 'asset_class': 'Fixed Income', 'sector': 'Credit', 'quantity': 5000, 'market_price': 101.25, 'beta': 0.0, 'duration': 4.2}
        ])
        
        # 2. Simulated 10-day historical returns matrix for statistical VaR calculation
        np.random.seed(42)
        self.historical_returns = np.random.normal(-0.001, 0.015, size=(100, len(self.portfolio)))

    def calculate_valuations(self):
        """Vectorized calculations for portfolio market values and total exposure."""
        self.portfolio['market_value'] = self.portfolio['quantity'] * self.portfolio['market_price']
        total_portfolio_value = self.portfolio['market_value'].sum()
        self.portfolio['weight'] = self.portfolio['market_value'] / total_portfolio_value
        return total_portfolio_value

    def calculate_risk_sensitivities(self):
        """
        Calculates Key Risk Metrics:
        - Weighted Portfolio Beta
        - Dollar Value of a Basis Point (DV01) for Fixed Income
        """
        # Equity Risk
        weighted_beta = (self.portfolio['beta'] * self.portfolio['weight']).sum()
        
        # Fixed Income Risk: DV01 = Market Value * Duration * 0.0001
        self.portfolio['dv01'] = np.where(
            self.portfolio['asset_class'] == 'Fixed Income',
            self.portfolio['market_value'] * self.portfolio['duration'] * 0.0001,
            0.0
        )
        total_dv01 = self.portfolio['dv01'].sum()
        
        return weighted_beta, total_dv01

    def calculate_parametric_var(self, total_value, confidence_level=0.95):
        """Calculates historical Value at Risk (VaR) utilizing matrix math."""
        # Calculate weighted portfolio returns over historical timeline
        weights = self.portfolio['weight'].values
        portfolio_returns = np.dot(self.historical_returns, weights)
        
        # Extract volatility and calculate percentile drop
        portfolio_std = np.std(portfolio_returns)
        portfolio_mean = np.mean(portfolio_returns)
        
        # 95% Confidence maps to a standard normal z-score of ~1.645
        z_score = 1.645 if confidence_level == 0.95 else 2.33
        var_percentage = z_score * portfolio_std - portfolio_mean
        
        return total_value * var_percentage

    def generate_executive_report(self):
        """Orchestrates analytics engine and outputs clean markdown telemetry."""
        total_mv = self.calculate_valuations()
        portfolio_beta, total_dv01 = self.calculate_risk_sensitivities()
        dollar_var = self.calculate_parametric_var(total_mv, confidence_level=0.95)
        
        print(f"=========================================================")
        print(f"       QUANTITATIVE PORTFOLIO RISK REPORT                 ")
        print(f"       Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}            ")
        print(f"=========================================================")
        print(f"Total Portfolio Market Value : ${total_mv:,.2f}")
        print(f"Systemic Risk Profile (Beta) : {portfolio_beta:.2f}")
        print(f"Interest Rate Sensitivity    : DV01 = ${total_dv01:,.2f}")
        print(f"Value at Risk (95% VaR, 1D)  : ${dollar_var:,.2f}")
        print(f"---------------------------------------------------------")
        print(f"\nAsset Class Breakdowns:")
        
        breakdown = self.portfolio.groupby('asset_class')['market_value'].sum().reset_index()
        for _, row in breakdown.iterrows():
            print(f" - {row['asset_class']}: ${row['market_value']:,.2f}")
        print(f"=========================================================")

if __name__ == "__main__":
    ledger = PortfolioRiskLedger()
    ledger.generate_executive_report()
