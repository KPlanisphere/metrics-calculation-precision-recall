# Metrics Calculation: Precision, Recall, and F-Measure

This repository contains a Python script for calculating precision, recall, F-measure, and R-precision for information retrieval tasks. The script processes relevant and retrieved document data to compute these metrics for each query.

## Features

- **Read Relevant and Retrieved Data**: Parse files containing relevant and retrieved documents for each query.
- **Compute Metrics**:
  - Precision
  - Recall
  - F-Measure
  - R-Precision
- **Customizable Parameter**: Specify the cutoff point (`Z`) for evaluating the top documents retrieved.
- **Output**: Results are saved in a formatted table to a specified output file.

## Files

- `lab7.py`: Main Python script for processing input files and calculating metrics.
- `rlv-ass`: Input file containing relevant documents for each query.
- `NPL_tf_idf_rels.txt`: Input file containing retrieved documents and their scores.
- `metrics_results.txt`: Output file containing the computed metrics in tabular format.

## How It Works

1. **Load Relevant Documents**:
   The script reads the `rlv-ass` file to create a mapping of relevant documents for each query.

2. **Load Retrieved Documents**:
   The `NPL_tf_idf_rels.txt` file is parsed to retrieve the top `Z` documents for each query.

3. **Compute Metrics**:
   For each query, the script calculates:
   - Precision: The ratio of relevant documents among the top `Z` retrieved documents.
   - Recall: The ratio of relevant documents retrieved to the total relevant documents.
   - F-Measure: The harmonic mean of precision and recall.
   - R-Precision: Precision when retrieving exactly `R` relevant documents.

4. **Output Results**:
   Results are written to `metrics_results.txt` in a structured table:
   ```
   | Consulta | Precision | Recuerdo | Medida F | Precision R |
   |----------|-----------|----------|----------|-------------|
   |    1     |   0.7500  |  0.6000  |  0.6667  |    0.7500   |
   ```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/KPlanisphere/metrics-calculation-precision-recall.git
   cd metrics-calculation-precision-recall
   ```

2. Place the `rlv-ass` and `NPL_tf_idf_rels.txt` files in the directory, or update the file paths in `lab7.py`.

3. Run the script:
   ```bash
   python lab7.py
   ```
   During execution, you will be prompted to enter the value of `Z` (cutoff point).

4. Check the output in `metrics_results.txt`.

## Requirements

- Python 3.10+

## Notes

- Ensure that the input files are correctly formatted. Each query's relevant and retrieved documents must follow the expected structure.
- The script includes error handling for empty queries or missing data.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
