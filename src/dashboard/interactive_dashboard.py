import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(layout="wide", page_title="Vaccination Coverage Analysis")

def load_data():
    """Loads the necessary data files."""
    try:
        clean_df = pd.read_csv('data/processed/vaccination_coverage_clean.csv')
        temporal_df = pd.read_csv('data/processed/temporal_analysis.csv')
        return clean_df, temporal_df
    except FileNotFoundError:
        st.error("Error: Processed data files not found. Please run the analysis notebooks first.")
        return None, None

def main():
    """Main function to render the dashboard."""
    st.title("💉 Vaccination Coverage Interactive Dashboard")
    st.markdown("""
    This dashboard provides an interactive view of vaccination coverage across different regions. 
    Use the filters to explore regional disparities and temporal trends.
    """)

    clean_df, temporal_df = load_data()

    if clean_df is None:
        return

    # --- Sidebar Filters ---
    st.sidebar.header("Filters")
    selected_state = st.sidebar.selectbox("Select State/UT", ['All'] + sorted(clean_df['state'].unique()))

    if selected_state != 'All':
        filtered_df = clean_df[clean_df['state'] == selected_state]
    else:
        filtered_df = clean_df

    # --- Main Content ---
    col1, col2 = st.columns(2)

    with col1:
        st.header("Regional Vaccination Coverage")
        # Use columns that exist in the cleaned file
        st.dataframe(filtered_df[['district', 'state', 'full_vaccination_any_source', 'bcg_vaccination', 'polio_3_doses']])

    with col2:
        st.header("Coverage Distribution")
        fig, ax = plt.subplots()
        # Use a column that exists, like 'full_vaccination_any_source'
        sns.histplot(filtered_df['full_vaccination_any_source'].dropna(), bins=20, kde=True, ax=ax)
        ax.set_title('Distribution of Full Vaccination Scores')
        ax.set_xlabel('Full Vaccination Coverage (%)')
        ax.set_ylabel('Number of Districts')
        st.pyplot(fig)

    # --- Temporal Trends ---
    st.header("📈 Outreach Trends: Is Coverage Improving?")
    st.markdown("This chart shows whether vaccination coverage is improving or declining for the youngest children compared to a slightly older group.")

    if temporal_df is not None:
        if selected_state != 'All':
            state_districts = clean_df[clean_df['state'] == selected_state]['district'].unique()
            temporal_filtered_df = temporal_df[temporal_df['District Names'].isin(state_districts)]
        else:
            temporal_filtered_df = temporal_df

        # For clarity, only show a subset if 'All' is selected
        if selected_state == 'All':
             # Get top and bottom 10 for clarity
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
