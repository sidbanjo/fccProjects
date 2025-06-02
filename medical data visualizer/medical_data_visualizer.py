import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (df.weight / (df.height/100)**2).map(lambda x : 0 if x <= 25 else 1)

# 3
df[["cholesterol", "gluc"]] = df[["cholesterol", "gluc"]].applymap(lambda x : 1 if x > 1 else 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt("cardio", ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # 6
    df_cat = df_cat.groupby("cardio").value_counts().reset_index().rename(columns={0: "total"}).sort_values("variable")
    

    # 7
    plot_bar = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar")


    # 8
    fig = plot_bar.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[
        (df.ap_lo <= df.ap_hi) &
        (df.height >= df.height.quantile(0.025)) &
        (df.height <= df.height.quantile(0.975)) &
        (df.weight >= df.weight.quantile(0.025)) &
        (df.weight <= df.weight.quantile(0.975))
    ]


    # 12
    corr = df_heat.corr().round(1)


    # 13
    mask = np.triu(np.ones_like(corr))



    # 14
    fig, ax = plt.subplots(layout= "tight")

    # 15
    fig.add_subplot(sns.heatmap(
        corr,
        mask= mask,
        ax= ax,
        fmt= ".1f",
        annot= True,
        linewidths= 1,
        cbar_kws= {"ticks": [-0.08, 0.00, 0.08, 0.16, 0.24], "shrink": 0.5},
        vmax= 0.32,
        vmin= -0.16,
        center= 0,
        annot_kws= {"size": 6}
        ))


    # 16
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()