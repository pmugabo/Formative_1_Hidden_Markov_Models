# Modeling Human Activity States Using Hidden Markov Models

This repository contains a completed Human Activity Recognition project using smartphone accelerometer and gyroscope data collected with Sensor Logger. The model uses a Gaussian Hidden Markov Model to infer four hidden states: standing, walking, jumping, and still.

## Repository contents

- `data/raw/` - training Sensor Logger recordings
- `data/unseen/` - unseen test recordings
- `data/processed/` - extracted features, sampling rates, transition matrix, and evaluation metrics
- `notebooks/human_activity_hmm.ipynb` - complete implementation
- `figures/` - transition heatmap, decoded sequence, confusion matrix, and sensor signal figure
- `report/` - final DOCX and PDF report

## Main result

Overall accuracy on unseen data: **0.951**.

## How to run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open the notebook:
   ```bash
   jupyter notebook notebooks/human_activity_hmm.ipynb
   ```
3. Run all cells.

## Sensors used

- Accelerometer: x, y, z
- Gyroscope: x, y, z

All recordings were resampled to 50 Hz during preprocessing to harmonize the sampling rate.
