-- Data import script for Supply Chain AI Use Cases

-- Insert sectors
INSERT INTO sectors (sector_name, description) VALUES
('Common', 'Use cases applicable across multiple industries'),
('Automotive', 'Automotive industry specific use cases'),
('Industrial', 'Industrial manufacturing and heavy industry use cases');

-- Insert value chains
INSERT INTO value_chains (value_chain_name, description) VALUES
('Sourcing, procurement and Supply Chain', 'End-to-end supply chain and procurement operations');

-- Insert use case categories with business impact and complexity ratings
INSERT INTO use_case_categories (category_name, description, business_impact_rating, implementation_complexity, estimated_roi_percentage) VALUES
('Cost Optimization', 'Initiatives focused on reducing costs across the supply chain', 5, 3, 25.0),
('Risk Management', 'Identifying and mitigating supply chain risks', 5, 4, 30.0),
('Supply Chain Visualization', 'Real-time tracking and control tower capabilities', 4, 4, 20.0),
('Demand Forecasting', 'AI-powered demand prediction and planning', 5, 3, 35.0),
('Inventory Optimization', 'Optimal inventory levels and reorder management', 4, 3, 25.0),
('Transportation & Routing', 'Logistics optimization and route planning', 4, 3, 20.0),
('Supplier Management', 'Vendor selection, performance, and collaboration', 4, 4, 30.0),
('Process Automation', 'Automating manual supply chain processes', 3, 2, 15.0),
('Sustainability', 'ESG and carbon footprint reduction', 3, 3, 10.0);

-- Insert personas
INSERT INTO personas (persona_name, role_description, department, decision_making_level) VALUES
('Supply Chain Cost Optimization', 'Focuses on cost reduction initiatives', 'Finance', 'Strategic'),
('Risk Manager', 'Identifies and manages supply chain risks', 'Risk Management', 'Strategic'),
('Supply Chain Control Tower', 'Monitors and controls supply chain operations', 'Operations', 'Tactical'),
('Planning Engineer', 'Optimizes supply chain planning and execution', 'Engineering', 'Tactical'),
('Sales & Planning Engineers', 'Forecasts demand and plans production', 'Sales & Planning', 'Tactical'),
('Planning / Inventory Managers', 'Manages inventory levels and policies', 'Operations', 'Tactical'),
('Logistics Manager', 'Oversees transportation and logistics', 'Logistics', 'Tactical'),
('Purchasing Manager', 'Manages supplier relationships and procurement', 'Procurement', 'Tactical'),
('Supervisor', 'Oversees warehouse and operational activities', 'Operations', 'Operational'),
('Sales Rep', 'Drives sales initiatives and customer relationships', 'Sales', 'Operational'),
('ESG Program Manager', 'Manages sustainability and ESG initiatives', 'Sustainability', 'Strategic'),
('Procurement Team', 'Executes procurement and sourcing activities', 'Procurement', 'Tactical'),
('Warehouse Manager', 'Manages warehouse operations and inventory', 'Operations', 'Tactical'),
('Supplier', 'External vendor providing goods/services', 'External', 'Operational'),
('Sales Engineer', 'Technical sales and customer support', 'Sales', 'Tactical'),
('Shipping Manager', 'Manages shipping and documentation', 'Logistics', 'Tactical'),
('General', 'General use case applicable to multiple roles', 'Cross-functional', 'Strategic');

-- Insert AI technologies
INSERT INTO ai_technologies (technology_name, technology_type, description, maturity_level, vendor_ecosystem) VALUES
('Machine Learning', 'ML', 'Predictive analytics and pattern recognition', 'Established', 'TensorFlow, PyTorch, Scikit-learn'),
('Natural Language Processing', 'NLP', 'Text analysis and document processing', 'Established', 'OpenAI, Google, Hugging Face'),
('Computer Vision', 'CV', 'Image and video analysis', 'Established', 'OpenCV, TensorFlow, PyTorch'),
('Predictive Analytics', 'ML', 'Forecasting and trend analysis', 'Established', 'SAS, IBM, Microsoft'),
('Optimization Algorithms', 'ML', 'Mathematical optimization for decision making', 'Established', 'Gurobi, CPLEX, OR-Tools'),
('Robotic Process Automation', 'RPA', 'Process automation and workflow management', 'Established', 'UiPath, Automation Anywhere, Blue Prism'),
('Internet of Things', 'IoT', 'Real-time data collection and monitoring', 'Established', 'AWS IoT, Azure IoT, Google Cloud IoT'),
('Blockchain', 'DLT', 'Secure and transparent transaction tracking', 'Emerging', 'Ethereum, Hyperledger, Corda'),
('Digital Twins', 'Simulation', 'Virtual representation of physical systems', 'Emerging', 'Siemens, GE, Microsoft'),
('Edge Computing', 'Computing', 'Localized data processing and analytics', 'Established', 'AWS Greengrass, Azure IoT Edge, Google Edge TPU');

