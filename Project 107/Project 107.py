import pandas as pd
import plotly.graph_objects as pgo
import plotly_express as px

df = pd.read_csv('data.csv')
std_df = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()

fig = px.scatter(std_df, x="student_id", y="level", size = "attempt", color = "attempt")
fig.show()