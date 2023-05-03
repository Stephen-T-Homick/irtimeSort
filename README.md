# irtimeSort

This simple python script is designed with the incident responder / handler in mind to combine Excel and CSV files for the purpose of organizing timestamps for a forensic report. It is written in Python and requires a compatible version of Microsoft Excel to run or a reliable csv reader.

This script is beneficial for combining date/timestamp data from multiple files into a single file for analysis.

## Getting Started

To get started irtimeSort, you will need to have Python installed on your machine. You can download Python from the official website [here](https://www.python.org/downloads/).

You will also need to install the following dependencies:

* pandas
* xlrd
* openpyxl

You can install these dependencies using pip3: (Be careful on Mac OS with using Brew that you don't break packages)

```
pip3 install pandas xlrd openpyxl
```

Once you have Python and the required dependencies installed, you can run the `irtimeSort.py` script. The script will prompt you to select the Excel and CSV files that you want to combine.

## Usage

To use the irtimeSort utility, follow these steps:

1. Open a terminal or command prompt and navigate to the directory containing the `irtimeSort.py` script.
2. Run the script by typing `python irtimeSort.py` and pressing Enter.
3. When prompted, select the Excel and CSV files that you want to combine.
4. The script will combine the data from both files and generate a new Excel file containing the combined data in a table format.
5. Use the table to analyze the data and create a forensic report.

## 'True' Usage

irtimeSort.py [-h] output_file input_files [input_files ...]

Combine dates or timestamps from XLSX or CSV files

positional arguments:
  output_file  path to the output file
  input_files  paths to the input files

options:
  -h, --help   show this help message and exit

## Customization

You can customize the table layout and formatting by modifying the `irtimeSort.py` script. Look for the `generate_table()` function to see how the table is generated.

## Contributing

If you would like to contribute to the irtimeSort utility, please fork the repository and submit a pull request. You can also submit bug reports or feature requests by opening an issue.

## License

This utility is open source and free to distribute and copy. See the 'license' file for more information.
