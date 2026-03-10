#!/usr/bin/env python3
"""
Vaccination Coverage Analysis - Regional Disparities and Policy Insights

This script provides a comprehensive analysis of vaccination coverage data to identify:
- Under-vaccinated regions requiring immediate intervention
- Rollout inconsistencies indicating logistics/supply chain issues  
- Regional disparities with statistical significance
- Public health policy recommendations based on evidence

Author: Data Analysis Team  
Date: March 2026
"""

import pandas as pd
import numpy as np
import json
from pathlib import Path
from scipy import stats

def load_vaccination_data():
    """
    Load and prepare vaccination coverage data for analysis.
    
    Returns:
        tuple: (DataFrame, dict) - cleaned data and metadata
    """
    try:
        # Define paths
        base_path = Path(__file__).parent.parent.parent
        data_path = base_path / "data" / "processed" / "vaccination_coverage_clean.csv"
        insights_path = base_path / "data" / "processed" / "vaccination_insights.json"
        
        # Load data
        df = pd.read_csv(data_path)
        
        if insights_path.exists():
            with open(insights_path, 'r') as f:
                insights = json.load(f)
        else:
            insights = {}
            
        # Calculate composite vaccination score
        key_vaccines = ['full_vaccination_any_source', 'polio_3_doses', 'dpt_3_doses', 'measles_first_dose']
        available_vaccines = [col for col in key_vaccines if col in df.columns]
        df['composite_vaccination_score'] = df[available_vaccines].mean(axis=1)
        
        return df, insights
        
    except Exception as e:
        print(f"⚠️ Error loading data: {e}")
        print("Please ensure notebooks have been executed to generate processed data.")
        return None, None

def analyze_regional_disparities(df):
    """
    Identify and analyze regional vaccination disparities.
    
    Args:
        df (DataFrame): Vaccination coverage data
        
    Returns:
        dict: Analysis results and recommendations
    """
    results = {
        'under_vaccinated_districts': [],
        'state_performance': {},
        'statistical_significance': False
    }
    
    if df is None or 'composite_vaccination_score' not in df.columns:
        return results
        
    # Identify worst-performing districts
    worst_districts = df.nsmallest(15, 'composite_vaccination_score')
    results['under_vaccinated_districts'] = worst_districts[['district', 'state', 'composite_vaccination_score']].to_dict('records')
    
    # State-level analysis  
    state_performance = df.groupby('state')['composite_vaccination_score'].agg(['mean', 'count']).round(1)
    state_performance = state_performance[state_performance['count'] >= 3]  # Minimum districts for reliability
    results['state_performance'] = state_performance.to_dict()
    
    # Test statistical significance of state differences
    state_groups = []
    for state in state_performance.index:
        state_data = df[df['state'] == state]['composite_vaccination_score'].dropna()
        if len(state_data) >= 3:
            state_groups.append(state_data.values)
    
    if len(state_groups) >= 2:
        try:
            h_statistic, p_value = stats.kruskal(*state_groups)
            results['statistical_significance'] = p_value < 0.05
            results['kruskal_wallis'] = {'h_statistic': h_statistic, 'p_value': p_value}
        except:
            pass
            
    return results

def detect_rollout_inconsistencies(df):
    """
    Detect and quantify rollout inconsistencies across vaccine types.
    
    Args:
        df (DataFrame): Vaccination coverage data
        
    Returns:
        dict: Inconsistency analysis and affected districts
    """
    results = {
        'inconsistent_districts': [],
        'inconsistency_statistics': {},
        'districts_needing_attention': 0
    }
    
    if df is None:
        return results
        
    # Calculate coefficient of variation for each district
    key_vaccines = ['full_vaccination_any_source', 'polio_3_doses', 'dpt_3_doses', 'measles_first_dose']
    available_vaccines = [col for col in key_vaccines if col in df.columns]
    
    def calculate_cv(row):
        values = row[available_vaccines].dropna() 
        if len(values) > 1 and values.mean() > 0:
            return (values.std() / values.mean()) * 100
        return np.nan
        
    df['vaccination_cv'] = df.apply(calculate_cv, axis=1)
    
    # Statistical analysis of inconsistency
    cv_data = df['vaccination_cv'].dropna()
    if len(cv_data) > 0:
        cv_mean = cv_data.mean()
        cv_std = cv_data.std() 
        
        results['inconsistency_statistics'] = {
            'mean_cv': cv_mean,
            'std_cv': cv_std,
            'total_districts': len(cv_data)
        }
        
        # Identify highly inconsistent districts (>2 standard deviations)
        threshold = cv_mean + 2 * cv_std
        inconsistent = df[df['vaccination_cv'] > threshold].nlargest(10, 'vaccination_cv')
        results['inconsistent_districts'] = inconsistent[['district', 'state', 'vaccination_cv']].to_dict('records')
        results['districts_needing_attention'] = (df['vaccination_cv'] > threshold).sum()
        
    return results

