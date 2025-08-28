import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Manufacturing AI Use Case Dashboard",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .priority-high { color: #d62728; font-weight: bold; }
    .priority-medium { color: #ff7f0e; font-weight: bold; }
    .priority-low { color: #2ca02c; font-weight: bold; }
    .sector-common { color: #1f77b4; font-weight: bold; }
    .sector-automotive { color: #ff7f0e; font-weight: bold; }
    .sector-industrial { color: #2ca02c; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_manufacturing_data():
    """Load and prepare the manufacturing AI use case data"""
    
    use_cases = [
        'Raw Material Management', 'Press Shop- Tool Maintenance', 'Production scheduling',
        'Production scheduling', 'Production scheduling', 'Production scheduling',
        'Maintenance scheduling functions', 'Part quality deterioration parameters',
        'Quality Assistant', 'Audit Assistant', 'Production Planning & Scheduling',
        'Manufacturing Execution Alerts', 'Production Execution Documentation',
        'Defect Management', 'Production Planning & Scheduling', 'Predictive Maintenance',
        'Knowledge Management', 'Production Planning / Capacity Optimization',
        'Quality Assurance', 'Quality Control', 'Predictive Maintenance',
        'Digital Command Tower', 'Warranty Analytics', 'Warranty Forecasting',
        'Knowledge Management / SOP Creation', 'Energy management / Sustainability',
        'Production timeline predictor', 'Production sequence optimiser',
        'Production timeline predictor'
    ]
    
    sectors = [
        'Common', 'Automotive', 'Common', 'Manufacturing', 'Manufacturing', 'Manufacturing',
        'Common', 'Common', 'Common', 'Common', 'Industrial', 'Industrial', 'Industrial',
        'Industrial', 'Industrial', 'Industrial', 'Industrial', 'Common', 'Common', 'Common',
        'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common'
    ]
    
    value_chains = [
        'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing',
        'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing',
        'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing',
        'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing',
        'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing', 'Manufacturing'
    ]
    
    personas = [
        'Stores Manager', 'Manufacturing Engineer', 'Production Manager', 'Production Manager',
        'Production Manager', 'Production Manager', 'Plant Maintenance Manager', 'Plant Quality Manager',
        'Plant Quality Manager', 'Plant Quality Manager', 'Production Planning Engineer', 'Shopfloor Manager',
        'Production Engineer / Technician', 'Quality Engineer', 'Production & Maintenance Engineers',
        'Maintenance Engineers', 'Maintenance Engineers', 'Production Manager', 'Quality Engineer',
        'Quality Engineer', 'Production Engineer', 'Production Manager', 'Quality Analyst', 'Quality Analyst',
        'Multiple', 'Production Manager', 'Production Manager', 'Production Manager', 'Production Manager'
    ]
    
    descriptions = [
        'Consolidated or customized Report Generation and Insights- Ex: Inventory Report, Dead Stock or Non Moving items, Inventory Carrying cost, Inventory Turnover days etc',
        'Tool life estimation forecast based on multiple production schedule. Tool life- Periodic Maintenance Scheduling (smart maintenance).',
        'workforce allocation planning.',
        'OEE analysis and scenario generation for improvements',
        'Machine Layout Planning and optimization',
        'Cycle time adherence vs optimization',
        '1) Spares costs optimization plans 2) Maintenance Plan generation 3)Machine life or parts life monitoring and optimization',
        'Part quality prediction, Examine consistency levels.',
        'Assist in huge loads of documentation work which quality control department is involved. Example: Generate comprehensive quality status reports. Maintain status of all check sheets. Remainder to close any Non-Conformance raised or follow up on corrective actions etc..',
        'Collection of quality documentation to generate different customized documents to comply with ISO or other requirements Ex: Generate a Dimensions Trend chart for a product and compare with past Cpk levels',
        'Optimise production plans and schedules to ensure that resources are utilised optimally and that customer demand is met in a timely manner; facilitate rapid response to disruptions, such as equipment breakdowns or changes in demand, by generating and analysing alternate production schedules in real time',
        'Use Andon alerts to estimate and communicate information about impacts to schedule',
        'Auto generate production work instructions',
        'Identify and correct potential defects in products before they are shipped to customers; reduce waste, and eliminate recalls due to defects',
        'Predict impact of equipment downtime on production schedules and deliveries',
        'Improved predictive maintenance for reduced downtime and increased productivity',
        'GenAI to query possible failure causes, and get high-probability suggestions on equipment input adjustments, maintenance required, spare parts to purchase that will mitigate downtime',
        'Use of AI to reduce Production planning errors addressing demand with reduced lead time and increased flexibility',
        'Monitor critical to quality parameters in manufacturing process and generate alerts based on Process capability index',
        'Automated visual inspection for defects using ML & computer vision',
        'Using Digital twin of asset the production performance is monitored and maintenance calls are automatically scheduled based on sensory data acquired.',
        'Decision making close to device / asset reducing latency',
        'Perform text processing techniques to clean, standardize data for analysis Use a pre-labelled datasets for training the models Identify key categories using Supervised Classification / LLM models and NLP techniques like Topic Modelling, Summarization, Sentiment Analysis, Intent Recognition',
        'Manufacturing / Supplier critical to quality product and process parameters are monitored and its corelation is established with historical manufacturing defects occurred in field / customer end . System then predicts the future failure rates for 1 / 3 / 6 months in service products which in turn helps to have proactive recall / service campaign in case of any safety / regulatory issues.',
        'Implicit and procedural knowledge gained within organisation is difficult to organize and accessible to larger group. Gen AI based knowledge preservation to retrieve historical learnings and formulate action plan, Create SOP, Provide Guided steps to users during maintenance and troubleshooting.',
        'AI can analyze energy consumption patterns and suggest ways to optimize energy usage, leading to cost savings and env sustainability',
        'Analyse real-time production data from MES systems and predict product completion data',
        'Analyse historical production data, machine capabilities and production schedules within SAP',
        'Using ML, it predicts more accurate operation times for each step in routing. Historical performance, machine conditions, other external factors affecting the operation duration, for more realistic timelines in SAP.'
    ]
    
    # Generate synthetic metrics for analysis
    business_impacts = [
        5, 4, 4, 5, 4, 4, 5, 4, 3, 3, 5, 4, 3, 5, 5, 5, 4, 5, 4, 4, 5, 5, 4, 5, 4, 4, 5, 5, 5
    ]
    
    implementation_complexities = [
        3, 4, 3, 4, 4, 3, 4, 3, 2, 2, 4, 3, 2, 4, 4, 4, 3, 4, 3, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4
    ]
    
    estimated_rois = [
        25.0, 30.0, 20.0, 35.0, 25.0, 20.0, 40.0, 25.0, 15.0, 15.0, 35.0, 25.0, 20.0, 40.0, 35.0, 40.0, 30.0, 35.0, 25.0, 30.0, 40.0, 35.0, 30.0, 40.0, 25.0, 30.0, 35.0, 35.0, 30.0
    ]
    
    implementation_timelines = [
        6, 8, 4, 6, 8, 5, 8, 6, 3, 3, 8, 5, 4, 8, 8, 10, 6, 8, 6, 8, 10, 8, 8, 10, 6, 8, 8, 8, 6
    ]
    
    risk_levels = [
        'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Low', 'Medium', 'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Low'
    ]
    
    # Create DataFrame
    df = pd.DataFrame({
        'use_case_name': use_cases,
        'sector': sectors,
        'value_chain': value_chains,
        'persona': personas,
        'description': descriptions,
        'business_impact': business_impacts,
        'implementation_complexity': implementation_complexities,
        'estimated_roi': estimated_rois,
        'implementation_timeline': implementation_timelines,
        'risk_level': risk_levels
    })
    
    # Calculate priority scores
    def calculate_score(row):
        impact_factor = row['business_impact'] * 0.4
        roi_factor = (row['estimated_roi'] / 40.0) * 5 * 0.3
        timeline_factor = ((12 - row['implementation_timeline']) / 12) * 5 * 0.2
        risk_scores = {'Low': 5, 'Medium': 3, 'High': 1}
        risk_factor = risk_scores[row['risk_level']] * 0.1
        return round(impact_factor + roi_factor + timeline_factor + risk_factor, 2)
    
    df['priority_score'] = df.apply(calculate_score, axis=1)
    
    # Add priority category
    def get_priority_category(score):
        if score >= 4.5:
            return 'High Priority'
        elif score >= 4.0:
            return 'Medium Priority'
        else:
            return 'Lower Priority'
    
    df['priority_category'] = df['priority_score'].apply(get_priority_category)
    
    return df

def main():
    """Main dashboard function"""
    st.markdown('<h1 class="main-header">🏭 Manufacturing AI Use Case Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    df = load_manufacturing_data()
    
    # Sidebar filters
    st.sidebar.header("📊 Filters")
    
    # Sector filter
    selected_sectors = st.sidebar.multiselect(
        "Select Sectors",
        options=df['sector'].unique(),
        default=df['sector'].unique()
    )
    
    # Priority filter
    selected_priorities = st.sidebar.multiselect(
        "Select Priority Levels",
        options=df['priority_category'].unique(),
        default=df['priority_category'].unique()
    )
    
    # Risk level filter
    selected_risks = st.sidebar.multiselect(
        "Select Risk Levels",
        options=df['risk_level'].unique(),
        default=df['risk_level'].unique()
    )
    
    # Apply filters
    filtered_df = df[
        (df['sector'].isin(selected_sectors)) &
        (df['priority_category'].isin(selected_priorities)) &
        (df['risk_level'].isin(selected_risks))
    ]
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Use Cases", len(filtered_df))
    
    with col2:
        avg_roi = filtered_df['estimated_roi'].mean()
        st.metric("Average ROI", f"{avg_roi:.1f}%")
    
    with col3:
        avg_priority = filtered_df['priority_score'].mean()
        st.metric("Average Priority Score", f"{avg_priority:.2f}")
    
    with col4:
        high_priority_count = len(filtered_df[filtered_df['priority_category'] == 'High Priority'])
        st.metric("High Priority Cases", high_priority_count)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Priority distribution
        priority_counts = filtered_df['priority_category'].value_counts()
        fig_priority = px.pie(
            values=priority_counts.values,
            names=priority_counts.index,
            title="Priority Distribution",
            color_discrete_map={
                'High Priority': '#d62728',
                'Medium Priority': '#ff7f0e',
                'Lower Priority': '#2ca02c'
            }
        )
        fig_priority.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_priority, use_container_width=True)
        
        # ROI vs Implementation Timeline
        fig_scatter = px.scatter(
            filtered_df,
            x='implementation_timeline',
            y='estimated_roi',
            color='priority_category',
            size='business_impact',
            hover_data=['use_case_name'],
            title="ROI vs Implementation Timeline",
            labels={'implementation_timeline': 'Implementation Timeline (months)', 'estimated_roi': 'Estimated ROI (%)'}
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with col2:
        # Sector distribution
        sector_counts = filtered_df['sector'].value_counts()
        fig_sector = px.bar(
            x=sector_counts.index,
            y=sector_counts.values,
            title="Use Cases by Sector",
            labels={'x': 'Sector', 'y': 'Number of Use Cases'},
            color=sector_counts.index,
            color_discrete_map={
                'Common': '#1f77b4',
                'Automotive': '#ff7f0e',
                'Industrial': '#2ca02c',
                'Manufacturing': '#d62728'
            }
        )
        st.plotly_chart(fig_sector, use_container_width=True)
        
        # Risk level distribution
        risk_counts = filtered_df['risk_level'].value_counts()
        fig_risk = px.pie(
            values=risk_counts.values,
            names=risk_counts.index,
            title="Risk Level Distribution",
            color_discrete_map={
                'Low': '#2ca02c',
                'Medium': '#ff7f0e',
                'High': '#d62728'
            }
        )
        fig_risk.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_risk, use_container_width=True)
    
    # Detailed use case table
    st.subheader("📋 Detailed Use Case Analysis")
    
    # Sort by priority score
    sorted_df = filtered_df.sort_values('priority_score', ascending=False)
    
    # Display table with better formatting
    for idx, row in sorted_df.iterrows():
        with st.expander(f"🏭 {row['use_case_name']} - Priority Score: {row['priority_score']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**Description:** {row['description']}")
                st.write(f"**Sector:** {row['sector']}")
                st.write(f"**Persona:** {row['persona']}")
            
            with col2:
                st.metric("Business Impact", row['business_impact'])
                st.metric("Implementation Complexity", row['implementation_complexity'])
                st.metric("Estimated ROI", f"{row['estimated_roi']}%")
                st.metric("Timeline", f"{row['implementation_timeline']} months")
                
                # Color-coded priority and risk
                priority_color = "priority-high" if row['priority_category'] == 'High Priority' else \
                               "priority-medium" if row['priority_category'] == 'Medium Priority' else "priority-low"
                
                st.markdown(f'<p class="{priority_color}">Priority: {row["priority_category"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p>Risk Level: {row["risk_level"]}</p>', unsafe_allow_html=True)
    
    # Recommendations section
    st.subheader("💡 Strategic Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🚀 Quick Wins (High ROI, Low Complexity):**
        - Quality Assistant & Audit Assistant
        - Production Execution Documentation
        - Raw Material Management
        """)
        
        st.markdown("""
        **⚡ High Impact Projects:**
        - Predictive Maintenance
        - Defect Management
        - Production Planning & Scheduling
        """)
    
    with col2:
        st.markdown("""
        **🔧 Strategic Initiatives:**
        - Digital Command Tower
        - Knowledge Management / SOP Creation
        - Warranty Analytics & Forecasting
        """)
        
        st.markdown("""
        **📊 Focus Areas:**
        - Maintenance & Quality functions
        - Production optimization
        - Energy management & Sustainability
        """)

if __name__ == "__main__":
    main()
