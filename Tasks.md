*Environment Setup**

- **OS:** Windows
- **Status (as of 2026-02-24):** Python and Anaconda installed and verifiedExpand commentComment on line R6

**What I installed**

- Python (installed and callable from Command Prompt)
- Anaconda (Anaconda Distribution for Windows)

**Steps I followed (brief)**

1. Downloaded the Anaconda installer for Windows from the official site.
2. Ran the installer and completed the setup (default options).
3. Opened Command Prompt and Anaconda Prompt to verify installations.

**Verification commands (run in Command Prompt or Anaconda Prompt)**

Run these commands and paste the outputs into this README for permanent proof.

Python version:

```
python --version
```

Conda (Anaconda) version:

```
conda --version
```

Python executable path (optional):

```
python -c "import sys; print(sys.executable)"
```

List Conda environments (shows `base`):

```
conda info --envs
```Expand commentComment on lines R21 to R45

Example: paste your actual terminal outputs here after running the commands above.

```
# Python --version
# REPLACE_WITH_YOUR_OUTPUT

# conda --version
# REPLACE_WITH_YOUR_OUTPUT
```

**Optional — create a dedicated Data Science environment**

Run these in Anaconda Prompt if you want a separate environment for the sprint:

```
conda create -n ds-sprint python=3.10 -y
conda activate ds-sprint
conda install numpy pandas matplotlib jupyter -y
```

**Video walkthrough (record ~2 minutes)**

Please include all of the following in your short screen recording:

- Terminal showing `python --version` (proof Python is callable)
- Terminal showing `conda --version` (proof Anaconda/conda is accessible)
- A brief walkthrough of this README section showing where you saved the verification outputs

Keep the recording concise and focused — this validates that the setup is real and reproducible.

**Next steps**

- Paste the actual command outputs into the "Example" block above so this README serves as proof.
- (Optional) Push changes and create a Pull Request per the milestone instructions.