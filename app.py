import streamlit as st
import time

from utils.helper_functions import load_data, count_jobs, create_markdown
from utils.plots import plot_top_technologies, plot_education, plot_experience, plot_top_technologies_funnel, \
    plot_gauge_chart


# Page configuration
st.set_page_config(
    page_title="Skill Scope",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded")

# Load data
with st.spinner("Loading data..."):
    time.sleep(1)
    data = load_data("data/processed/data_processed.csv")

# Sidebar
with st.sidebar:
    st.sidebar.image("style/logo.png", use_column_width=True)

    category_list = data["Category"].unique()

    selected_category = st.selectbox("Select a category", category_list)

    job_count = count_jobs(data, selected_category)

    st.markdown("---")

    st.subheader("Info")
    st.markdown("[Project Repository](https://github.com/georgescutelnicu/Skill-Scope/)")

    st.markdown("---")

    st.subheader("Links")
    st.markdown("[GitHub](https://github.com/georgescutelnicu)")
    st.markdown("[Kaggle](https://www.kaggle.com/georgescutelnicu)")
    st.markdown("[HuggingFace](https://huggingface.co/georgescutelnicu)")
    st.markdown("[Personal Website](https://georgescutelnicu.github.io/)")

# Layout
st.markdown(create_markdown(f"Analyzing {selected_category} trends across {job_count} jobs"), unsafe_allow_html=True)

col = st.columns((1, 2, 1), gap='large')

with col[0]:
    fig = plot_education(data, selected_category)
    st.plotly_chart(fig)

    fig = plot_top_technologies_funnel(data, selected_category, "Clouds", 3)
    st.plotly_chart(fig)

    fig = plot_gauge_chart(data, selected_category, "jobs")
    st.plotly_chart(fig)

with col[1]:
    fig = plot_top_technologies(data, selected_category, "Languages", 10)
    st.plotly_chart(fig)

    fig = plot_top_technologies(data, selected_category, "Technologies", 10)
    st.plotly_chart(fig)

    fig = plot_top_technologies(data, selected_category, "Databases", 8)
    st.plotly_chart(fig)

with col[2]:
    fig = plot_experience(data, selected_category)
    st.plotly_chart(fig)

    fig = plot_top_technologies_funnel(data, selected_category, "Tools", 3, "right")
    st.plotly_chart(fig)

    fig = plot_gauge_chart(data, selected_category, "applicants")
    st.plotly_chart(fig)

with st.expander('About', expanded=True):
    st.write('''
        **Skill Scope Dashboard**

        This dashboard is designed to analyze job market trends in Romania across various categories.

        **Data Source**

        The data used in this dashboard is sourced from [LinkedIn](https://ro.linkedin.com/) 
        and it was scraped on June 24, 2024.\n
        Please be aware that job market trends can change rapidly.

        **Technologies Used**

        BeautifulSoup, Pandas,  Plotly, Streamlit.
    ''')

# Load css file
with open("style/styles.css") as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
