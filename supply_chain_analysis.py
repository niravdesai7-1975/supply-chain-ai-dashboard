#!/usr/bin/env python3
"""
Supply Chain AI Use Case Analysis and Visualization Tool
This script analyzes the supply chain AI use cases and generates insights and visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class SupplyChainAnalyzer:
    def __init__(self):
        self.data = None
        self.load_sample_data()
    
    def load_sample_data(self):
        """Load sample data based on the provided use case information"""
        data = {
            'use_case_name': [
                'Cost optimization', 'Risk Identification', 'Supply chain Visualization',
                'Supply chain optimization', 'Demand Forecasting', 'Inventory Optimization',
                'Transportation & Routing', 'Vendor selection / Purchasing price forecasting',
                'AI Assisted Demand forecasting', 'AI led Supplier Risk Prediction',
                'Cost Modelling & Scenario Planning', 'Inventory Management',
                'Demand / Supply Balancing', 'Realtime routing & Space allocation',
                'Realtime order track & trace', 'Carbon footprint reduction',
                'Supplier Quality Analytics', 'Supplier collaboration', 'Supplier onboarding',
                'Supplier verification', 'Inventory classification', 'Shipment data analysis',
                'Material staging automation', 'Material receiving process automation',
                'MRP Documentation', 'MRP Data accuracy', 'Order quantity management',
                'Configuration setting', 'Demand Planning', 'AI powered digitization of shipment documents'
            ],
            'sector': [
                'Common', 'Automotive', 'Common', 'Industrial', 'Industrial', 'Industrial',
                'Industrial', 'Industrial', 'Common', 'Common', 'Common', 'Common',
                'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common',
                'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common',
                'Common', 'Common', 'Common'
            ],
            'category': [
                'Cost Optimization', 'Risk Management', 'Supply Chain Visualization',
                'Supply Chain Optimization', 'Demand Forecasting', 'Inventory Optimization',
                'Transportation & Routing', 'Supplier Management', 'Demand Forecasting',
                'Risk Management', 'Cost Optimization', 'Inventory Management',
                'Demand Forecasting', 'Transportation & Routing', 'Supply Chain Visualization',
                'Sustainability', 'Supplier Management', 'Supplier Management', 'Supplier Management',
                'Supplier Management', 'Inventory Management', 'Supply Chain Visualization',
                'Process Automation', 'Process Automation', 'Process Automation', 'Process Automation',
                'Inventory Management', 'Process Automation', 'Demand Forecasting', 'Process Automation'
            ],
            'persona': [
                'Supply Chain Cost Optimization', 'Risk Manager', 'Supply Chain Control Tower',
                'Planning Engineer', 'Sales & Planning Engineers', 'Planning / Inventory Managers',
                'Logistics Manager', 'Purchasing Manager', 'Procurement Team', 'Procurement Team',
                'Procurement Team', 'Procurement Team', 'Procurement Team', 'Warehouse Manager',
                'Procurement Team', 'ESG Program Manager', 'Procurement Team', 'Supplier',
                'Procurement Team', 'Procurement Team', 'Sales Engineer', 'Procurement Team',
                'Warehouse Manager', 'Warehouse Manager', 'Procurement Team', 'Procurement Team',
                'Procurement Team', 'Procurement Team', 'Procurement Team', 'Shipping Manager'
            ],
            'business_impact': [
                5, 5, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4
            ],
            'implementation_complexity': [
                3, 4, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 3, 2, 3, 3, 2, 4, 2, 2, 2, 3, 3, 2, 3, 2, 3, 2
            ],
            'estimated_roi': [
                25.0, 30.0, 20.0, 25.0, 35.0, 25.0, 20.0, 30.0, 25.0, 30.0, 25.0, 25.0, 25.0, 20.0, 20.0, 10.0, 25.0, 20.0, 30.0, 20.0, 20.0, 20.0, 25.0, 25.0, 20.0, 25.0, 20.0, 25.0, 20.0
            ],
            'implementation_timeline': [
                6, 8, 12, 10, 6, 4, 5, 7, 6, 8, 5, 6, 7, 10, 4, 8, 6, 5, 7, 4, 3, 3, 6, 5, 4, 6, 5, 6, 4
            ],
            'risk_level': [
                'Medium', 'High', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'High', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'Medium', 'Low', 'Low', 'Low'
            ]
        }
        
        self.data = pd.DataFrame(data)
        self.calculate_priority_scores()
    
    def calculate_priority_scores(self):
        """Calculate priority scores based on business impact, ROI, timeline, and risk"""
        def calculate_score(row):
            # Business impact factor (40%)
            impact_factor = row['business_impact'] * 0.4
            
            # ROI factor (30%) - normalize ROI to 1-5 scale
            roi_factor = (row['estimated_roi'] / 35.0) * 5 * 0.3
            
            # Timeline factor (20%) - shorter timeline gets higher score
            timeline_factor = ((12 - row['implementation_timeline']) / 12) * 5 * 0.2
            
            # Risk factor (10%) - lower risk gets higher score
            risk_scores = {'Low': 5, 'Medium': 3, 'High': 1}
            risk_factor = risk_scores[row['risk_level']] * 0.1
            
            return round(impact_factor + roi_factor + timeline_factor + risk_factor, 2)
        
        self.data['priority_score'] = self.data.apply(calculate_score, axis=1)
    
    def generate_summary_statistics(self):
        """Generate summary statistics for the use cases"""
        print("=== SUPPLY CHAIN AI USE CASE ANALYSIS ===\n")
        
        print(f"Total Use Cases: {len(self.data)}")
        print(f"Average Priority Score: {self.data['priority_score'].mean():.2f}")
        print(f"Average Business Impact: {self.data['business_impact'].mean():.1f}")
        print(f"Average Implementation Complexity: {self.data['implementation_complexity'].mean():.1f}")
        print(f"Average Estimated ROI: {self.data['estimated_roi'].mean():.1f}%")
        print(f"Average Implementation Timeline: {self.data['implementation_timeline'].mean():.1f} months")
        
        print(f"\nSector Distribution:")
        print(self.data['sector'].value_counts())
        
        print(f"\nCategory Distribution:")
        print(self.data['category'].value_counts())
        
        print(f"\nRisk Level Distribution:")
        print(self.data['risk_level'].value_counts())
    
    def generate_priority_analysis(self):
        """Analyze and display priority-based insights"""
        print("\n=== PRIORITY ANALYSIS ===\n")
        
        # Top 10 use cases by priority
        top_10 = self.data.nlargest(10, 'priority_score')
        print("Top 10 Use Cases by Priority Score:")
        for idx, row in top_10.iterrows():
            print(f"{row['priority_score']:.2f} - {row['use_case_name']}")
        
        # Priority distribution
        print(f"\nPriority Score Distribution:")
        print(f"High Priority (4.5-5.0): {len(self.data[self.data['priority_score'] >= 4.5])}")
        print(f"Medium Priority (4.0-4.4): {len(self.data[self.data['priority_score'] >= 4.0])}")
        print(f"Lower Priority (<4.0): {len(self.data[self.data['priority_score'] < 4.0])}")
    
    def generate_sector_analysis(self):
        """Analyze use cases by sector"""
        print("\n=== SECTOR ANALYSIS ===\n")
        
        sector_stats = self.data.groupby('sector').agg({
            'priority_score': ['mean', 'count'],
            'business_impact': 'mean',
            'estimated_roi': 'mean',
            'implementation_timeline': 'mean'
        }).round(2)
        
        print("Sector Performance Summary:")
        print(sector_stats)
    
    def generate_category_analysis(self):
        """Analyze use cases by category"""
        print("\n=== CATEGORY ANALYSIS ===\n")
        
        category_stats = self.data.groupby('category').agg({
            'priority_score': ['mean', 'count'],
            'business_impact': 'mean',
            'estimated_roi': 'mean',
            'implementation_complexity': 'mean'
        }).round(2)
        
        print("Category Performance Summary:")
        print(category_stats)
    
    def create_visualizations(self):
        """Create various visualizations for the analysis"""
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))
        fig.suptitle('Supply Chain AI Use Case Analysis Dashboard', fontsize=16, fontweight='bold')
        
        # 1. Priority Score Distribution
        axes[0, 0].hist(self.data['priority_score'], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Priority Score Distribution')
        axes[0, 0].set_xlabel('Priority Score')
        axes[0, 0].set_ylabel('Frequency')
        
        # 2. Business Impact vs Implementation Complexity
        scatter = axes[0, 1].scatter(self.data['implementation_complexity'], self.data['business_impact'], 
                                    c=self.data['priority_score'], cmap='viridis', s=100, alpha=0.7)
        axes[0, 1].set_title('Business Impact vs Implementation Complexity')
        axes[0, 1].set_xlabel('Implementation Complexity')
        axes[0, 1].set_ylabel('Business Impact')
        plt.colorbar(scatter, ax=axes[0, 1], label='Priority Score')
        
        # 3. ROI vs Timeline
        axes[0, 2].scatter(self.data['implementation_timeline'], self.data['estimated_roi'], 
                           c=self.data['priority_score'], cmap='plasma', s=100, alpha=0.7)
        axes[0, 2].set_title('ROI vs Implementation Timeline')
        axes[0, 2].set_xlabel('Implementation Timeline (months)')
        axes[0, 2].set_ylabel('Estimated ROI (%)')
        
        # 4. Sector Performance
        sector_priority = self.data.groupby('sector')['priority_score'].mean().sort_values(ascending=True)
        axes[1, 0].barh(sector_priority.index, sector_priority.values, color='lightcoral')
        axes[1, 0].set_title('Average Priority Score by Sector')
        axes[1, 0].set_xlabel('Average Priority Score')
        
        # 5. Category Performance
        category_priority = self.data.groupby('category')['priority_score'].mean().sort_values(ascending=True)
        axes[1, 1].barh(category_priority.index, category_priority.values, color='lightgreen')
        axes[1, 1].set_title('Average Priority Score by Category')
        axes[1, 1].set_xlabel('Average Priority Score')
        
        # 6. Risk Level Analysis
        risk_priority = self.data.groupby('risk_level')['priority_score'].mean().sort_values(ascending=True)
        axes[1, 2].bar(risk_priority.index, risk_priority.values, color='gold')
        axes[1, 2].set_title('Average Priority Score by Risk Level')
        axes[1, 2].set_ylabel('Average Priority Score')
        
        plt.tight_layout()
        plt.savefig('supply_chain_analysis_dashboard.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_implementation_roadmap(self):
        """Generate implementation roadmap recommendations"""
        print("\n=== IMPLEMENTATION ROADMAP RECOMMENDATIONS ===\n")
        
        # Phase 1: Quick Wins (Months 1-6)
        phase1 = self.data[
            (self.data['implementation_timeline'] <= 6) & 
            (self.data['priority_score'] >= 4.0) &
            (self.data['risk_level'] == 'Low')
        ].sort_values('priority_score', ascending=False)
        
        print("Phase 1: Quick Wins (Months 1-6)")
        print("Focus: Low-risk, high-impact implementations")
        for idx, row in phase1.iterrows():
            print(f"  • {row['use_case_name']} (Priority: {row['priority_score']:.2f}, Timeline: {row['implementation_timeline']} months)")
        
        # Phase 2: Core Capabilities (Months 7-18)
        phase2 = self.data[
            (self.data['implementation_timeline'] > 6) & 
            (self.data['implementation_timeline'] <= 18) &
            (self.data['priority_score'] >= 4.0)
        ].sort_values('priority_score', ascending=False)
        
        print(f"\nPhase 2: Core Capabilities (Months 7-18)")
        print("Focus: Building comprehensive AI capabilities")
        for idx, row in phase2.iterrows():
            print(f"  • {row['use_case_name']} (Priority: {row['priority_score']:.2f}, Timeline: {row['implementation_timeline']} months)")
        
        # Phase 3: Advanced Features (Months 19+)
        phase3 = self.data[
            (self.data['implementation_timeline'] > 18) |
            (self.data['priority_score'] < 4.0)
        ].sort_values('priority_score', ascending=False)
        
        print(f"\nPhase 3: Advanced Features (Months 19+)")
        print("Focus: Innovation and competitive advantage")
        for idx, row in phase3.iterrows():
            print(f"  • {row['use_case_name']} (Priority: {row['priority_score']:.2f}, Timeline: {row['implementation_timeline']} months)")
    
    def export_recommendations(self):
        """Export analysis results and recommendations to CSV"""
        # Export main data with priority scores
        self.data.to_csv('supply_chain_use_cases_with_priorities.csv', index=False)
        
        # Export top priority use cases
        top_priority = self.data.nlargest(15, 'priority_score')
        top_priority.to_csv('top_priority_use_cases.csv', index=False)
        
        # Export implementation roadmap
        roadmap_data = []
        for idx, row in self.data.iterrows():
            if row['implementation_timeline'] <= 6 and row['priority_score'] >= 4.0 and row['risk_level'] == 'Low':
                phase = 'Phase 1: Quick Wins'
            elif row['implementation_timeline'] <= 18 and row['priority_score'] >= 4.0:
                phase = 'Phase 2: Core Capabilities'
            else:
                phase = 'Phase 3: Advanced Features'
            
            roadmap_data.append({
                'use_case_name': row['use_case_name'],
                'phase': phase,
                'priority_score': row['priority_score'],
                'business_impact': row['business_impact'],
                'implementation_complexity': row['implementation_complexity'],
                'estimated_roi': row['estimated_roi'],
                'implementation_timeline': row['implementation_timeline'],
                'risk_level': row['risk_level']
            })
        
        roadmap_df = pd.DataFrame(roadmap_data)
        roadmap_df.to_csv('implementation_roadmap.csv', index=False)
        
        print("\n=== EXPORT COMPLETED ===")
        print("Files exported:")
        print("  • supply_chain_use_cases_with_priorities.csv")
        print("  • top_priority_use_cases.csv")
        print("  • implementation_roadmap.csv")

def main():
    """Main function to run the analysis"""
    analyzer = SupplyChainAnalyzer()
    
    # Generate comprehensive analysis
    analyzer.generate_summary_statistics()
    analyzer.generate_priority_analysis()
    analyzer.generate_sector_analysis()
    analyzer.generate_category_analysis()
    analyzer.generate_implementation_roadmap()
    
    # Create visualizations
    analyzer.create_visualizations()
    
    # Export results
    analyzer.export_recommendations()
    
    print("\n=== ANALYSIS COMPLETE ===")
    print("Check the generated files and dashboard for detailed insights.")

if __name__ == "__main__":
    main()
