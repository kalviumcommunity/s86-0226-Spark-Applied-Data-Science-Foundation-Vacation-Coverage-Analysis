import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(layout="wide", page_title="Vaccination Coverage Analysis")

def load_data():
    """Loads the necessary data files."""
    try:
        clean_df = pd.read_csv('data/processed/vaccination_coverage_clean.csv')
        temporal_df = pd.read_csv('data/processed/temporal_analysis.csv')
        with open('data/processed/comprehensive_vaccination_analysis.json', 'r') as f:
            analysis_data = json.load(f)
        return clean_df, temporal_df, analysis_data
    except FileNotFoundError:
        st.error("Error: Processed data files not found. Please run the analysis notebooks first.")
        return None, None, None

def main():
    """Main function to render the dashboard."""
    st.title("💉 Vaccination Coverage Interactive Dashboard")
    st.markdown("""
    This dashboard provides an interactive and in-depth view of vaccination coverage, regional disparities, and healthcare delivery insights across various districts and states.
    """)

    clean_df, temporal_df, analysis_data = load_data()

    if clean_df is None:
        return

    # --- Sidebar Filters ---
    st.sidebar.header("Filters")
    selected_state = st.sidebar.selectbox("Select State/UT", ['All'] + sorted(clean_df['state'].unique()))

    if selected_state != 'All':
        filtered_df = clean_df[clean_df['state'] == selected_state]
    else:
        filtered_df = clean_df

    # --- Key Insights Summary ---
    st.header("Key Analysis Insights")
    summary = analysis_data.get('summary', {})
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Districts Analyzed", summary.get('total_districts_analyzed', 'N/A'))
    col2.metric("Districts Needing Immediate Attention", summary.get('districts_needing_immediate_attention', 'N/A'))
    col3.metric("Districts with Rollout Issues", summary.get('districts_with_rollout_issues', 'N/A'))
    col4.metric("Evidence of Disparities", "Significant" if summary.get('statistical_evidence_of_disparities') == "True" else "Not Significant")

    # --- Detailed Analysis Tabs ---
    tab1, tab2, tab3, tab4 = st.tabs(["Regional Disparities", "Rollout Inconsistencies", "State Performance", "Healthcare Delivery"])

    with tab1:
        st.subheader("Top 15 Under-Vaccinated Districts")
        st.markdown("These districts have the lowest composite vaccination scores and require immediate attention.")
        under_vaccinated_df = pd.DataFrame(analysis_data['regional_disparities']['under_vaccinated_districts'])
        st.dataframe(under_vaccinated_df)

    with tab2:
        st.subheader("Top 10 Districts with Inconsistent Vaccination Rollout")
        st.markdown("These districts show high variability (Coefficient of Variation) in vaccination coverage, indicating potential supply chain or delivery issues.")
        inconsistent_df = pd.DataFrame(analysis_data['rollout_inconsistencies']['inconsistent_districts'])
        st.dataframe(inconsistent_df)

    with tab3:
        st.subheader("State-wise Vaccination Performance")
        st.markdown("This chart shows the mean composite vaccination score for each state.")
        state_perf = analysis_data['regional_disparities']['state_performance']['mean']
        state_perf_df = pd.DataFrame(list(state_perf.items()), columns=['State', 'Mean Composite Score']).sort_values('Mean Composite Score', ascending=False)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.barplot(x='Mean Composite Score', y='State', data=state_perf_df, ax=ax, palette='viridis')
        ax.set_title('State-wise Mean Composite Vaccination Score')
        ax.set_xlabel('Mean Composite Score')
        ax.set_ylabel('State')
        st.pyplot(fig)

    with tab4:
        st.subheader("Healthcare Delivery: Public vs. Private Sector")
        delivery_data = analysis_data['healthcare_delivery']['public_vs_private']
        public_mean = delivery_data.get('public_mean', 0)
        private_mean = delivery_data.get('private_mean', 0)
        
        st.markdown(f"The analysis indicates that the **public healthcare system is the primary driver of vaccination**, with an average coverage of **{public_mean:.2f}%** from public sources, compared to just **{private_mean:.2f}%** from private sources.")
        
        fig, ax = plt.subplots()
        sns.barplot(x=['Public Sector', 'Private Sector'], y=[public_mean, private_mean], ax=ax)
        ax.set_ylabel('Mean Vaccination Coverage (%)')
        ax.set_title('Vaccination Coverage by Healthcare Sector')
        st.pyplot(fig)
        
        st.info("Recommendations: Strengthen public healthcare infrastructure and focus resources on government health facilities.")

    # --- Original Content (can be kept or integrated into tabs) ---
    st.header("Explore Data and Trends")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Regional Vaccination Coverage Data")
        st.dataframe(filtered_df[['district', 'state', 'full_vaccination_any_source', 'bcg_vaccination', 'polio_3_doses']])

    with col2:
        st.subheader("Coverage Distribution")
        fig, ax = plt.subplots()
        sns.histplot(filtered_df['full_vaccination_any_source'].dropna(), bins=20, kde=True, ax=ax)
        ax.set_title('Distribution of Full Vaccination Scores')
        ax.set_xlabel('Full Vaccination Coverage (%)')
        ax.set_ylabel('Number of Districts')
        st.pyplot(fig)

    # --- Temporal Trends ---
    st.header("📈 Outreach Trends: Is Coverage Improving?")
    st.markdown("This chart shows whether vaccination coverage is improving or declining for the youngest children (12-23 months) compared to a slightly older group (24-35 months).")

    if temporal_df is not None:
        if selected_state != 'All':
            state_districts = clean_df[clean_df['state'] == selected_state]['district'].unique()
            temporal_filtered_df = temporal_df[temporal_df['District Names'].isin(state_districts)]
        else:
            temporal_filtered_df = temporal_df

        if selected_state == 'All':
            top_10 = temporal_filtered_df.nlargest(10, 'Progress_Metric')
            bottom_10 = temporal_filtered_df.nsmallest(10, 'Progress_Metric')
            plot_df = pd.concat([top_10, bottom_10])
        else:
            plot_df = temporal_filtered_df

        if not plot_df.empty:
            fig, ax = plt.subplots(figsize=(10, 12))
            for i, row in plot_df.iterrows():
                color = 'green' if row['Progress_Metric'] > 0 else 'red'
                ax.plot([0, 1], [row['Coverage_24_35'], row['Coverage_12_23']], marker='o', color=color)
                ax.text(-0.05, row['Coverage_24_35'], row['District Names'], ha='right', va='center', fontsize=9)
                ax.text(1.05, row['Coverage_12_23'], f"{row['Progress_Metric']:.1f}%", ha='left', va='center', fontsize=9, color=color)

            ax.set_xticks([0, 1])
            ax.set_xticklabels(['24-35 Months', '12-23 Months'])
            ax.set_ylabel('Vaccination Coverage (%)')
            ax.set_title('Change in Vaccination Coverage Between Age Cohorts')
            st.pyplot(fig)
        else:
            st.warning("No temporal data to display for the selected state.")

if __name__ == '__main__':
    main()
