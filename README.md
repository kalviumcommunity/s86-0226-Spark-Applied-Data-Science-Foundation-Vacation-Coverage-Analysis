# s86-0226-Spark-Applied-Data-Science-Foundation-Vacation-Coverage-Analysis

# Vaccination Coverage Analysis

## Overview
Government health departments publish vaccination data, but decision-makers often lack clear visibility into regional disparities.

This project applies the **Question → Data → Insight** data science lifecycle to turn public vaccination data into actionable guidance for public health planning.

## Problem Statement
This analysis focuses on three core goals:
- Identify under-vaccinated regions
- Detect rollout inconsistencies
- Understand temporal trends in vaccination outreach

## Data Science Lifecycle

### 1) Question
Every analysis starts with a focused question:

**Which regions are under-vaccinated, where are rollout inconsistencies occurring, and how are vaccination trends changing over time?**

Why this matters:
- Targets a real decision-making gap
- Prioritizes disparities over raw totals
- Defines what data must be collected and validated

### 2) Data
To answer the question, the project uses:
- Regional vaccination coverage rates
- Weekly/monthly vaccination counts
- Population and demographic context
- Reporting timestamps

Data quality checks include:
- Completeness and missing values
- Reporting delays
- Regional inconsistencies

The dataset is treated as **evidence in context**, not automatic truth.

### 3) Insight
Insights come from interpretation, not just calculation. Expected outcomes include:
- Regions with consistently low vaccination coverage
- Sudden fluctuations that suggest rollout or reporting issues
- Plateauing trends that may signal reduced outreach effectiveness

These insights help connect patterns to public health actions.

## Applying the Lifecycle to This Project

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

# Launching Jupyter Notebook and Understanding the Home Interface

This section provides a step-by-step guide to help you navigate and familiarize yourself with Jupyter Notebook. By completing this milestone, you will be able to confidently launch, navigate, and manage notebooks in your project environment.

## Objectives

1. **Launch Jupyter Notebook correctly from your local environment**
2. **Understand the Jupyter Home interface**
3. **Navigate folders and files confidently**
4. **Create and manage notebooks in the correct location**

### Why This Matters

Many early data science issues arise from:

- Running notebooks from the wrong directory
- Creating files in unintended locations
- Losing track of datasets or notebooks
- Confusion about which environment or kernel is active

This milestone ensures that:

- Your notebooks live where your project expects them
- Your data, notebooks, and scripts stay organized
- You avoid silent workflow mistakes early in the sprint

Think of this as learning the workspace rules before doing any real work.

---

## Steps to Complete

### 1. Launching Jupyter Notebook

Launch Jupyter Notebook from the terminal or command prompt:

- Ensure the correct Conda environment is active
- Launch Jupyter using the terminal command:
  ```bash
  jupyter notebook
  ```
- Confirm that Jupyter opens in your web browser without errors
- Pay attention to the directory from which Jupyter is launched, as this determines the root folder shown in the interface

### 2. Understanding the Jupyter Home Interface

Once Jupyter opens, explore the Home interface. Identify:

- The file and folder listing area
- Navigation breadcrumbs
- Buttons for creating new files and notebooks
- Indicators for file types (folders, notebooks, scripts)

The goal is to understand what you are seeing, not to interact with everything.

### 3. Navigating Project Folders

Practice navigating through folders using the Jupyter interface:

- Move into and out of directories
- Locate your project folder
- Understand how folder navigation maps to your local file system

This step ensures you always know where your work is being saved.

### 4. Creating and Opening a Notebook

Create a new Jupyter Notebook:

- Create a notebook in the correct folder
- Open the notebook
- Confirm that it uses the expected Python kernel
- Run a simple cell to ensure the notebook executes correctly

> **Note:** You are not expected to write data science code here—only to verify notebook functionality.

### 5. Notebook File Management Basics

Understand basic notebook management actions:

- Rename a notebook
- Save changes
- Close the notebook safely
- Reopen it from the Home interface

This ensures you can manage notebook files without accidental loss or confusion.

---

## Video Walkthrough (~2 Minutes)

Record a short screen-capture video demonstrating your understanding. Your video must include:

1. Launching Jupyter Notebook from the terminal
2. A walkthrough of the Home interface
3. Navigating folders
4. Creating and opening a notebook
5. Running a simple cell

