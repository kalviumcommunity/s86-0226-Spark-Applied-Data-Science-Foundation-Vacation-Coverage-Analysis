import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_temporal_trends(input_path='data/raw/datafile.csv', output_visual_path='visuals/outreach_trends.png', output_csv_path='data/processed/temporal_analysis.csv'):
    """
    Analyzes temporal trends in vaccination coverage by comparing two age cohorts.

    Args:
        input_path (str): Path to the raw data file.
        output_visual_path (str): Path to save the output visualization.
        output_csv_path (str): Path to save the processed temporal data.
    """
    # Load the dataset
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"Error: The file at {input_path} was not found.")
        return

    # Define vaccination columns to analyze
    vaccination_cols = [
        'Children age 12-23 months fully vaccinated based on information from either vaccination card or mother\'s recall11 (%)',
        'Children age 24-35 months who have received a second dose of measles-containing vaccine (MCV) (%)'
    ]

    # Check if necessary columns exist
    if not all(col in df.columns for col in vaccination_cols + ['District Names', 'State/UT']):
        print("Error: The dataset is missing required columns.")
        print(f"Available columns: {df.columns.tolist()}")
        return

    # Clean column names for easier access
    df.columns = df.columns.str.strip()

    # Calculate coverage for each cohort
    # Convert percentage strings to numeric, coercing errors
    df[vaccination_cols[0]] = pd.to_numeric(df[vaccination_cols[0]], errors='coerce')
    df[vaccination_cols[1]] = pd.to_numeric(df[vaccination_cols[1]], errors='coerce')

    # Drop rows where vaccination data is missing for a fair comparison
    df.dropna(subset=vaccination_cols, inplace=True)


    cohort_12_23 = df.groupby('District Names')[vaccination_cols[0]].mean().reset_index()
    cohort_12_23 = cohort_12_23.rename(columns={vaccination_cols[0]: 'Coverage_12_23'})

    cohort_24_35 = df.groupby('District Names')[vaccination_cols[1]].mean().reset_index()
    cohort_24_35 = cohort_24_35.rename(columns={vaccination_cols[1]: 'Coverage_24_35'})

    # Merge the cohorts
    merged_df = pd.merge(cohort_12_23, cohort_24_35, on='District Names')

    # Calculate the Progress Metric
    merged_df['Progress_Metric'] = merged_df['Coverage_12_23'] - merged_df['Coverage_24_35']

    # Sort by the progress metric
    sorted_df = merged_df.sort_values(by='Progress_Metric', ascending=False)

    # --- Visualization: Slope Chart ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 20))

    # Get top and bottom 20 for clarity
    top_20 = sorted_df.head(20)
    bottom_20 = sorted_df.tail(20)
    plot_df = pd.concat([top_20, bottom_20])

    for i, row in plot_df.iterrows():
        # Line color based on progress
        color = 'green' if row['Progress_Metric'] > 0 else 'red'
        ax.plot([0, 1], [row['Coverage_24_35'], row['Coverage_12_23']], marker='o', color=color, linewidth=1.5, markersize=5)
        
        # Add district labels
        ax.text(-0.05, row['Coverage_24_35'], row['District Names'], ha='right', va='center', fontsize=8)
        ax.text(1.05, row['Coverage_12_23'], f"{row['Progress_Metric']:.1f}%", ha='left', va='center', fontsize=8, color=color)


    # Formatting the plot
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['24-35 Months', '12-23 Months'], fontsize=12)
    ax.set_ylabel('Vaccination Coverage (%)', fontsize=12)
    ax.set_title('Outreach Trends: Vaccination Coverage Change by District', fontsize=16, pad=20)
    
    # Remove y-axis labels for districts, as they are now next to the lines
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('outward', 10))

    # Save the processed data for the dashboard
    try:
        sorted_df.to_csv(output_csv_path, index=False)
        print(f"Temporal analysis data saved to {output_csv_path}")
    except Exception as e:
        print(f"Error saving temporal data: {e}")

    plt.tight_layout()
    
    # Save the visualization
    try:
        plt.savefig(output_visual_path, dpi=300)
        print(f"Visualization saved to {output_visual_path}")
    except Exception as e:
        print(f"Error saving visualization: {e}")


if __name__ == '__main__':
    # To run this script from the root of the project directory:
    # python src/analysis/temporal_analysis.py
    analyze_temporal_trends()
