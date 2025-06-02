import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates= True, index_col= "date")

# Clean data
df = df.loc[
    (df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize= (12, 4.5))

    ax.plot(df.index, df.value, color= "red")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    plt.tight_layout(pad= 2)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]
    df_bar = df_bar.groupby(["year", "month"], sort= False).mean(numeric_only=True).round(2).reset_index()
    filler_table = pd.DataFrame({
            "year": [2016, 2016, 2016, 2016],
            "month": ["January", "February", "March", "April"],
            "value": [0.00,0.00,0.00,0.00]
        })
    df_bar = pd.concat([filler_table, df_bar]).reset_index(drop=True)
    df_bar = df_bar.pivot_table(columns="month", index="year", values="value", sort=False).head(15)
    
    # Draw bar plot
    fig, ax = plt.subplots(figsize= (8, 8))
    width = 0.05
    multiplier = 0
    import numpy as np
    pos = np.arange(len(df_bar.index))

    for month, value in df_bar.items():
        offset= width * multiplier
        ax.bar(pos + offset, value.values, width, label= month)
        multiplier += 1

    ax.set_ylabel("Average Page Views")
    ax.set_xlabel("Years")
    ax.set_xticks(pos + width*5, df_bar.index)
    ax.tick_params(axis= "x", labelrotation= 90)
    ax.legend(loc= "upper left")
    plt.tight_layout(pad= 2)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize= (26, 8))

    order= ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    fig.add_subplot(sns.boxplot(
        data= df_box,
        x= "year",
        y= "value",
        hue= "year",
        ax= ax1,
        legend= False
    ))
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_yticks([x for x in range(0,220000,20000)])

    fig.add_subplot(sns.boxplot(
        data= df_box.sort_values(by= "month"),
        x= "month",
        y= "value",
        hue= "month",
        order= order,
        ax= ax2,
        legend= False
    ))
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_yticks([x for x in range(0,220000,20000)])

    fig.tight_layout(pad= 3)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
