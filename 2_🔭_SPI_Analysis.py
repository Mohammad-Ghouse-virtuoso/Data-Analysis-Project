import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as ptx 
from PIL import Image

st.set_page_config(
        page_title= "SPI Analysis",
        page_icon="🔭"
    ) 
st.markdown("""
<style>
.css-1rs6os.edgvbvh3
{
    visibilty:hidden;
}         
.css-1lsmgbg.egzxvld0
{
    visibility:hidden; 
}
</style>
            
""",unsafe_allow_html=True)
page = st.sidebar.radio("",("📊 SPI ANALYSIS","🍀 Basic Human Needs", "🎨 Wellbeing", " 🎓 Opportunities"))
if page == "📊 SPI ANALYSIS":
    st.title("Hello welcome to SPI Analysis page.")
    image="SPI image(1).jpg"
    col1, col2 = st.columns([1,3])
    with col1:
        st.image(image,width=450)
    st.subheader("The SPI consists of four-parameters: ")
    st.caption("**Basic Human needs:** Understanding our basic human needs is fundamental to fostering a fulfilling life. These needs encompass the essentials required for our physical, emotional, and psychological well-being. From access to clean water and nutritious food to the warmth of human connection, acknowledging and meeting these needs lays the groundwork for a thriving existence.")
    st.caption("**Wellbeing:** Wellbeing encapsulates the holistic state of being content, healthy, and fulfilled. It extends beyond mere physical health to encompass mental and emotional harmony. Cultivating wellbeing involves nurturing positive relationships, pursuing meaningful goals, and prioritizing self-care practices that nourish the mind, body, and spirit.")
    st.caption("**Opportunities:** Opportunity serves as the gateway to personal growth and advancement. It represents the chance for individuals to realize their potential, pursue their aspirations, and contribute meaningfully to society. Embracing opportunities requires resilience, initiative, and an open mindset, empowering individuals to overcome challenges and seize moments that lead to progress and fulfillment.")
    st.caption("**Nutrition-Medical care:** Basic nutrition and medical care are cornerstones of a healthy and thriving community. Access to nourishing food and essential healthcare services not only sustains physical well-being but also fosters resilience and vitality. By ensuring equitable access to these resources, societies can uplift individuals and promote overall prosperity, laying the foundation for a future where everyone can flourish.")
    st.markdown("---")
    # Define your fixed content#3498DB;
    
    summary_card = """
        <div style="padding: 10px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #F7DC6F ;">
            <h2 style="color:#8E44AD ;"> A quick summary</h2>
            <p style="color:#1B2631;">
            <b>Basic Human Needs:</b> Acknowledging and meeting our fundamental needs, including access to clean water, nutritious food, and human connection, is essential for a fulfilling life.<br>
            <b> Wellbeing:</b>Cultivating holistic well-being involves nurturing positive relationships, pursuing meaningful goals, and prioritizing self-care practices that nourish the mind, body, and spirit.<br>
            <b>Opportunities:</b>Embracing opportunities empowers individuals to realize their potential, pursue aspirations, and contribute meaningfully to society, fostering personal growth and societal advancement.<br>
            <b>Nutrition-Medical Care:</b>
            Access to basic nutrition and medical care sustains physical well-being, promotes resilience, and uplifts communities, laying the foundation for a healthy and prosperous future.
            </p>
         </div>
    """
    # Display the summary card
    st.markdown(summary_card,unsafe_allow_html=True)
    #st.subheader('Parameters in Basic Human Needs, on country basis')