-- Insert use cases with priority scores and risk levels
INSERT INTO use_cases (use_case_name, sector_id, value_chain_id, category_id, persona_id, description, business_objective, key_benefits, success_metrics, implementation_timeline_months, estimated_budget_range, risk_level, priority_score, status) VALUES
('Cost optimization', 1, 1, 1, 1, 'Generate scenarios by analyzing trends and suggest cost optimization initiatives.', 'Reduce supply chain costs', 'Cost reduction, Improved efficiency', 'Cost savings %, Efficiency improvement %', 6, '$100K-$500K', 'Medium', 4.8, 'Proposed'),
('Risk Identification', 2, 1, 2, 2, 'Predicts risks to highlight shortages and other risks factoring global trends and scenarios. Ex: Sourcing of rare earth materials used in exhaust components', 'Identify and mitigate supply chain risks', 'Risk reduction, Proactive planning', 'Risk incidents reduced, Response time improvement', 8, '$200K-$800K', 'High', 4.9, 'Proposed'),
('Supply chain Visualization', 1, 1, 3, 3, 'Realtime tracking of supply chain elements and generate next steps, predict failures and suggest corrective actions etc', 'Real-time supply chain visibility', 'Improved visibility, Faster response', 'Visibility improvement %, Response time reduction', 12, '$500K-$1.5M', 'Medium', 4.5, 'Proposed'),
('Supply chain optimization', 3, 1, 1, 4, 'Identify the optimal network configuration; Increase supply chain visibility to make faster, more informed decisions', 'Optimize supply chain network', 'Cost reduction, Improved efficiency', 'Cost savings %, Efficiency improvement %', 10, '$300K-$1M', 'Medium', 4.6, 'Proposed'),
('Demand Forecasting', 3, 1, 4, 5, 'Forecast demand with high precision for optimized inventory levels, reduced stockouts, and enhanced customer satisfaction', 'Improve demand prediction accuracy', 'Better planning, Reduced stockouts', 'Forecast accuracy %, Stockout reduction %', 6, '$150K-$600K', 'Low', 4.7, 'Proposed'),
('Inventory Optimization', 3, 1, 5, 6, 'Determine optimal inventory levels and reorder points', 'Optimize inventory management', 'Reduced carrying costs, Better service levels', 'Inventory turnover ratio, Service level improvement', 4, '$100K-$400K', 'Low', 4.4, 'Proposed'),
('Transportation & Routing', 3, 1, 6, 7, 'Identify the most efficient transportation routes and schedules; dynamically adjust to changes in demand or disruptions', 'Optimize transportation efficiency', 'Cost reduction, Improved delivery times', 'Transportation cost reduction %, Delivery time improvement', 5, '$200K-$700K', 'Medium', 4.3, 'Proposed'),
('Vendor selection / Purchasing price forecasting & variance', 3, 1, 7, 8, 'Predict material prices; optimize sourcing strategies and cost estimations', 'Optimize sourcing decisions', 'Cost reduction, Better supplier selection', 'Cost savings %, Supplier performance improvement', 7, '$250K-$800K', 'Medium', 4.5, 'Proposed'),
('AI Assisted Demand forecasting', 1, 1, 4, 12, 'Using ML for demand forecasting with inputs from Sales Plan, Market Data, Consumption patterns', 'Improve demand forecasting accuracy', 'Better planning, Reduced uncertainty', 'Forecast accuracy %, Planning efficiency improvement', 6, '$200K-$700K', 'Low', 4.6, 'Proposed'),
('AI led Supplier Risk Prediction', 1, 1, 2, 12, 'Critical Supplier process parameters are monitored and suppliers with high risk are identified for proactive actions reducing impact of shortage / delayed delivery on manufacturing operations', 'Proactive supplier risk management', 'Risk reduction, Supply continuity', 'Risk incidents reduced, Supply disruption reduction', 8, '$300K-$1M', 'High', 4.8, 'Proposed'),
('Cost Modelling & Scenario Planning', 1, 1, 1, 12, 'The Prices of Commodity are forecasted using historical data and factors impacting', 'Improve cost forecasting accuracy', 'Better cost planning, Scenario analysis', 'Cost forecast accuracy %, Scenario planning efficiency', 5, '$150K-$500K', 'Medium', 4.4, 'Proposed'),
('Inventory Management', 1, 1, 5, 12, 'The trick with inventory planning is to order just the right amount of product to satisfy customer demand while avoiding overstock or out-of-stock issues. AI solutions can constantly rebalance demand and supply by automatically analysing all available data and constraints.', 'Optimize inventory planning', 'Reduced costs, Better service levels', 'Inventory turnover ratio, Service level improvement', 6, '$200K-$600K', 'Low', 4.5, 'Proposed'),
('Demand / Supply Balancing', 1, 1, 4, 12, 'Monitor Stage wise product movement to identify bottleneck points, define inventory policies and enhance customer satisfaction', 'Balance demand and supply', 'Improved efficiency, Better customer service', 'Efficiency improvement %, Customer satisfaction improvement', 7, '$250K-$700K', 'Medium', 4.3, 'Proposed'),
('Realtime routing & Space allocation', 1, 1, 6, 13, 'Use of AGV''s to move parts from warehouse to assembly station to streamline material movement and reduce downtime.', 'Optimize material movement', 'Reduced downtime, Improved efficiency', 'Downtime reduction %, Efficiency improvement %', 10, '$400K-$1.2M', 'Medium', 4.2, 'Proposed'),
('Realtime order track & trace', 1, 1, 3, 12, 'AI-driven real-time tracking and visibility solutions are poised to improve operations and customer satisfaction by providing accurate, up-to-date information on shipment status and location', 'Improve order visibility', 'Better customer service, Operational efficiency', 'Customer satisfaction improvement, Response time reduction', 4, '$150K-$500K', 'Low', 4.4, 'Proposed'),
('Carbon footprint reduction', 1, 1, 9, 11, 'AI can assess env impact of SC operations and suggest ways to minimize carbon footprint to align with sustainability goals and regulatory requirements', 'Reduce environmental impact', 'Sustainability compliance, Cost savings', 'Carbon footprint reduction %, Compliance improvement', 8, '$200K-$800K', 'Medium', 4.1, 'Proposed'),
('Supplier Quality Analytics', 1, 1, 7, 12, 'Using various organizational parameters and ML to understand and predict supplier performance', 'Improve supplier performance', 'Better quality, Reduced risks', 'Quality improvement %, Risk reduction %', 6, '$200K-$600K', 'Medium', 4.3, 'Proposed'),
('Supplier collaboration', 1, 1, 7, 14, 'Facilitate intelligent collaboration with suppliers by analysing production lead times, new sales orders, and historical performance. This information can be used to optimize JIT inventory strategies.', 'Improve supplier collaboration', 'Better coordination, Reduced inventory', 'Collaboration efficiency %, Inventory reduction %', 5, '$150K-$500K', 'Low', 4.2, 'Proposed'),
('Supplier onboarding', 1, 1, 7, 12, 'Automated supplier onboarding process, by analysing compliance requirements and verifying documentation. Analyse contract terms and conditions, identify potential risks, recommend optimizations and use this for better contract term negotiations, contract management, ensure compliance. Analyse market conditions, historical pricing data, negotiation strategies to suggest insights during supplier negotiations', 'Streamline supplier onboarding', 'Faster onboarding, Better compliance', 'Onboarding time reduction %, Compliance improvement %', 7, '$200K-$700K', 'Medium', 4.4, 'Proposed'),
('Supplier verification', 1, 1, 7, 12, 'Automate the verification of supplier invoices by analysing invoice data against purchase orders and delivery receipts within SAP. This reduces risk of errors, accelerates invoice processing and enhances financial transparency.', 'Automate invoice verification', 'Reduced errors, Faster processing', 'Error reduction %, Processing time improvement', 4, '$100K-$400K', 'Low', 4.1, 'Proposed'),
('Inventory classification', 1, 1, 5, 15, 'Automate items classification through ABC analysis, studying historical data, improve inventory management efforts. Analyse historical sales data and inventory turnover rates to identify dead stock. This information can help make informed decisions on discounts, promotions, or write-offs.', 'Automate inventory classification', 'Better inventory management, Reduced dead stock', 'Classification accuracy %, Dead stock reduction %', 3, '$80K-$300K', 'Low', 4.0, 'Proposed'),
('Shipment data analysis', 1, 1, 3, 12, 'Analyse incoming advanced shipment notifications to extract relevant information like shipment details, expected quantities, and delivery schedules, streamlining the overall process.', 'Streamline shipment processing', 'Faster processing, Better accuracy', 'Processing time reduction %, Accuracy improvement %', 3, '$100K-$350K', 'Low', 4.0, 'Proposed'),
('Material staging automation', 1, 1, 8, 13, 'Automate material staging by analysing kit orders, component availability, and production schedules to ensure right set of materials are ready for the production process.', 'Automate material staging', 'Reduced errors, Improved efficiency', 'Error reduction %, Efficiency improvement %', 6, '$200K-$600K', 'Medium', 4.2, 'Proposed'),
('Material receiving process automation', 1, 1, 8, 13, 'Automate the identification and resolution of exceptions during receiving process. Update the systems for materials receipt within SAP for transparency, and reduce manual entry errors.', 'Automate receiving process', 'Reduced errors, Faster processing', 'Error reduction %, Processing time improvement', 5, '$150K-$500K', 'Medium', 4.1, 'Proposed'),
('MRP Documentation', 1, 1, 8, 12, 'Proactive Gen AI based user-friendly documentation to understand MRP errors. Insights generation analysing common pitfalls, error patterns, and scope for improvement', 'Improve MRP documentation', 'Better understanding, Reduced errors', 'Documentation quality improvement, Error reduction %', 4, '$100K-$400K', 'Low', 4.0, 'Proposed'),
('MRP Data accuracy', 1, 1, 8, 12, 'Intelligent data integrity check by analysing bill of materials, material master records, and work center data. Ensure data elements are complete, accurate, and consistent.', 'Improve data accuracy', 'Better data quality, Reduced errors', 'Data accuracy improvement %, Error reduction %', 6, '$200K-$600K', 'Medium', 4.3, 'Proposed'),
('Order quantity management', 1, 1, 5, 12, 'Insights generated based on safety stock levels, reorder points, and lead times, based on real-time demand insights', 'Optimize order quantities', 'Better inventory management, Reduced costs', 'Cost reduction %, Service level improvement', 4, '$120K-$400K', 'Low', 4.1, 'Proposed'),
('Configuration setting', 1, 1, 8, 12, 'Analyse SAP''s system configuration settings related to MRP, checks based on parameters like planning horizon, MRP groups. Ensure specific configuration to requirements like Made-to-stock.', 'Optimize system configuration', 'Better performance, Reduced errors', 'Performance improvement %, Error reduction %', 5, '$150K-$500K', 'Medium', 4.0, 'Proposed'),
('Demand Planning', 1, 1, 4, 12, 'Predict future demand variations by analysing planned vs actual demand within SAP.', 'Improve demand planning', 'Better forecasting, Reduced uncertainty', 'Forecast accuracy %, Planning efficiency improvement', 6, '$200K-$600K', 'Low', 4.2, 'Proposed'),
('AI powered digitization of shipment documents', 1, 1, 8, 16, 'AI can be leverage to simplify Cumbersome physical document retrieval process from data storage to address the shipment related queries', 'Digitize shipment documents', 'Faster retrieval, Better accessibility', 'Retrieval time reduction %, Accessibility improvement %', 4, '$100K-$400K', 'Low', 4.0, 'Proposed');