> **Submission Guidelines:**
> - Submit your work as a Pull Request (if required by the assignment)
> - Submit the video link as instructed
> - Video should be approximately 2 minutes
> - Video must be screen-facing and clearly visible
> - Keep explanations concise and focused on navigation and understanding

---

## Important Notes

- This milestone is about orientation and confidence, not analysis
- Do not start EDA or data loading yet
- Always be aware of the folder you are working in
- Treat notebooks as project artifacts, not temporary scratchpads

Understanding Jupyter’s workspace early prevents disorganization later. This milestone ensures you can navigate, create, and manage notebooks intentionally throughout the Data Science sprint.

---

## Bonus Content

This section is optional, and learners who want to explore the topics covered so far can utilize the materials provided below:

- [Running the Notebook](https://jupyter-notebook.readthedocs.io/en/stable/)
- [Jupyter/IPython Notebook Quick Start Guide](https://realpython.com/jupyter-notebook-introduction/)
- [Get Started With Jupyter Notebook For Python](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)

# Running, Restarting, and Interrupting Jupyter Kernels

This milestone focuses on understanding how Jupyter kernels work and how to control them safely. Many notebook issues are not caused by code errors, but by kernel state—cells running out of order, stale variables, or long-running executions that were never interrupted.

## Why This Matters
Common notebook problems include:

- Code working once but failing later
- Variables mysteriously changing values
- Cells depending on hidden execution order
- Kernels freezing during execution

These issues usually come from poor kernel management, not bad logic.

This milestone ensures that:

- Your notebooks behave consistently
- You can debug issues systematically
- Reviewers and teammates can reproduce your results

Think of the kernel as the engine of your notebook—this lesson teaches you how to control it.

## What You Are Expected to Do
This is a kernel control and debugging milestone, not a data analysis task.

You are expected to:

1. **Run Cells in Sequence**
   - Execute cells one by one
   - Observe how outputs depend on execution order
   - Understand that the kernel remembers variables until restarted

2. **Restart the Kernel**
   - Use the restart option from the Jupyter menu
   - Observe that variables and memory are cleared
   - Rerun cells from the top to restore state

3. **Interrupt Execution**
   - Start a deliberately long-running or infinite operation
   - Interrupt execution using the interrupt option
   - Confirm that the notebook remains responsive afterward

4. **Recognize When to Restart vs Interrupt**
   - Identify scenarios where interrupting is sufficient
   - Identify scenarios where a full restart is safer
   - Explain the trade-offs between the two actions

## Video Walkthrough (~2 Minutes)
Record a short screen-capture video demonstrating kernel control.

Your video must include:
- Running cells normally
- Interrupting a running cell
- Restarting the kernel
- Rerunning cells after restart
- Brief explanation of why each action is used

## Data Organization Milestone: Raw, Processed, and Output Data

### Why Organize Data?
Organizing data across its lifecycle ensures:
- Trustworthy and auditable workflows
- Reproducible results
- Prevention of data corruption and accidental overwrites

### Folder Structure
To maintain clean and auditable workflows, organize your data into the following folders:

1. **Raw Data**
   - Contains the original, untouched source data.
   - Guidelines:
     - Store raw data exactly as received.
     - Never edit or clean raw data directly.
     - Treat raw data as read-only.
     - Keep raw data clearly identifiable.

2. **Processed Data**
   - Contains datasets derived from raw data after cleaning or transformation.
   - Guidelines:
     - Save cleaned or transformed datasets separately.
     - Use clear filenames indicating the processing stage.
     - Ensure processed data can be recreated from raw data.
     - Avoid mixing processed files with raw inputs.

3. **Output Artifacts**
   - Contains final or intermediate results such as plots, tables, reports, or models.
   - Guidelines:
     - Store outputs separately from data folders.
     - Use descriptive names for output files.
     - Keep outputs easy to locate and review.

### Preventing Data Contamination
To avoid errors and maintain data integrity:
- Identify risks of overwriting raw data.
- Avoid circular dependencies between data stages.
- Ensure scripts read from raw data and write to processed/output folders.
- Maintain a one-directional data flow.

### Video Walkthrough
Record a short screen-capture video (~2 minutes) explaining your data organization. Include:
- Raw data folder and explanation.
- Processed data folder and explanation.
- Output artifacts folder and explanation.
- Rationale behind separating data stages.

### Submission Guidelines
- Submit your work as a Pull Request (if required).
- Submit the video link as instructed.
- Ensure the video is screen-facing, clearly visible, and approximately 2 minutes long.