elif page=="🍀 Basic Human Needs":
    st.title("🧩 Basic Human needs Insights")
    image='H&W.png'
    st.image(image)
    st.write("\n\n")

    df=pd.read_csv("spi(1).csv")
    st.write(df.head(21))

    limit=70
    high = df[df["spi_score"] > limit]
    lower = df[df["spi_score"] <= limit]

    fig_height=500
    fig_width=300

    tab1, tab2 = st.tabs(["Bar Graph","Line Graph"])
    colors=['Orange','Green','Red','Blue']
    with tab1:
        st.write("Bar Graph visual")
        st.subheader("Countries with High SPI score")
        st.bar_chart(high.set_index('country')['spi_score'],use_container_width=True, height=fig_height,width=fig_width)


        #st.bar_chart(df.set_index("country")["spi_score"])
        st.subheader("Countries with Low SPI score")
        st.bar_chart(lower.set_index('country')['spi_score'],use_container_width=True,height=fig_height,width=fig_width)

    #Line chart on basic human needs by country
    with tab2:
        st.write("Line Graph visual")
        st.subheader("Countries with High SPI score")
        st.line_chart(high.set_index('country')['spi_score'],use_container_width=True,height=fig_height,width=fig_width)

        st.subheader("Countries with low SPI score")
        st.line_chart(lower.set_index('country')['spi_score'],use_container_width=True,height=fig_height,width=fig_width)    
    
    st.markdown("---")
    st.markdown("> ### Stacked bar on Water sanitation, shelter, personal safety by countries")
    grouped_df=df.groupby('country')[['water_sanitation','shelter','personal_safety']].sum().reset_index()

    top_30_df = grouped_df.sort_values(by=['water_sanitation','shelter','personal_safety'], ascending=False).head(30)
    #Melting the dataframe to long form 
    melt_df=pd.melt(top_30_df,id_vars=['country'],var_name='component',value_name='value')
    #stacked chart -------
    chart = alt.Chart(melt_df).mark_bar().encode(
        x='country',
        y='value',
        color='component'
    ).properties(
        width=800,
        height=500,
        title="Stacked Bar chart of Basic Human needs by country"
    )        
    st.write(chart,justify='center')
    st.markdown("---")
    #Scatter Plot for Water Sanitation and Shelter by Country
    st.markdown("> ### Scatterplot on Water sanitation, shelter by countries")
    df['country']= range(1, len(df) + 1)
    Schart=alt.Chart(df).mark_circle().encode(
        x=alt.X('country',title="Country"),
        y=alt.Y('water_sanitation',title="Water Sanitation"),
        size=alt.Size('shelter', scale=alt.Scale(range=[50, 100]), title='Shelter'),
        color=alt.Color('shelter', scale=alt.Scale(scheme='category10'), title='Water Sanitation, Shelter by Country'),
        tooltip=['country','water_sanitation','shelter']
    ).properties(
        width=900,
        height=500,
        title="Scatterplot of Water sanitation by shelter"
    )
    st.write(Schart,justify='center')
    st.markdown("---")
    st.markdown("> ### Heatmap on personal safety and basic nutrirtion by country")
    #Heat map 
    pf=pd.read_csv('spi(2).csv')
    heatmap_data = pf.pivot_table(index='country', values=['personal_safety', 'basic_nutri_med_care'])
    ptx.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt=".2f")
    ptx.title('Heatmap of Personal Safety and Basic Nutrition by Country')
    ptx.xlabel('Parameters')
    ptx.ylabel('Countries')
    ptx.xticks(rotation=45)
    ptx.tight_layout()
    st.pyplot(ptx)
    st.markdown("---")
    # Define the text for the summary card
    #3D Graph
    st.markdown("> ### 3D representation of wellbeing scores")
    data = pd.read_csv("spi(2).csv")  # Replace "your_data.csv" with the path to your CSV file
    # Create a 3D scatter plot
    fig = px.scatter_3d(data, x='basic_human_needs', y='wellbeing', z='opportunity', color='country', size='spi_rank',
                        hover_name='country', size_max=10)

    # Update layout settings
    fig.update_layout(title="3D Map of Countries",
                    scene=dict(xaxis_title='basic_human_needs',
                                yaxis_title='wellbeing',
                                zaxis_title='opportunity'))

    # Display the 3D plot
    st.plotly_chart(fig)
    st.markdown("---")
    st.write("\n\n")
    summary_card = """
        <div style="padding: 10px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #C0C0C0;">
            <h2 style="color:#3498DB ;"> Summary</h2>
            <p style="color:#1B2631;">
            <b>Basic Human Needs:</b>The average score for basic human needs across the dataset is approximately 94.48.
            The scores range from a minimum of 92.46 to a maximum of 96.85, indicating a relatively narrow range of variation.<br>
            <b> Water Sanitation:</b>The average score for water sanitation is approximately 98.17, suggesting high levels of access to clean water and sanitation facilities.<br>
            <b>Shelter:</b> The average score for shelter is approximately 92.91, indicating a relatively high level of adequacy in housing conditions.<br>
            <b>Basic Nutrition and Medical Care:</b>
            The scores range from a minimum of 97.16 to a maximum of 98.99, suggesting consistent access to basic nutrition and medical care across the dataset.
            </p>
        </div>
    """
    # Display the summary card
    st.markdown(summary_card,unsafe_allow_html=True)


