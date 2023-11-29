import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

'''column_name = 'Topic'

    # Read the Excel file into a DataFrame
    df = pd.read_excel(fname)

    # Count the occurrences of each value in the specified column
    value_counts = df[column_name].value_counts()

    # Plot a pie chart
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Pie Chart of {column_name} Values')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()'''

def make_pi_chart(fname,column):
    
    #column_name = 'Topic'

    # Read the Excel file into a DataFrame
    df = pd.read_excel(fname)

    # Count the occurrences of each value in the specified column
    value_counts = df[column].value_counts()

    # Plot a pie chart with counts and percentages
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(value_counts, labels=value_counts.index,
                                    autopct=lambda p: f'{int(p*sum(value_counts)/100)}\n({p:.1f}%)',
                                    textprops=dict(color="w"))

    # Add a legend
    ax.legend(wedges, value_counts.index, title=column, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.title(f'Pie Chart of {column} Values')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the pie chart as a PNG file
    plt.savefig(f'{column}_pie_chart.png', bbox_inches='tight')

def sources_bar_plot(fname):
    column_name = 'Source'

    # Read the Excel file into a DataFrame
    '''df = pd.read_excel(fname)

    df['Source'].value_counts().plot(kind='bar')
    plt.title('Bar Chart of Article Sources')
    plt.xlabel('News Sources')
    plt.ylabel('Count')
    #plt.show()

    plt.savefig('sources_bar_chart.png')'''

    df = pd.read_excel(fname)

    # Set the figure size
    plt.figure(figsize=(10, 6))  # Adjust the size as needed

    # Plot the bar chart
    df['Source'].value_counts().plot(kind='bar')
    
    plt.title('Bar Chart of Article Sources')
    plt.xlabel('News Sources')
    plt.ylabel('Count')

    # Save the figure with a higher resolution
    plt.savefig('sources_bar_chart.png', dpi=300, bbox_inches='tight')
'''
def coverage_pi_chart(fname):
    column_name = 'Coverage'

    # Read the Excel file into a DataFrame
    df = pd.read_excel(fname)

    # Count the occurrences of each value in the specified column
    value_counts = df[column_name].value_counts()

    # Plot a pie chart
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Pie Chart of {column_name} Values')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    df = pd.read_excel(fname)

    # Count the occurrences of each value in the specified column
    value_counts = df['Coverage'].value_counts()

    # Plot a pie chart with counts and percentages
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(value_counts, labels=value_counts.index,
                                    autopct=lambda p: f'{int(p*sum(value_counts)/100)}\n({p:.1f}%)',
                                    textprops=dict(color="w"))

    # Add a legend
    ax.legend(wedges, value_counts.index, title='Coverage', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.title(f'Pie Chart of Coverage Values')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the pie chart as a PNG file
    plt.savefig('pie_chart.png', bbox_inches='tight')
'''

def coverage_per_topic_barchart(fname):
    df = pd.read_excel(fname)

    grouped_df = df.groupby('Topic')['Coverage'].value_counts().unstack().fillna(0)

    '''for category in grouped_df.index:
        plt.figure(figsize=(5, 5))  # Adjust figure size as needed
        plt.pie(grouped_df.loc[category], labels=grouped_df.columns, autopct='%1.1f%%', startangle=90)
        plt.title(f'Pie Chart for Category {category}')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.show()'''

    grouped_df = df.groupby(['Topic', 'Coverage']).size().unstack(fill_value=0)

    # Normalize the counts to get proportions
    normalized_df = grouped_df.div(grouped_df.sum(axis=1), axis=0)

    # Plot a grouped bar chart
    normalized_df.plot(kind='bar', stacked=True, colormap='viridis', figsize=(8, 6))
    plt.title('Proportions of Coverage for Each Topic')
    plt.xlabel('Topic')
    plt.ylabel('Proportion')
    plt.legend(title='Coverage')
    plt.savefig('coverage_per_topic_chart.png', bbox_inches='tight')

def data_box(fname):
    df = pd.read_excel(fname)
    cross_tab_counts = pd.crosstab(df['Topic'], df['Coverage'], margins=True, margins_name='Total')

    # Create a cross-tabulation table with percentages
    cross_tab_percentages = pd.crosstab(df['Topic'], df['Coverage'], normalize='index', margins=True, margins_name='Total') * 100
    cross_tab_percentages = cross_tab_percentages.round(2)

    # Display the count table
    print("Counts Table:")
    print(cross_tab_counts)
    print("\n")

    # Display the percentages table
    print("Percentages Table:")
    print(cross_tab_percentages)

    # Create a figure and axis for the counts table
    fig_counts, ax_counts = plt.subplots(figsize=(8, 6))
    ax_counts.axis('off')  # Turn off the axis
    table_counts = table(ax_counts, cross_tab_counts, loc='center', colWidths=[0.2] * len(cross_tab_counts.columns))
    table_counts.auto_set_font_size(False)
    table_counts.set_fontsize(10)
    table_counts.scale(1.5, 1.5)

    # Save the counts table as an image
    fig_counts.savefig('counts_table.png', bbox_inches='tight')

    # Create a figure and axis for the percentages table
    fig_percentages, ax_percentages = plt.subplots(figsize=(8, 6))
    ax_percentages.axis('off')  # Turn off the axis
    table_percentages = table(ax_percentages, cross_tab_percentages, loc='center', colWidths=[0.2] * len(cross_tab_percentages.columns))
    table_percentages.auto_set_font_size(False)
    table_percentages.set_fontsize(10)
    table_percentages.scale(1.5, 1.5)

    # Save the percentages table as an image
    fig_percentages.savefig('percentages_table.png', bbox_inches='tight')

    #plt.show()


if __name__ == "__main__":
    excel_file = "FINAL_DATA.xlsx"

    make_pi_chart(excel_file, 'Topic')
    make_pi_chart(excel_file, 'Coverage')
    
    sources_bar_plot(excel_file)

    coverage_per_topic_barchart(excel_file)
    
    data_box(excel_file)

