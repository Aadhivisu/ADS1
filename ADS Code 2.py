import pandas as pd #header file
import matplotlib.pyplot as plt #used for visualize data effectively 
import seaborn as sns #is used to leverage Seaborn's capabilities for nformative, and statistically relevant visualizations in Python.

def filter_and_process_data(indicator, countries):
    ''''''
    df = pd.read_csv('API2.csv', skiprows=4) # To read the data in given file name   
    filtered_data = df[(df["Indicator Name"] == indicator) & (df['Country Name'].isin(countries))]
    filtered_data = filtered_data.drop(['Country Code', 'Indicator Name', 'Indicator Code', 
                                        '1960', '1961', '1962', '1963', '1964', '1965', '1966', 
                                        '1967', '1968', '1969', '1970', '1971', '1972', '1973', 
                                        '1974', '1975', '1976', '1977', '1978', '1979', '1980', 
                                        '1981', '1982', '1983', '1984', '1985', '1986', '1987', 
                                        '1988', '1989', '1990', '1991', '1992', '1993', '1994', 
                                        '1995', '1996', '1997', '1998', '1999', '2021', '2022', 
                                        'Unnamed: 67'], axis=1).reset_index(drop=True) # filtered data is for filtering the data what we need
    data_t = filtered_data.transpose()#Transposing data can be useful in various scenarios, especially when the orientation of the data needs to be changed for easier analysis
    data_t.columns = data_t.iloc[0]
    data_t = data_t.iloc[1:]
    data_t.index = pd.to_numeric(data_t.index) #Converting the index to numeric values can be beneficial when you need to perform mathematical operations
    data_t['Years'] = data_t.index
    data_t.reset_index(drop=True)
    return filtered_data, data_t    

def lineplot(linePlotData, title): # To create a line plot for give data 
    '''Create a line plot using Seaborn.

    Parameters:
    - data: A dictionary where keys are labels for
    the line plots and values are lists of data points.
    - countries: List of country names to be included in the line plot.
    """'''
    plt.figure() # used to plot the figure 
    linePlotData.plot(x='Years', y=['Australia', 'China', 'Finland', 'India', 'United Kingdom'], kind='line', figsize=(10, 4), marker='o')
    plt.title(title) # used to represent the title name
    plt.xticks(range(2000, 2021, 2)) # used to define the range
    plt.xlabel('Years') # X label name
    plt.ylabel('Countries') # Y label name 
    plt.legend() # when multiple datasets or different aspects of data need to be visualized together, as it helps in clarifying
    plt.show() # To show the data


def barplot(df, x_value, y_value, head_title, x_label, y_label, colors=('blue', 'yellow', 'orange', 'brown', 'green')): #To create barplot using Seaborn
    '''Create a bar plot using Seaborn.

    Parameters:
    - data: A dictionary where keys are labels for the bar plots and values are lists of data points.
    - countries: List of country names to be included in the bar plot.
    """'''
    plt.figure(figsize=(10, 4)) #To describe the Figure size 
    df_filtered = df[df['Years'].isin([2000, 2004, 2008, 2012, 2016, 2020])] #Filtring process
    df_filtered.plot(x=x_value, y=y_value, kind='bar', title=head_title, color=colors, width=0.65, figsize=(10,7), xlabel=x_label, ylabel=y_label)
    plt.legend(loc='best', bbox_to_anchor=(1, 0.4)) # when multiple datasets or different aspects of data need to be visualized together, as it helps in clarifying
    plt.show
    
def create_box_plot(data, countries): #to create a box plot using seaborn
    """
    Create a box plot using Seaborn.

    Parameters:
    - data: A dictionary where keys are labels for the box plots and values are lists of data points.
    - countries: List of country names to be included in the box plot.
    """
    sns.set(style="whitegrid") # to context of your data visualization
    plt.figure(figsize=(10, 6))

    # Convert the data dictionary to a Pandas DataFrame
    df = pd.DataFrame({country: data[country] for country in countries})

    # Create box plot
    sns.boxplot(data=df)

    plt.xlabel('Country') #X label name
    plt.ylabel('Value') #Y label name
    plt.title('CO2 emissions (kg per PPP $ of GDP') # used to represent the title name
    plt.show()

    
def create_pieplot(df, years, label_names= ['Algeria', 'Brazil', 'Spain', 'India', 'Nepal'], autopct='%1.0f%%', fontsize=11):
    '''Create a pieplot using Seaborn.

    Parameters:
    - data: A dictionary where keys are labels for the pie plots and values
    are lists of data points.
    - countries: List of country names to be included in the pie plot.
    """'''
    plt.figure(figsize=(4, 5)) # figuresize
    plt.pie(df[str(years)], autopct=autopct, labels=label_names, startangle=180, wedgeprops={"edgecolor": "black", "linewidth": 2, "antialiased": True},)
    plt.title(f'Arable land in {years}', fontsize=fontsize) #used to represent the title name
    plt.savefig('pieplot.png') #providing a specific path can be done by modifying the string parameter
    plt.show()


def slicing(df): #This function is useful when you need to focus on specific columns within a DataFrame for slicing it.
    df = df[['Country Name', '2008']]
    return df

def merge(d1, d2, d3, d4): #Its is used to merge the data 
    merge1 = pd.merge(d1, d2, on='Country Name', how='outer')
    merge2 = pd.merge(merge1, d3, on='Country Name', how='outer')
    merge3 = pd.merge(merge2, d4, on='Country Name', how='outer')
    merge3 = merge3.reset_index(drop=True)
    return merge3


def create_correlation_heatmap(data, title):
    """
    Create a correlation heatmap.

    Parameters:
    - data: A Pandas DataFrame containing the data 
    for which you want to calculate the correlation.
    - title: Title of the heatmap.
    """
    plt.figure(figsize=(7, 5))
    numeric_df = data.select_dtypes(include='number')
    
    # Calculate the correlation matrix
    correlation_matrix = numeric_df.corr()
    
    # Create a heatmap using Seaborn
    sns.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt='.2f', linewidths=.5)
    
    plt.title(title)
    plt.show()


country_list = ['Australia', 'China', 'Finland', 'India', 'United Kingdom']
data1, data1_t = filter_and_process_data('CO2 emissions (kg per PPP $ of GDP)', country_list)
data2, data2_t = filter_and_process_data('Access to electricity (% of population)', country_list)
data3, data3_t = filter_and_process_data('Arable land (% of land area)', country_list)
data4, data4_t = filter_and_process_data('Agriculture, forestry, and fishing, value added (% of GDP)', country_list)




data1_cor = slicing(data1).rename(columns={'2008': 'Agriculture'})
data2_cor = slicing(data2).rename(columns={'2008': 'Arable'})
data3_cor = slicing(data3).rename(columns={'2008': 'Co2 Emission'})
data4_cor = slicing(data4).rename(columns={'2008': 'Access to electricity'})

data_merged = merge(data1_cor, data2_cor, data3_cor, data4_cor ) #Data is merged and ready to describe 

data_merged.describe() # I have described the data that is merged 


lineplot(data4_t, "Agriculture, forestry, and fishing")  #data for line plot

barplot(data3_t, 'Years', ['Australia', 'China', 'Finland', 'India', 'United Kingdom'], 
        'Arable Land', 'Years', 'y axis', ('red', 'brown', 'green', 'blue', 'orange')) #data for bar plot 
  
create_box_plot(data1_t, country_list) #data for box plot 
 
# Function definition for pie plot
create_pieplot(data2, '2020') # data for pieplot

# Function definition for correlation heatmap
create_correlation_heatmap(data_merged, "Correlation Heatmap for CO2 Emissions")

