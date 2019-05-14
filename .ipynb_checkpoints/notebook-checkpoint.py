# %%
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

# %%
import pandas as pd
import numpy as np

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# %%
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# %%
df = pd.read_csv("1500m.csv")

# %%
split_points = [str(i*100) for i in range(1, 16)]
split_points

# %%
def convert(x):
    if ":" in str(x):
        m, s = x.split(":")
        return int(m)*60 + float(s)
    else:
        try:
            return float(x)
        except:
            return np.nan

for pt in split_points:
    df[pt+"_sec"] = df[pt].apply(convert)

# %%
for i, pt1 in enumerate(reversed(split_points)):
    for pt2 in list(reversed(split_points))[i+1:]:
        df[pt1+"-"+pt2] = df[pt1+"_sec"] - df[pt2+"_sec"]

# %%
for c in df.columns.tolist():
    if "-" in c:
        df[c+"_normed"] = df[c]/df["1500_sec"]

# %%
sec_cols = [col for col in df.columns.tolist() if "sec" in col]
df.loc[:, sec_cols] = df[sec_cols].interpolate(axis=1)

# %%
init_notebook_mode(connected=True)

layout = go.Layout(
    autosize=False,
    width=1000,
    height=500,
    plot_bgcolor = '#E5E5E5',
    paper_bgcolor = '#E5E5E5',
)

dimensions = []
for col in ["300_sec", "500_sec", "700_sec", "900_sec", "1100_sec", "1300_sec", "1500_sec"]:
    dimensions += [
        dict(range=[df[col].min(), df[col].max()],
             label=col,
             values=df[col].values)
    ]


data = [
    go.Parcoords(
        line=dict(color='blue'),
        dimensions=dimensions
    )
    
]

fig = go.Figure(data=data, layout=layout)

plotly.offline.iplot(fig, filename = 'parcoord-dimensions')

# %%
plotly.offline.plot(fig, filename = 'parcoord-dimensions')

# %%
init_notebook_mode(connected=True)

layout = go.Layout(
    autosize=False,
    width=1000,
    height=500,
    plot_bgcolor = '#E5E5E5',
    paper_bgcolor = '#E5E5E5',
)

dimensions = []
for col in ["300-100", "500-300", "700-500", "900-700", "1100-900", "1300-1100", "1500-1300", "1500_sec"]:
    dimensions += [
        dict(range=[df[col].min(), df[col].max()],
             label=col,
             values=df[col].values)
    ]


data = [
    go.Parcoords(
        line=dict(color='blue'),
        dimensions=dimensions
    )
    
]

fig = go.Figure(data=data, layout=layout)

plotly.offline.iplot(fig, filename = 'parcoord-dimensions')

# %%
plt.figure(figsize=(20, 10))
plt.title("percentage of time spent in segment")
sns.violinplot(data=df[[
    "300-100_normed",
    "500-300_normed",
    "700-500_normed",
    "900-700_normed",
    "1100-900_normed",
    "1300-1100_normed",
    "1500-1300_normed"]]*100)


# %%
df["categ"] = pd.qcut(df["1500_sec"], 3, labels=["blue", "green", "orange"])

# %%
df["100_sec_normed"] = df["100_sec"]/df["1500_sec"]

# %%
cols1 = ["100_sec_normed", "200-100_normed", "300-200_normed",
         "400-300_normed", "500-400_normed", "600-500_normed",
         "700-600_normed", "800-700_normed", "900-800_normed",
         "1000-900_normed", "1100-1000_normed", "1200-1100_normed",
         "1300-1200_normed", "1400-1300_normed", "1500-1400_normed"]

cols = cols1+["categ"]

plt.figure(figsize=(20, 10))

def plot_row(row):
    plt.plot(row[cols1], color=row["categ"], alpha=0.3, marker="o")

(df[cols]).apply(plot_row, axis=1)
plt.show()

# %%
cols1 = ["300_sec", "400_sec",
         "500_sec", "600_sec", "700_sec", "800_sec",
         "900_sec", "1000_sec", "1100_sec", "1200_sec",
         "1300_sec", "1400_sec", "1500_sec"]

init_notebook_mode(connected=True)

layout = go.Layout(
    autosize=False,
    width=1000,
    height=500,
    plot_bgcolor = '#E5E5E5',
    paper_bgcolor = '#E5E5E5',
)

dimensions = []
for col in cols1:
    dimensions += [
        dict(range=[df[col].min(), df[col].max()],
             label=col,
             values=df[col].values)
    ]


data = [
    go.Parcoords(
        line=dict(color='blue'),
        dimensions=dimensions
    )
    
]

fig = go.Figure(data=data, layout=layout)

plotly.offline.iplot(fig, filename = 'parcoord-dimensions')

# %%
plotly.offline.plot(fig, filename = 'parcoord-dimensions')

# %%
cols1 = ["100_sec", "200_sec", "300_sec", "500_sec", "700_sec", "900_sec", "1100_sec", "1300_sec", "1500_sec"]
cols = cols1+["categ"]

plt.figure(figsize=(20, 10))

def plot_row(row):
    plt.plot(row[cols1], color=row["categ"], alpha=0.3, marker="o")

(df[cols]).apply(plot_row, axis=1)
plt.show()

# %%
