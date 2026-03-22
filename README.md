# Vaccination Coverage Analysis - Regional Disparities & Policy Insights

## What's This All About?

Imagine you're a public health official. You have a ton of data about vaccinations across the country, but it's just a giant spreadsheet. How do you quickly figure out which areas need the most help? This project is designed to solve that problem.

We take raw vaccination data and turn it into clear, actionable insights. Our goal is to help decision-makers spot under-vaccinated regions, find issues in the vaccine rollout, and understand how vaccination rates are changing over time.

## What We've Done

We've already completed a deep analysis of the data, which includes:

- **Cleaning the Data**: We've taken the raw data and cleaned it up to make sure it's accurate and consistent.
- **Finding Key Insights**: We've identified the 15 districts that need the most urgent help and 20 districts where the vaccine rollout seems to be inconsistent.
- **Statistical Proof**: We've used statistical tests to prove that the differences we're seeing between regions are real and not just due to random chance.
- **Temporal Analysis**: We've analyzed how vaccination coverage is changing over time by comparing different age groups.

## Interactive Dashboard & Predictive Model

To make our findings even more accessible, we've built two new features:

### 1. Interactive Dashboard

We've created an interactive dashboard that lets you explore the data for yourself. You can filter by state to see how different districts are performing and view the trends in vaccination coverage over time.

**How to run the dashboard:**

1.  Make sure you have the required libraries installed:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the following command in your terminal:
    ```bash
    streamlit run src/dashboard/interactive_dashboard.py
    ```

### 2. Predictive Model

We've also built a simple predictive model to understand what factors are most important for achieving high vaccination coverage. Our model found that the coverage of the Polio vaccine is the strongest predictor of full immunization. This suggests that the infrastructure and outreach for the Polio vaccine program are very effective and could be a model for other vaccination efforts.

You can retrain the model by running:

```bash
python src/models/train_model.py
```

## How This Helps

This project helps public health officials make better decisions by:

- **Focusing Resources**: By identifying the areas that need the most help, we can make sure that resources are sent where they're needed most.
- **Improving Logistics**: By spotting inconsistencies in the vaccine rollout, we can help fix supply chain and logistics issues.
- **Providing Clear Evidence**: Our statistical analysis gives policymakers the evidence they need to make informed decisions.

## Technical Details

For those interested in the technical side of things, this project uses Python and a number of popular data science libraries. The analysis is done in a series of Jupyter notebooks and Python scripts:

1.  **[Data Cleaning](notebooks/01_data_cleaning.ipynb)**: Preparing the data for analysis.
2.  **[EDA & Visualizations](notebooks/02_eda_visualizations.ipynb)**: Exploring the data and creating visualizations.
3.  **[Temporal Analysis](src/analysis/temporal_analysis.py)**: Analyzing trends over time.
4.  **[Predictive Model](src/models/train_model.py)**: Training a model to predict vaccination coverage.
5.  **[Interactive Dashboard](src/dashboard/interactive_dashboard.py)**: An interactive dashboard to explore the data.

6.  **[Statistical Analysis](notebooks/03_statistical_analysis.ipynb)** - Hypothesis testing and validation

### Automated Analysis Script

**[Main Analysis Script](src/analysis/vacation_data_demo.py)**

- Comprehensive vaccination coverage analysis
- Statistical validation of regional disparities
- Evidence-based policy recommendation generation
- Automated reporting and results export

### Key Outputs Generated

- `vaccination_coverage_clean.csv` - Processed dataset
- `vaccination_insights.json` - EDA findings and patterns
- `statistical_analysis_results.json` - Statistical test results
- `comprehensive_vaccination_analysis.json` - Complete analysis report

## Data Science Methodology

### Statistical Rigor

- **Hypothesis Testing:** Kruskal-Wallis for regional comparisons
- **Effect Size Analysis:** Eta-squared for practical significance
- **Confidence Intervals:** 95% CIs for key estimates
- **Correlation Analysis:** Pearson correlation for vaccine relationships

### Validation Approach

- Multiple vaccine cross-validation for composite scores
- Statistical significance testing (α = 0.05)
- Practical significance thresholds (>2 SD for severe inconsistency)
- Evidence-based recommendation tiers

## Running the Analysis

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### Quick Start

```bash
# Run complete analysis pipeline
python src/analysis/vacation_data_demo.py

# Or execute notebooks interactively
jupyter notebook notebooks/
```

## Results & Impact

### Quantified Outcomes

- **706 districts analyzed** across India's vaccination system
- **15 priority districts identified** for immediate intervention
- **20 districts flagged** for rollout consistency issues
- **Statistical evidence generated** for policy decisions (p < 0.05)

### Public Health Value

- **Targeted intervention:** Focus resources where most needed
- **Evidence-based policy:** Statistical validation for funding decisions
- **Systematic monitoring:** Framework for ongoing performance tracking
- **Equity focus:** Identifies and addresses coverage disparities

## Future Enhancements

### Temporal Analysis

- Longitudinal trend analysis as historical data becomes available
- Seasonal vaccination pattern identification
- Progress tracking over multiple reporting cycles

### Geographic Integration

- Mapping integration for spatial pattern analysis
- Distance-to-facility accessibility modeling
- Population density correlation analysis

### Predictive Modeling

- Risk prediction models for coverage gaps
- Early warning systems for supply chain issues
- Resource allocation optimization algorithms

---

## Data Science Lifecycle Success

This project demonstrates the complete **Question → Data → Insight** lifecycle:

✅ **Question:** Clear, actionable research questions driving analysis  
✅ **Data:** Rigorous processing and quality validation of real-world health data  
✅ **Insight:** Statistical evidence transformed into specific policy recommendations

**Impact:** Evidence-based recommendations ready for immediate implementation by public health officials.

### Key Question

Where are vaccination disparities occurring, and how are coverage trends evolving over time?

### Data Needed

**Vaccination data**

- Total doses administered
- Coverage percentages by region
- Time-series trends

**Population and demographics**

- Population size
- Urban/rural classification
- Age distribution

**Temporal data**

- Reporting dates
- Weekly or monthly updates

### Expected Impact

The analysis supports:

- Targeted interventions in low-coverage regions
- Better healthcare resource allocation
- Proactive outreach planning
- Early identification of stagnation risk

## Conclusion

The **Question → Data → Insight** lifecycle ensures a structured and responsible approach:

- The question defines direction
- The data provides evidence
- The insight drives action

This project transforms vaccination statistics into practical guidance for public health decision-making.
