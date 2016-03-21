
# xlrd

### What it is good for?

Read Excel documents.

The `xlrd` module reads a spreadsheet into a hierarchical data structure. On top are sheets, consisting of rows which in turn consist of columns.
The corresponding Python module `xlwt` allows you to write Excel spreadsheets. You may also consider the newer `openpyxl` module.

### Installed with Python by default?

no

### Installed with Anaconda?

yes

### How to install it?

    pip install xlrd

### Example

    >>> import xlrd

    >>> workbook = xlrd.open_workbook('hamlet.xlsx')
    >>> sheet_names = workbook.sheet_names()
    >>> sheet = workbook.sheet_by_name(sheet_names[0])

    >>> for row_idx in range(sheet.nrows):
    ...    for col_idx in range(sheet.ncols):
    ...         cell = sheet.cell(row_idx, col_idx)
    ...         print(cell.value, end="\t")
    ...    print()
    1.0    Hamlet    the Prince of Denmark
    2.0    Polonius  Ophelias father

### Where to learn more?

[http://www.python-excel.org/](http://www.python-excel.org/)