-- Insert technology mappings for key use cases
INSERT INTO use_case_technologies (use_case_id, technology_id, technology_role, implementation_notes) VALUES
(1, 1, 'Primary', 'ML models for trend analysis and cost optimization scenarios'),
(1, 4, 'Secondary', 'Predictive analytics for cost forecasting'),
(2, 1, 'Primary', 'ML models for risk prediction and trend analysis'),
(2, 4, 'Secondary', 'Predictive analytics for risk assessment'),
(3, 7, 'Primary', 'IoT sensors for real-time tracking'),
(3, 1, 'Secondary', 'ML for failure prediction and corrective actions'),
(4, 5, 'Primary', 'Optimization algorithms for network configuration'),
(4, 1, 'Secondary', 'ML for decision support'),
(5, 1, 'Primary', 'ML models for demand forecasting'),
(5, 4, 'Secondary', 'Predictive analytics for trend analysis'),
(6, 5, 'Primary', 'Optimization algorithms for inventory levels'),
(6, 1, 'Secondary', 'ML for demand prediction'),
(7, 5, 'Primary', 'Optimization algorithms for route planning'),
(7, 7, 'Secondary', 'IoT for real-time traffic and condition data'),
(8, 1, 'Primary', 'ML for price forecasting'),
(8, 4, 'Secondary', 'Predictive analytics for market trends'),
(9, 1, 'Primary', 'ML models for demand forecasting'),
(9, 4, 'Secondary', 'Predictive analytics for sales planning'),
(10, 1, 'Primary', 'ML for supplier risk prediction'),
(10, 4, 'Secondary', 'Predictive analytics for risk assessment');