def analyze_healthcare_delivery(df):
    """
    Analyze public vs private healthcare delivery patterns.
    
    Args:
        df (DataFrame): Vaccination coverage data
        
    Returns:
        dict: Healthcare delivery analysis
    """
    results = {
        'public_vs_private': {},
        'delivery_patterns': {},
        'recommendations': []
    }
    
    if df is None:
        return results
        
    # Analyze public vs private facility usage
    if 'vaccinations_public_facility' in df.columns and 'vaccinations_private_facility' in df.columns:
        public_data = df['vaccinations_public_facility'].dropna()
        private_data = df['vaccinations_private_facility'].dropna()
        
        if len(public_data) > 0 and len(private_data) > 0:
            results['public_vs_private'] = {
                'public_mean': public_data.mean(),
                'private_mean': private_data.mean(),
                'public_samples': len(public_data),
                'private_samples': len(private_data)
            }
            
            # Determine dominant delivery system
            public_dominant = public_data.mean() > private_data.mean()
            results['delivery_patterns']['primary_system'] = 'public' if public_dominant else 'private'
            
            # Generate recommendations
            if public_dominant:
                results['recommendations'].append("Strengthen public healthcare infrastructure")
                results['recommendations'].append("Focus resources on government health facilities")
            else:
                results['recommendations'].append("Develop public-private partnerships")
                results['recommendations'].append("Leverage private sector capacity")
                
    return results

def generate_policy_recommendations(disparity_results, inconsistency_results, delivery_results):
    """
    Generate evidence-based policy recommendations.
    
    Args:
        disparity_results (dict): Regional disparity analysis
        inconsistency_results (dict): Rollout inconsistency analysis  
        delivery_results (dict): Healthcare delivery analysis
        
    Returns:
        dict: Structured policy recommendations
    """
    recommendations = {
        'immediate_actions': [],
        'medium_term_strategies': [],
        'long_term_monitoring': [], 
        'resource_allocation_priorities': []
    }
    
    # Immediate actions based on under-vaccinated regions
    if disparity_results['under_vaccinated_districts']:
        worst_count = len(disparity_results['under_vaccinated_districts'])
        recommendations['immediate_actions'].append(f"Emergency intervention in {worst_count} worst-performing districts")
        recommendations['immediate_actions'].append("Deploy mobile vaccination units to under-served areas")
        
    # Address rollout inconsistencies  
    if inconsistency_results['districts_needing_attention'] > 0:
        inconsistent_count = inconsistency_results['districts_needing_attention']
        recommendations['immediate_actions'].append(f"Investigate supply chain issues in {inconsistent_count} inconsistent districts")
        
    # Medium-term strategies
    if disparity_results['statistical_significance']:
        recommendations['medium_term_strategies'].append("Implement state-level performance monitoring")
        recommendations['medium_term_strategies'].append("Share best practices from high-performing states")
        
    # Healthcare system recommendations
    if delivery_results['recommendations']:
        recommendations['medium_term_strategies'].extend(delivery_results['recommendations'])
        
    # Long-term monitoring
    recommendations['long_term_monitoring'].append("Establish quarterly vaccination coverage reviews")
    recommendations['long_term_monitoring'].append("Implement predictive analytics for early intervention")
    
    # Resource allocation
    recommendations['resource_allocation_priorities'].append("Prioritize bottom 10% districts for additional funding")
    recommendations['resource_allocation_priorities'].append("Allocate logistics support to high-inconsistency regions")
    
    return recommendations

