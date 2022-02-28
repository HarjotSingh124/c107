
import pandas  as pd 
import csv
import plotly.express as px

df = pd.read_csv("data.csv")

fig =px.scatter(
            x="student_id",
            y="level",
            size = df.groupby("level")["attempt"].mean(),
            color = "attempt",
            size_max= 100
            )

fig.show()