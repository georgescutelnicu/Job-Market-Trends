import pandas as pd
import plotly.express as px
from collections import Counter


def plot_top_technologies(df, category, tech_column, n):
    """
    Plot a bar chart showing the top n technologies based on their occurrences in the specified column.

    Args:
    - df (pd.DataFrame): DataFrame containing data.
    - category (str): Category to filter the DataFrame.
    - tech_column (str): Column name containing data.
    - n (int): Number of top technologies to plot.
    """

    # Prepare data
    category_df = df[df["Category"] == category]

    all_technologies = []
    for technologies in category_df[tech_column]:
        all_technologies.extend(eval(technologies))
    tech_counter = Counter(all_technologies)
    top_technologies = tech_counter.most_common(n)

    total_count = sum(tech_counter.values())

    tech_df = pd.DataFrame(top_technologies, columns=["Technology", "Count"])
    tech_df["Percentage"] = (tech_df["Count"] / total_count) * 100

    # Create the Plotly bar chart
    fig = px.bar(tech_df, x="Technology", y="Count", text="Percentage",
                 title=f"Top {n} {tech_column} in {category}")

    fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside",
                      marker_color="skyblue", marker_line_color="black",
                      hovertemplate="Technology: %{x}<br>Count: %{y}<br>Percentage: %{text:.2f}%")

    fig.update_layout(
        title={"x": 0.5, "xanchor": "center"},
        template="simple_white",
        xaxis=dict(tickangle=-45, title=""),
        yaxis=dict(title=""),
        hoverlabel=dict(
            bgcolor="black",
            font_size=14,
            font_color="white"
        )
    )

    return fig


def plot_education(df, category):
    """
    Plot a donut chart showing the distribution of 'degree' and 'without degree' education status.

    Args:
    - df (pd.DataFrame): DataFrame containing education data.
    - category (str): Category to filter the DataFrame.
    """

    # Prepare data
    category_df = df[df["Category"] == category]

    value_counts = category_df["Education"].value_counts()
    with_degree = value_counts.get("['degree']")
    without_degree = value_counts.get("[]")

    total_count = len(category_df)
    with_degree_percent = (with_degree / total_count) * 100
    without_degree_percent = (without_degree / total_count) * 100

    data = {
        "Education Status": ["Mentioned", "Not Mentioned"],
        "Count": [with_degree, without_degree],
        "Percentage": [with_degree_percent, without_degree_percent]
    }
    edu_df = pd.DataFrame(data)

    # Create the Plotly donut chart
    fig = px.pie(edu_df, names="Education Status", values="Count", hole=0.5)

    fig.update_traces(textposition="inside", textinfo="percent+label", marker=dict(colors=["skyblue", "aliceblue"]),
                      hovertemplate="Status: %{label}<br>Count: %{value}<br>Percentage: %{percent}")

    fig.update_layout(
        annotations=[dict(text="Bachelor's Degree", font_size=15, showarrow=False)],
        showlegend=False,
        template="simple_white",
        hoverlabel=dict(
            bgcolor="black",
            font_size=14,
            font_color="white"
        )
    )

    return fig


def plot_experience(df, category):
    """
    Plot a donut chart showing the distribution of experience levels: Intern, Executive, Senior, Mid, Junior.

    Args:
    - df (pd.DataFrame): DataFrame containing experience data.
    - category (str): Category to filter the DataFrame.
    """

    # Prepare data
    category_df = df[df["Category"] == category]

    value_counts = category_df["Experience"].value_counts()
    levels = ["Intern", "Executive", "Senior", "Mid", "Junior"]
    counts = [value_counts.get(level, 0) for level in levels]

    total_count = sum(counts)
    percentages = [(count / total_count) * 100 for count in counts]

    data = {
        "Experience Level": levels,
        "Count": counts,
        "Percentage": percentages
    }
    exp_df = pd.DataFrame(data)

    # Create the Plotly donut chart
    fig = px.pie(exp_df, names="Experience Level", values="Count", hole=0.5)

    fig.update_traces(textposition="inside", textinfo="percent+label",
                      marker=dict(colors=["darkslateblue", "darkblue", "steelblue", "skyblue", "powderblue"]),
                      hovertemplate="Level: %{label}<br>Count: %{value}<br>Percentage: %{percent}",
                      textfont_color="white")

    fig.update_layout(
        annotations=[dict(text="Experience Levels", font_size=15, showarrow=False)],
        showlegend=False,
        template="simple_white",
        hoverlabel=dict(
            bgcolor="black",
            font_size=14,
            font_color="white"
        )
    )

    return fig
