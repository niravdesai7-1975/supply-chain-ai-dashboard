#!/usr/bin/env python3
"""
Supply Chain AI Use Case Dashboard - Working Version
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Supply Chain AI Use Case Dashboard",
    page_icon="🚚",
    layout="wide"
)

@st.cache_data
def load_data():
    """Load and prepare the supply chain use case data"""
    # Create data with exactly 29 elements
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
    
    # Verify all arrays have the same length
    lengths = [len(v) for v in data.values()]
    print(f"Array lengths: {lengths}")
    
    df = pd.DataFrame(data)
    
    # Calculate priority scores
    def calculate_score(row):
        impact_factor = row['business_impact'] * 0.4
        roi_factor = (row['estimated_roi'] / 35.0) * 5 * 0.3
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
    st.markdown('<h1 style="font-size: 3rem; font-weight: bold; color: #1f77b4; text-align: center;">🚚 Supply Chain AI Use Case Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    df = load_data()
    
    st.success(f"✅ Successfully loaded {len(df)} use cases!")
    
    # Sidebar filters
    st.sidebar.header("📊 Filters")
    
    # Sector filter
    selected_sectors = st.sidebar.multiselect(
        "Select Sectors",
        options=df['sector'].unique(),
        default=df['sector'].unique()
    )
    
    # Category filter
    selected_categories = st.sidebar.multiselect(
        "Select Categories",
        options=df['category'].unique(),
        default=df['category'].unique()
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
        (df['category'].isin(selected_categories)) &
        (df['priority_category'].isin(selected_priorities)) &
        (df['risk_level'].isin(selected_risks))
    ]
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Use Cases", len(filtered_df))
    
    with col2:
        avg_priority = filtered_df['priority_score'].mean()
        st.metric("Avg Priority Score", f"{avg_priority:.2f}")
    
    with col3:
        avg_roi = filtered_df['estimated_roi'].mean()
        st.metric("Avg Estimated ROI", f"{avg_roi:.1f}%")
    
    with col4:
        avg_timeline = filtered_df['implementation_timeline'].mean()
        st.metric("Avg Timeline", f"{avg_timeline:.1f} months")
    
    # Priority distribution
    st.subheader("📈 Priority Score Distribution")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.histogram(
            filtered_df, 
            x='priority_score', 
            nbins=10,
            title="Priority Score Distribution",
            labels={'priority_score': 'Priority Score', 'count': 'Number of Use Cases'}
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        priority_counts = filtered_df['priority_category'].value_counts()
        fig = px.pie(
            values=priority_counts.values,
            names=priority_counts.index,
            title="Priority Category Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Business Impact vs Implementation Complexity
    st.subheader("🎯 Business Impact vs Implementation Complexity")
    fig = px.scatter(
        filtered_df,
        x='implementation_complexity',
        y='business_impact',
        color='priority_score',
        size='estimated_roi',
        hover_data=['use_case_name', 'sector', 'category'],
        title="Business Impact vs Implementation Complexity (Size = ROI, Color = Priority)",
        labels={
            'implementation_complexity': 'Implementation Complexity (1-5)',
            'business_impact': 'Business Impact (1-5)',
            'priority_score': 'Priority Score',
            'estimated_roi': 'Estimated ROI (%)'
        }
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Top Priority Use Cases
    st.subheader("🏆 Top Priority Use Cases")
    top_use_cases = filtered_df.nlargest(10, 'priority_score')[['use_case_name', 'priority_score', 'business_impact', 'estimated_roi', 'implementation_timeline', 'risk_level']]
    
    st.dataframe(top_use_cases, use_container_width=True)
    
    # Implementation Roadmap
    st.subheader("🗓️ Implementation Roadmap")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Phase 1: Quick Wins (Months 1-6)**")
        phase1 = filtered_df[
            (filtered_df['implementation_timeline'] <= 6) & 
            (filtered_df['priority_score'] >= 4.0) &
            (filtered_df['risk_level'] == 'Low')
        ].sort_values('priority_score', ascending=False)
        
        for idx, row in phase1.iterrows():
            st.markdown(f"• **{row['use_case_name']}** (Priority: {row['priority_score']:.2f})")
    
    with col2:
        st.markdown("**Phase 2: Core Capabilities (Months 7-18)**")
        phase2 = filtered_df[
            (filtered_df['implementation_timeline'] > 6) & 
            (filtered_df['implementation_timeline'] <= 18) &
            (filtered_df['priority_score'] >= 4.0)
        ].sort_values('priority_score', ascending=False)
        
        for idx, row in phase2.iterrows():
            st.markdown(f"• **{row['use_case_name']}** (Priority: {row['priority_score']:.2f})")
    
    with col3:
        st.markdown("**Phase 3: Advanced Features (Months 19+)**")
        phase3 = filtered_df[
            (filtered_df['implementation_timeline'] > 18) |
            (filtered_df['priority_score'] < 4.0)
        ].sort_values('priority_score', ascending=False)
        
        for idx, row in phase3.iterrows():
            st.markdown(f"• **{row['use_case_name']}** (Priority: {row['priority_score']:.2f})")
    
    # Download section
    st.subheader("📥 Download Data")
    col1, col2 = st.columns(2)
    
    with col1:
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download Filtered Data (CSV)",
            data=csv,
            file_name="supply_chain_use_cases_filtered.csv",
            mime="text/csv"
        )
    
    with col2:
        csv_all = df.to_csv(index=False)
        st.download_button(
            label="Download All Data (CSV)",
            data=csv_all,
            file_name="supply_chain_use_cases_all.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
