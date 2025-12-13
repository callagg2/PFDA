# Programming for Data Analytics (PFDA)

The PDFA course is designed to help participants to: 

* Programmatically create plots and other visual outputs from data.
* Design computer algorithms to solve numerical problems.
* Create software that incorporates and utilises standard numerical libraries.
* Employ appropriate data structures when programming for data-intensive applications.


It contains four assignments and a project. The assignments comprise one  **Python Script** and three **Jupyter Notebooks** while the project comprises of a  **Jupyter Notebook**.

## Repository Contents

| File/Folder | Description |
| :--- | :--- |
| `assignments/assignment02-bankholidays.py` | This assignment looks at how you would read in data from a json file, and then clean it up before extracting information from the dictionary object contained within. |
| `assignments/assignment03-pie.ipynb` | This assignment looks at how you would read in data from a csv file, clean up any null values, split text within a column into two columns, and then plot the values of one of those columns in a pie-chart. |
| `assignments/population.ipynb` | This assignment reads in data from a csv file, removes superflouos columns, then creates a pivot table from the data so that the data can be interpreted better. |
| `assignments/weather.ipynb` | This assignment reads in data from a csv file, removes superflouos columns, then works out how to use the groupby function to find the maximums and means of various variables before creating various charts to represent the underlying data. |
| `project/rppi_versus_wpi.ipynb.py` | This project draws upon parts of the various assignment to be able to regress the Residential Property Price Index against the Wholesale Price Index for Building & Construction Materials to identify the size of the dependency. |
| `requirements.txt` | List of Python dependencies required to run the project. |

## Installation & Local Usage

To run this project on your local machine, follow these steps (using bash):

### 1. Clone the repository
git clone [https://github.com/callagg2/pfda.git](https://github.com/callagg2/pfda.git)
cd pfda

### 2. Set up a virtual environment (Optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the code (view the notebook)
jupyter notebook problems.ipynb
