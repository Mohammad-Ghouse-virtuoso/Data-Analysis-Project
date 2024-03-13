import streamlit as st

st.set_page_config(
    page_title= "About us",
    page_icon="🗨️"
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
st.title("Hello welcome to About us page.")
summary_text = """
        <div style="padding: 10px; border: 1px solid #e0e0e0; border-radius: 10px; margin-bottom:20px; background-color: #D1F2EB;">
            <h3 style="color:#A93226;">About us</h3>
            <b style="color:#17202A;">Data analysis and data science are crucial components in today's rapidly evolving digital landscape. In our data analysis project, we are dedicated to exploring the depths of these fields, utilizing the power of Python and cutting-edge libraries to uncover valuable insights and trends. With a professional approach and a passion for data-driven decision-making, we strive to provide our best with the latest advancements and best practices in the world of data analysis. 
            </b>
        </div>
    """
##A2D9CE, #F7DC6F ,#FFC300
# Display the summary card
st.markdown(summary_text, unsafe_allow_html=True)
st.image('14985.jpg')
# Set up the layout with rows and columns
col1, col2 = st.columns(2)  # Create two columns
# Define the content for each card
with col1:
    st.write(
        """
        <div style="padding: 20px; margin-bottom: 20px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #f9f9f9;">
            <h3 style="color: #333333; font-size: 20px;">Team Member 1</h3>
            <p style="color: #666666; font-size: 16px;">K.S.Mohammad Ghouse<br>
            3BR21CS065, CSE-A sec <br>
            BITM, Ballari
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.write(
        """
        <div style="padding: 20px; margin-bottom: 20px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #f9f9f9;">
            <h3 style="color: #333333; font-size: 20px;">Team Member 2</h3>
            <p style="color: #666666; font-size: 16px;">Karthik K<br>
            3BR21CS068, CSE-A sec <br>
            BITM, Ballari
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col1:
    st.write(
        """
        <div style="padding: 20px; margin-bottom: 20px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #f9f9f9;">
            <h3 style="color: #333333; font-size: 20px;">Team Member 3</h3>
            <p style="color: #666666; font-size: 16px;">Hanumantha B K<br>
            3BR21CS050, CSE-A sec <br>
            BITM, Ballari
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.write(
        """
        <div style="padding: 20px; margin-bottom: 20px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #f9f9f9;">
            <h3 style="color: #333333; font-size: 20px;">Team Member 4</h3>
            <p style="color: #666666; font-size: 16px;">K Manikanta<br>
            3BR21CS069, CSE-A sec <br>
            BITM, Ballari
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col1:
    st.write(
        """
        <div style="padding: 20px; margin-bottom: 20px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #f9f9f9;">
            <h3 style="color: #333333; font-size: 20px;">Team Member 5</h3>
            <p style="color: #666666; font-size: 16px;">J Manoj<br>
            3BR21CS056, CSE-A sec <br>
            BITM, Ballari
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
#Mrs.Alekya<br>Mrs.Steffi Nivedita Asst.Prof, CSE Dept.
with col2:
    st.write(
        """
        <div style="padding: 20px; margin-bottom: 20px; border: 1px solid #e0e0e0; border-radius: 10px; background-color: #f9f9f9;">
            <h3 style="color: #333333; font-size: 20px;">Designated Faculty:</h3>
            <p style="color: #666666; font-size: 16px;">Mrs.Alekya<br>Mrs.Steffi Nivedita<br>BITM, Ballari
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

import streamlit as st

# Define the footer content
footer_content = """
<footer style="background-color: #17202A; padding: 10px; text-align: center;">
    <p style="margin: 0;">Copyright © 2024 SPI analysis. All rights reserved.</p>
    <p style="margin: 0;">Designed with ❤️ by CSE A-Sec</p>
</footer>
"""

# Display the footer
st.markdown(footer_content, unsafe_allow_html=True)


import streamlit as st

# Define the list of contributors
contributors = [
    {"name": "Institute for comptetiveness", "source": "https://www.socialprogress.org/india"},
    {"name": "Streamlit community", "source": "https://docs.streamlit.io"},
    {"name": "Dataset reference", "source": "https://amankharwal.medium.com"}
]

# Display the interactive credits
st.title("Credits")
st.markdown("---")
# Iterate over the list of contributors
for contributor in contributors:
    # Display contributor name and role
    st.write(f"**{contributor['name']}** - {contributor['source']}")
    
    # Add a clickable link to the contributor's GitHub profile
    #github_link = f"[GitHub](https://github.com/{contributor['github']})"
    #st.write(f"GitHub: {github_link}")

    # Add a separator between contributors
    st.markdown("---")
