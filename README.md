

# Nessus Scan Comparison Tool

This tool allows you to compare two Nessus scan results and generate a report highlighting new, closed, and open findings.

## Prerequisites

- [Git](https://git-scm.com/)
- [Nessus Scan Results](#prepare-nessus-scan-results)

## Usage

1. **Prepare Nessus Scan Results:**
   - Acquire the old Nessus scan result file and the new Nessus scan result file.
   - Ensure that you rename the files to match the expected names (`old.csv` and `new.csv`).

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/exrienz/Nessus_Compare-Scan.git
   cd Nessus_Compare-Scan
   ```

3. **Give Permission to `extract.sh`:**
   ```bash
   chmod +x extract.sh
   ```

4. **Copy Old and New Nessus Scan Results:**
   - Copy the `old.csv` and `new.csv` files into the same directory where the script (`extract.sh`) is located.

5. **Execute the Script:**
   ```bash
   ./extract.sh
   ```

6. **Review the Results:**
   - Open or inspect the generated `report.csv` file to view the comparison results.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please [open an issue](https://github.com/exrienz/Nessus_Compare-Scan/issues).

## License

This project is licensed under the [MIT License](LICENSE).

```

Remember to replace placeholders like `[Nessus Scan Results]` and `[MIT License]` with actual links or details specific to your project. Also, update the repository URL, and add a license file if needed.
