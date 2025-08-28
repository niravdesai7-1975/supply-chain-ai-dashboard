#!/usr/bin/env python3
"""
Test script to debug the data loading issue
"""

import pandas as pd

def test_data():
    """Test the data structure"""
    # Create data with exactly 29 elements in each array
    data = {
        'use_case_name': [
            'Cost optimization', 'Risk Identification', 'Supply chain Visualization',
            'Supply chain optimization', 'Demand Forecasting', 'Inventory Optimization',
            'Transportation & Routing', 'Logistics Documents', 'Vendor selection',
            'Subcontracting', 'Route Optimizer', 'Spare part replacement', 'Demand Forecasting',
            'Supplier Performance', 'Supplier Sourcing', 'AI Assisted Demand forecasting',
            'Demand Planning using AI', 'AI led Supplier Risk Prediction', 'Cost Modelling',
            'Inventory Management', 'Demand / Supply Balancing', 'Realtime routing',
            'Realtime order track & trace', 'Carbon footprint reduction', 'Supplier Quality Analytics',
            'Supplier collaboration', 'Real-time inventory information', 'Supplier onboarding',
            'Supplier verification', 'Inventory classification'
        ],
        'sector': [
            'Common', 'Automotive', 'Common', 'Industrial', 'Industrial', 'Industrial',
            'Industrial', 'Industrial', 'Industrial', 'Industrial', 'Industrial', 'Industrial',
            'Industrial', 'Industrial', 'Common', 'Common', 'Common', 'Common', 'Common',
            'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common',
            'Common', 'Common', 'Common'
        ],
        'category': [
            'Cost Optimization', 'Risk Management', 'Supply Chain Visualization',
            'Supply Chain Optimization', 'Demand Forecasting', 'Inventory Optimization',
            'Transportation & Routing', 'Process Automation', 'Supplier Management',
            'Supplier Management', 'Transportation & Routing', 'Sales & Marketing', 'Demand Forecasting',
            'Supplier Management', 'Supplier Management', 'Demand Forecasting', 'Demand Forecasting',
            'Risk Management', 'Cost Optimization', 'Inventory Management', 'Demand Forecasting',
            'Transportation & Routing', 'Supply Chain Visualization', 'Sustainability',
            'Supplier Management', 'Supplier Management', 'Supply Chain Visualization', 'Supplier Management',
            'Supplier Management', 'Inventory Management'
        ],
        'persona': [
            'Supply Chain Cost Optimization', 'Risk Manager', 'Supply Chain Control Tower',
            'Planning Engineer', 'Sales & Planning Engineers', 'Planning / Inventory Managers',
            'Logistics Manager', 'Logistics Manager', 'Purchasing Manager',
            'Purchasing Manager', 'Supervisor', 'Sales Rep', 'General', 'General', 'General',
            'Procurement Team', 'Procurement Team', 'Procurement Team', 'Procurement Team',
            'Procurement Team', 'Procurement Team', 'Warehouse Manager', 'Procurement Team',
            'ESG Program Manager', 'Procurement Team', 'Supplier', 'Supplier', 'Procurement Team',
            'Procurement Team', 'Sales Engineer'
        ],
        'business_impact': [
            5, 5, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4
        ],
        'implementation_complexity': [
            3, 4, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2
        ],
        'estimated_roi': [
            25.0, 30.0, 20.0, 25.0, 35.0, 25.0, 20.0, 20.0, 30.0, 25.0, 20.0, 20.0, 35.0, 25.0, 25.0, 25.0, 25.0, 30.0, 25.0, 25.0, 25.0, 20.0, 20.0, 10.0, 25.0, 20.0, 20.0, 30.0, 20.0
        ],
        'implementation_timeline': [
            6, 8, 12, 10, 6, 4, 5, 4, 7, 6, 5, 4, 6, 6, 6, 6, 6, 8, 5, 6, 7, 10, 4, 8, 6, 5, 4, 7, 4
        ],
        'risk_level': [
            'Medium', 'High', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'High', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Low'
        ]
    }
    
    # Check array lengths
    print("Array lengths:")
    for key, value in data.items():
        print(f"  {key}: {len(value)}")
    
    # Check if all arrays have the same length
    lengths = [len(v) for v in data.values()]
    print(f"\nAll lengths: {lengths}")
    print(f"Unique lengths: {set(lengths)}")
    
    if len(set(lengths)) == 1:
        print("✅ All arrays have the same length!")
        
        # Create DataFrame
        df = pd.DataFrame(data)
        print(f"\n✅ Successfully created DataFrame with {len(df)} rows")
        print(f"Columns: {list(df.columns)}")
        
        # Calculate priority scores
        def calculate_score(row):
            impact_factor = row['business_impact'] * 0.4
            roi_factor = (row['estimated_roi'] / 35.0) * 5 * 0.3
            timeline_factor = ((12 - row['implementation_timeline']) / 12) * 5 * 0.2
            risk_scores = {'Low': 5, 'Medium': 3, 'High': 1}
            risk_factor = risk_scores[row['risk_level']] * 0.1
            return round(impact_factor + roi_factor + timeline_factor + risk_factor, 2)
        
        df['priority_score'] = df.apply(calculate_score, axis=1)
        print(f"Priority scores range: {df['priority_score'].min():.2f} to {df['priority_score'].max():.2f}")
        
        return df
    else:
        print("❌ Array length mismatch!")
        return None

if __name__ == "__main__":
    df = test_data()
    if df is not None:
        print("\nFirst few rows:")
        print(df.head())
