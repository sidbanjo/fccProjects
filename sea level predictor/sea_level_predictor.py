import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", parse_dates= True)
    df["NOAA Adjusted Sea Level"]= df["NOAA Adjusted Sea Level"].fillna(0.00)

    # Create scatter plot
    fig, ax = plt.subplots(layout= "constrained")
    ax.scatter("Year", "CSIRO Adjusted Sea Level", data= df)
    ax.set_xlim(right= 2060)

    # Create first line of best fit
    regr = linregress(x= df["Year"], y= df["CSIRO Adjusted Sea Level"])
    year_ext = [x for x in range(df.Year.min(), 2051)]
    yline_data = []
    for x in year_ext:
        yline_data.append(regr.slope * x + regr.intercept)
    ax.plot(year_ext, yline_data)

    # Create second line of best fit
    predict_df = df.query("Year >= 2000")
    predict_regr = linregress(x= predict_df["Year"], y= predict_df["CSIRO Adjusted Sea Level"])
    predict_year = [x for x in range(2000, 2051)]
    predict_yline_data = []
    for x in predict_year:
        predict_yline_data.append(predict_regr.slope * x + predict_regr.intercept)
    ax.plot(predict_year, predict_yline_data)

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()