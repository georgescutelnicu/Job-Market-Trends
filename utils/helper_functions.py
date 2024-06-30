import pandas as pd


def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    """

    data = pd.read_csv(file_path)
    return data


def count_jobs(df, category):
    """
    Count the number of jobs in a specified category.

    Args:
    - df (pd.DataFrame): DataFrame containing data.
    - category (str): Category to filter the DataFrame.
    """

    category_df = df[df["Category"] == category]

    return len(category_df)


def create_markdown(description):
    """
    Create a styled HTML description with a job count.

    Args:
    - description (str): The description text to display.
    """

    html_content = f"""
     <div style="
         text-align: center; 
         font-size: 20px; 
         font-weight: bold; 
         color: #444444; 
         padding: 18px; 
         background-color: #f0f2f6; 
         border-radius: 5px;
         margin-bottom: 2%;">
         {description}
     </div>
     """

    return html_content