def main():
    """
    Execute comprehensive vaccination coverage analysis and generate policy recommendations.
    """
    
    print("="*80)
    print("VACCINATION COVERAGE ANALYSIS - REGIONAL DISPARITIES & POLICY INSIGHTS")
    print("="*80)
    print()
    
    # Load and validate data
    print("1. Loading vaccination coverage data...")
    df, existing_insights = load_vaccination_data()
    
    if df is None:
        print("❌ Unable to load vaccination data. Please run the notebooks first.")
        return
        
    print()
    
    # Analyze regional disparities
    print("2. Analyzing regional vaccination disparities...")
    disparity_results = analyze_regional_disparities(df)
    
    if disparity_results['under_vaccinated_districts']:
        worst_district = disparity_results['under_vaccinated_districts'][0]
        print(f"   🚨 Worst performing district: {worst_district['district']} ({worst_district['state']}) - {worst_district['composite_vaccination_score']:.1f}%")
        print(f"   📊 {len(disparity_results['under_vaccinated_districts'])} districts identified for immediate intervention")
    
    if disparity_results['statistical_significance']:
        print(f"   ✅ Statistical evidence: State-level differences are significant (p < 0.05)")
    else:
        print(f"   ⚠️ No significant state-level differences detected")
    print()
    
    # Detect rollout inconsistencies  
    print("3. Detecting vaccination rollout inconsistencies...")
    inconsistency_results = detect_rollout_inconsistencies(df)
    
    if inconsistency_results['inconsistency_statistics']:
        stats = inconsistency_results['inconsistency_statistics']
        print(f"   📈 Average inconsistency (CV): {stats['mean_cv']:.1f}%")
        print(f"   🎯 Districts needing attention: {inconsistency_results['districts_needing_attention']}")
    
    if inconsistency_results['inconsistent_districts']:
        worst_inconsistent = inconsistency_results['inconsistent_districts'][0]
        print(f"   🔄 Most inconsistent: {worst_inconsistent['district']} (CV: {worst_inconsistent['vaccination_cv']:.1f}%)")
    print()
    
    # Analyze healthcare delivery patterns
    print("4. Analyzing healthcare delivery patterns...")
    delivery_results = analyze_healthcare_delivery(df)
    
    if delivery_results['public_vs_private']:
        pub_priv = delivery_results['public_vs_private']
        primary_system = delivery_results['delivery_patterns'].get('primary_system', 'unknown')
        print(f"   🏥 Public facilities: {pub_priv['public_mean']:.1f}% average usage")
        print(f"   🏢 Private facilities: {pub_priv['private_mean']:.1f}% average usage") 
        print(f"   🎯 Primary delivery system: {primary_system.title()}")
    print()
    
    # Generate policy recommendations
    print("5. Generating evidence-based policy recommendations...")
    recommendations = generate_policy_recommendations(
        disparity_results, inconsistency_results, delivery_results
    )
    
    print()
    print("="*80)
    print("📋 POLICY RECOMMENDATIONS FOR PUBLIC HEALTH DECISION-MAKERS")
    print("="*80)
    
    print(f"\n🚨 IMMEDIATE ACTIONS (0-3 months):")
    for action in recommendations['immediate_actions']:
        print(f"   • {action}")
    
    print(f"\n🚀 MEDIUM-TERM STRATEGIES (3-12 months):")  
    for strategy in recommendations['medium_term_strategies']:
        print(f"   • {strategy}")
    
    print(f"\n📈 LONG-TERM MONITORING (1+ years):")
    for monitoring in recommendations['long_term_monitoring']:
        print(f"   • {monitoring}")
        
    print(f"\n💰 RESOURCE ALLOCATION PRIORITIES:")
    for priority in recommendations['resource_allocation_priorities']:
        print(f"   • {priority}")
    
    # Save comprehensive results
    print()
    print("6. Saving analysis results...")
    
    try:
        base_path = Path(__file__).parent.parent.parent  
        results_dir = base_path / "data" / "processed"
        results_dir.mkdir(exist_ok=True)
        
        complete_analysis = {
            'analysis_timestamp': pd.Timestamp.now().isoformat(),
            'regional_disparities': disparity_results,
            'rollout_inconsistencies': inconsistency_results, 
            'healthcare_delivery': delivery_results,
            'policy_recommendations': recommendations,
            'summary': {
                'total_districts_analyzed': len(df),
                'districts_needing_immediate_attention': len(disparity_results['under_vaccinated_districts']),
                'districts_with_rollout_issues': inconsistency_results['districts_needing_attention'],
                'statistical_evidence_of_disparities': disparity_results['statistical_significance']
            }
        }
        
        output_file = results_dir / "comprehensive_vaccination_analysis.json"
        with open(output_file, 'w') as f:
            json.dump(complete_analysis, f, indent=2, default=str)
            
        print(f"   ✅ Complete analysis saved to: {output_file}")
        
    except Exception as e:
        print(f"   ⚠️ Could not save results: {e}")
    
    print()
    print("="*80) 
    print("✅ VACCINATION COVERAGE ANALYSIS COMPLETE")
    print("="*80)
    print()
    print("🎯 KEY FINDINGS:")
    print(f"   • {len(df)} districts analyzed across {df['state'].nunique()} states/UTs")
    print(f"   • {len(disparity_results['under_vaccinated_districts'])} districts identified for priority intervention")
    if inconsistency_results['districts_needing_attention'] > 0:
        print(f"   • {inconsistency_results['districts_needing_attention']} districts show rollout inconsistencies")
    print(f"   • Evidence-based recommendations generated for policy makers")
    
    print()
    print("📊 NEXT STEPS:")
    print("   1. Share findings with public health officials")
    print("   2. Implement recommended interventions in priority districts") 
    print("   3. Monitor progress and update analysis with new data")
    print("   4. Conduct follow-up analysis to measure improvement")

if __name__ == "__main__":
    main()