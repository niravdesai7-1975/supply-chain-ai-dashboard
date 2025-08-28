# Temporary script to count elements in each list
use_cases = [
    'Cost optimization', 'Risk Identification', 'Supply chain Visualization',
    'Supply chain optimization', 'Demand Forecasting', 'Inventory Optimization',
    'Transportation & Routing', 'Logistics Documents', 'Vendor selection / Purchasing price forecasting & variance',
    'Subcontracting', 'Route Optimizer', 'Spare part replacement', 'Demand Forecasting',
    'Supplier Performance', 'Supplier Sourcing', 'AI Assisted Demand forecasting',
    'Demand Planning using AI', 'AI led Supplier Risk Prediction', 'Cost Modelling & Scenario Planning',
    'Inventory Management', 'Demand / Supply Balancing', 'Realtime routing & Space allocation',
    'Realtime order track & trace', 'Carbon footprint reduction', 'Supplier Quality Analytics',
    'Supplier collaboration', 'Real-time inventory information', 'Supplier onboarding',
    'Supplier verification', 'Inventory classification', 'Shipment data analysis',
    'Material staging automation', 'Material receiving process automation', 'MRP Documentation',
    'MRP Data accuracy', 'Order quantity management', 'Configuration setting', 'Demand Planning',
    'AI powered digitization of shipment documents'
]

sectors = [
    'Common', 'Automotive', 'Common', 'Industrial', 'Industrial', 'Industrial',
    'Industrial', 'Industrial', 'Industrial', 'Industrial', 'Industrial', 'Industrial',
    'Industrial', 'Industrial', 'Common', 'Common', 'Common', 'Common', 'Common',
    'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common',
    'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common'
]

categories = [
    'Cost Optimization', 'Risk Management', 'Supply Chain Visualization',
    'Supply Chain Optimization', 'Demand Forecasting', 'Inventory Optimization',
    'Transportation & Routing', 'Process Automation', 'Supplier Management',
    'Supplier Management', 'Transportation & Routing', 'Sales & Marketing', 'Demand Forecasting',
    'Supplier Management', 'Supplier Management', 'Demand Forecasting', 'Demand Forecasting',
    'Risk Management', 'Cost Optimization', 'Inventory Management', 'Demand Forecasting',
    'Transportation & Routing', 'Supply Chain Visualization', 'Sustainability',
    'Supplier Management', 'Supplier Management', 'Supply Chain Visualization', 'Supplier Management',
    'Supplier Management', 'Inventory Management', 'Supply Chain Visualization',
    'Process Automation', 'Process Automation', 'Process Automation', 'Process Automation',
    'Demand Forecasting', 'Process Automation'
]

personas = [
    'Supply Chain Cost Optimization', 'Risk Manager', 'Supply Chain Control Tower',
    'Planning Engineer', 'Sales & Planning Engineers', 'Planning / Inventory Managers',
    'Logistics Manager', 'Logistics Manager', 'Purchasing Manager',
    'Purchasing Manager', 'Supervisor', 'Sales Rep', 'General', 'General', 'General',
    'Procurement Team', 'Procurement Team', 'Procurement Team', 'Procurement Team',
    'Procurement Team', 'Procurement Team', 'Warehouse Manager', 'Procurement Team',
    'ESG Program Manager', 'Procurement Team', 'Supplier', 'Supplier', 'Procurement Team',
    'Procurement Team', 'Sales Engineer', 'Procurement Team', 'Warehouse Manager',
    'Warehouse Manager', 'Procurement Team', 'Procurement Team', 'Procurement Team',
    'Procurement Team', 'Shipping Manager'
]

business_impacts = [
    5, 5, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4
]

implementation_complexities = [
    3, 4, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 2, 3, 3, 2, 3, 2, 3, 2
]

estimated_rois = [
    25.0, 30.0, 20.0, 25.0, 35.0, 25.0, 20.0, 20.0, 30.0, 25.0, 20.0, 20.0, 35.0, 25.0, 25.0, 25.0, 25.0, 30.0, 25.0, 25.0, 25.0, 20.0, 20.0, 10.0, 25.0, 20.0, 20.0, 30.0, 20.0, 20.0, 25.0, 25.0, 20.0, 25.0, 20.0, 25.0, 20.0
]

implementation_timelines = [
    6, 8, 12, 10, 6, 4, 5, 4, 7, 6, 5, 4, 6, 6, 6, 6, 6, 8, 5, 6, 7, 10, 4, 8, 6, 5, 4, 7, 4, 3, 6, 5, 4, 6, 5, 6, 4
]

risk_levels = [
    'Medium', 'High', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'High', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'Medium', 'Low', 'Low', 'Low'
]

print(f"use_cases: {len(use_cases)}")
print(f"sectors: {len(sectors)}")
print(f"categories: {len(categories)}")
print(f"personas: {len(personas)}")
print(f"business_impacts: {len(business_impacts)}")
print(f"implementation_complexities: {len(implementation_complexities)}")
print(f"estimated_rois: {len(estimated_rois)}")
print(f"implementation_timelines: {len(implementation_timelines)}")
print(f"risk_levels: {len(risk_levels)}")