elif page == "🎨 Wellbeing":
    st.title("Welcome this is a wellbeing page..")
    st.image('Family_image(1).png')
    df=pd.read_csv('spi(2).csv')
    # Load the data
    Wtab1, Wtab2 = st.tabs(["Bar Graph","Line Graph"])
    colors=['Orange','Green','Red','Blue']
    with Wtab1:
        st.markdown("**Bar graph visual for wellbeing**")
        st.caption("**Countries rank by wellbeing index.**")
        st.bar_chart(df[df["wellbeing"]>0].set_index('country')['wellbeing'],use_container_width=True, height=400,width=600)

    with Wtab2:
        #st.bar_chart(df.set_index("country")["spi_score"])
        st.markdown("**Line graph visual for wellbeing**")
        st.caption("**Countries rank by wellbeing index.**")
        st.line_chart(df[df['wellbeing']>0].set_index('country')['wellbeing'],use_container_width=True,height=400,width=600)
    st.write("\n")
    st.markdown("---")
    #line chart for health and wellness by country health_wellness
    st.markdown("> ### **Line chart for Health & Wellness by country.**")
    fig=px.line(df[df["health_wellness"]>0 ],x='country',y='health_wellness',color_discrete_sequence=['green'],hover_name='health_wellness')

    st.plotly_chart(fig, use_container_width=True,height=500,width=600)
    st.markdown("---")
    #Pie chart for env_quality by country
    st.markdown("> ### **Pie Chart for environment quality by country.**")
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    # Sample data
    # Define colors for each country Bold,G10,prism,
    colors = px.colors.qualitative.Prism_r  # Using built-in Pastel color palette
    # Create a pie chart using Plotly Express
    fig = px.pie(df, values='env_quality', names='country', color='country', color_discrete_sequence=colors)
    # Set title
    fig.update_layout(title='Environmental Quality by Country')
    # Display the pie chart in Streamlit
    st.plotly_chart(fig)
    st.markdown("---")
    #Area chart access_basic_knowledge by country
    st.markdown("> ### Area Chart for environment quality by country.")
    fig=px.area(df, x='country', y='access_basic_knowledge',height=700,width=800)
    fig.update_xaxes(title_text="Country")
    fig.update_yaxes(title_text="Access to education")
    st.plotly_chart(fig,use_container_width=True)
    #Comparision table
    st.markdown("---")
    st.markdown("> ### Comparision table of wellbeing")
    df=pd.read_csv('spi(2).csv')
    dataf=df[['country','access_basic_knowledge','access_info_comm','health_wellness']].head(5)
    dataf.set_index('country',inplace=True)
    st.table(dataf)
    
    st.markdown("---")
    
    #coorelation table 
    # Sample data (replace this with your own data)
    st.markdown("> ### Correlation matrix for Wellbeing")
    datafc=df[['country','access_basic_knowledge','access_info_comm','health_wellness']]
        # Calculate the correlation matrix
    correlation_matrix = datafc.corr()
         # Display the correlation matrix
    st.write("Correlation Matrix:")
    st.write(correlation_matrix)

    # Create a heatmap using Plotly Express
    st.markdown("> ### Heatmap representation on wellbeing factors")
    fig = px.imshow(correlation_matrix, labels=dict(x="Wellbeing Factors", y="Wellbeing Factors", color="Correlation"))
    fig.update_layout(title="Correlation Analysis between Wellbeing Factors")
    st.markdown("---")
    st.plotly_chart(fig)

    st.markdown("---")
    st.markdown("> ### Geographical map representation on wellbeing scores")
        # Sample data (replace this with your own data)
    data = pd.read_csv('spi(1).csv')
        # Create a geographical map using Plotly Express
    fig = px.scatter_geo(data, locations=data['country'], locationmode='country names', 
                        color='wellbeing', hover_name='country', 
                        size='wellbeing', projection='natural earth')

    # Customize the map layout
    fig.update_layout(title='Wellbeing Scores by Country',
                    geo=dict(showcoastlines=True, showland=True, showocean=True, showlakes=True))

    # Display the map in Streamlit
    st.plotly_chart(fig)
    st.markdown("---")
    summary_card = """
        <div style="padding: 10px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #C0C0C0;">
            <h2 style="color:#3498DB ;"> Summary</h2>
            <p style="color:#1B2631;">
            <b>Wellbeing:</b>The wellbeing scores range from 88.12 to 93.8,The average wellbeing score is approximately 91.47,Overall, the population appears to have relatively high levels of wellbeing.<br>
            <b> Access to Information and Communication:</b>Access to information and communication scores range from 87.97 to 98.18.The average access to information and communication score is approximately 94.22.<br>
            <b>Health and Wellness:</b>Health and wellness scores range from 82.32 to 92.63.The average health and wellness score is approximately 87.83.<br>
            <b>Environmental Quality:</b>Environmental quality scores range from 80.41 to 95.15.The average environmental quality score is approximately 87.81.
            </p>
        </div>
    """
    # Display the summary card
    st.markdown(summary_card,unsafe_allow_html=True)



