# Source code is included in the Jupyter notebook.
# This file documents the main project pipeline:
# 1. Load Sensor Logger Accelerometer.csv and Gyroscope.csv files.
# 2. Resample all recordings to 50 Hz.
# 3. Extract time-domain and frequency-domain features from 1-second windows.
# 4. Train a Gaussian HMM using Baum-Welch EM refinement.
# 5. Decode unseen activity sequences using Viterbi.
# 6. Evaluate using sensitivity, specificity, accuracy, and confusion matrix.
