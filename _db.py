import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Dashboard", page_icon=":tada:", layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
#Title of Dashboard
st.title("****Countries GDP****")
#Headers Tabs with styling
selected = option_menu(
        menu_title=None,
        options=["Home", "Data Info", "Data Visualization"],
        icons=["map", "info-lg", "graph-up"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "red", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "green"},
        })

# Loading Dataset
data = pd.read_csv(r"Countries GDP 1960-2020.csv")
df = data.drop(["2018", "2019", "2020"], axis=1)

#### Tab 1
if selected == "Home":
    st.write(f"### ***Life Expectancy and GDP per capital of Countries***")
    df = px.data.gapminder()
    #Geographical Map
    map_fig = px.scatter_geo(df,
                             locations='iso_alpha',
                             projection='orthographic',
                             color='continent',
                             opacity=.8,
                             hover_name='country',
                             hover_data=['lifeExp', "gdpPercap"]
                             )
    st.plotly_chart(map_fig)

#### Tab 2
if selected == "Data Info":
    st.write(f"#### ***{selected}***")
    if st.checkbox("View Dataset"):
        st.dataframe(df)
    st.write("##### Our data is of the shape :", df.shape)
    col1,col2 = st.columns(2)
    with col1:
        st.write("##### Columns :")
        all_columns = df.columns.to_list()
        st.dataframe(all_columns)
        st.text("")
        st.write("##### Please select the columns you want to view")
        selected_columns = st.multiselect("Column Names", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)
    with col2:
        st.write("##### Below is the description of our Dataset:")
        st.write(df.describe())

#### Tab 3
if selected == "Data Visualization":
    col1, col2 = st.columns(2)
    st.write(f"### ***{selected}***")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select Type of Plot", ["Area Chart", "Bar Chart", "Line Chart",  "hist", "box", "kde"])
    selected_columns_names = st.multiselect("Select Columns To Plot", all_columns_names)
    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

        if type_of_plot == "Area Chart":
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)
        elif type_of_plot == "Bar Chart":
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)
        elif type_of_plot == "Line Chart":
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)
        elif type_of_plot:
            cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()