else:
    st.markdown("# Welcome to the opportunities analysis page.")
    st.image('Mother_daughter.png') 
    df=pd.read_csv('spi(2).csv')
    Otab1, Otab2 = st.tabs(["Bar Graph","Line Graph"])
    colors=['Orange','Green','Red','Blue']
    with Otab1:
        st.markdown("**Bar graph visual for opportunities**")
        st.caption("**Countries rank by  opportunities index.**")
        st.bar_chart(df[df["opportunity"]>0].set_index('country')['opportunity'],use_container_width=True, height=400,width=600)

    with Otab2:
        #st.bar_chart(df.set_index("country")["spi_score"])
        st.markdown("**Line graph visual for opportunity**")
        st.caption("**Countries rank by opportunity index.**")
        st.line_chart(df[df['opportunity']>0].set_index('country')['opportunity'],use_container_width=True,height=400,width=600)
    
    st.markdown("___")
    #line chart on personal_rights by countries
    st.markdown("> ### **Line chart for personal rights by country.**")
    st.caption("**Countries rank by personal rights index.**")
    fig=px.line(df[df["health_wellness"]>0 ],x='country',y='personal_rights',color_discrete_sequence=['yellowgreen'],hover_name='personal_rights')
    st.plotly_chart(fig, use_container_width=True,height=500,width=600)
    
    st.markdown("___")
    
    #Bar_chart by personal_freedom_choice by country
    st.markdown("> ### **Bar graph visual for personal freedom choice**")
    st.caption("**Countries rank by personal freedom choice index.**")
    st.bar_chart(df[df["personal_freedom_choice"]>0].set_index('country')['personal_freedom_choice'],use_container_width=True, height=400,width=600)

    st.markdown("___")

    #Comparision table of opportunities
    st.markdown("> ### Comparision table of opportunities")
    df=pd.read_csv('spi(2).csv')
    dataOppor=df[['country','personal_freedom_choice','personal_rights','access_adv_edu']].head(5)
    dataOppor.set_index('country',inplace=True)
    st.table(dataOppor)
    st.write("\n")
    st.markdown("---")

    #Area chart on components of opportunities
    st.markdown("> ### **Area Chart for adanvce education of opportunities**")
    fig=px.area(df, x='country', y='access_adv_edu',height=700,width=800)
    fig.update_xaxes(title_text="Country")
    fig.update_yaxes(title_text="Access to Advance education")
    st.plotly_chart(fig,use_container_width=True)

    st.markdown("___")

    #Heatmap personal_freedom_choice by country
    pf=pd.read_csv('spi(2).csv')
    heatmap_data = pf.pivot_table(index='country', values=['personal_rights','personal_freedom_choice','access_adv_edu'])
    ptx.figure(figsize=(12, 7))
    sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt=".2f")
    ptx.title('Heatmap of personal_freedom_choice by Country')
    ptx.xlabel('Parameters')
    ptx.ylabel('Countries')
    ptx.xticks(rotation=45)
    ptx.tight_layout()
    st.pyplot(ptx)

    st.write("\n")
    st.markdown("___")

    #Geographical data on opportunities
    st.markdown("> ### Geographical map representation on opportunities scores")
    # Sample data (replace this with your own data)
    data = pd.read_csv('spi(1).csv')
    # Create a geographical map using Plotly Express
    fig = px.scatter_geo(data, locations=data['country'], locationmode='country names', 
                        color='opportunity', hover_name='country', 
                        size='opportunity', projection='natural earth')
    # Customize the map layout
    fig.update_layout(title='Wellbeing Scores by Country',
                    geo=dict(showcoastlines=True, showland=True, showocean=True, showlakes=True))

    # Display the map in Streamlit
    st.plotly_chart(fig)
    st.markdown("---")
    # Define the text for the summary card

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt

    # Sample data (replace this with your own data)
    data = pd.read_csv('spi(2).csv')

    # Allow user to select columns for histogram, ['opportunity','personal_freedom_choice','personal_rights','access_adv_edu'])
    selected_columns = st.multiselect(label="Select columns for histogram", options=data.columns.tolist())

    if selected_columns:
        # Generate histograms for each selected attribute
        num_cols = len(selected_columns)
        num_rows = (num_cols + 1) // 2  # Ensure even distribution of subplots

        fig, axes = plt.subplots(nrows=num_rows, ncols=2, figsize=(10, 8*num_rows))
        axes = axes.flatten()  # Flatten axes for easier indexing

        for i, column in enumerate(selected_columns):
            ax = axes[i]
            data[column].hist(ax=ax, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
            ax.set_title(f'{column} Histogram')
            ax.set_xlabel('Score')
            ax.set_ylabel('Frequency')

        # Remove any extra unused subplots
        for ax in axes[num_cols:]:
            ax.remove()

        # Adjust layout
        plt.tight_layout()

        # Display the histogram in Streamlit
        st.pyplot(fig)
    else:
        st.warning("Please select columns for histogram")

    st.markdown("---")
    summary_card = """
    <div style="padding: 10px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #C0C0C0;">
        <h2 style="color:#3498DB ;"> Summary</h2>
        <p style="color:#1B2631;">
        <b>Opportunity:</b>The opportunity scores range from 80.36 to 89.3.The average opportunity score is approximately 85.53.<br>
        <b>Personal Rights:</b>Personal rights scores range from 91.43 to 97.71.The average personal rights score is approximately 95.36.<br>
        <b>Personal Freedom of Choice:</b>Personal freedom of choice scores range from 79.39 to 90.65.The average personal freedom of choice score is approximately 86.41.<br>
        <b>Access to Advanced Education:</b>Access to advanced education scores range from 65.99 to 88.77.The average access to advanced education score is approximately 81.43.
        </p>
    </div>
    """
    # Display the summary card
    st.markdown(summary_card,unsafe_allow_html=True)
