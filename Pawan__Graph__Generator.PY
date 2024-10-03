import pandas as Pandas__Data__Frame
import seaborn as Sagar__Nivasam
import matplotlib.pyplot as Maths__Plotting__Graph
import os as Prachalan__Pranali


def Pawan__Generate__Dataframe():
	Pawan__Excel__File__Name = "Pawan__Portfolio__Wizard.xlsx"
	Pawan__Maha__Dataframe = Pandas__Data__Frame.read_excel(Pawan__Excel__File__Name)
	Pawan__Company__Name__List = Pawan__Maha__Dataframe['Company__Name'].tolist()
	Pawan__Create__Graphs(Pawan__Maha__Dataframe)


def Pawan__Create__Graphs(Pawan__Maha__Dataframe):
	Pawan__Company__Name__List = Pawan__Maha__Dataframe['Company__Name'].tolist()
	Pawan__Folder__Path = Prachalan__Pranali.getcwd()
	Pawan__Folder__Path = Pawan__Folder__Path  + "\\Images\\"
	Graph1 = Pawan__Maha__Dataframe[['Company__Name', 'Total Current Amount']]
	Graph1 = Graph1.sort_values(by='Total Current Amount', ascending=False).reset_index(drop=True)  # Sort and reset the index
	# Set the style of seaborn
	Sagar__Nivasam.set(style="whitegrid")
	# Choose a color palette that can accommodate 10-20 colors
	color_palette = Sagar__Nivasam.color_palette("husl", len(Graph1))
	# Create a bar plot
	Maths__Plotting__Graph.figure(figsize=(16, 9))  # Set the figure size
	Maths__Plotting__Graph.subplots_adjust(left=0.2)
	bar_plot = Sagar__Nivasam.barplot(x='Total Current Amount', y='Company__Name', data=Graph1, hue='Company__Name', dodge=False, palette=color_palette, legend=False)
	# Assign 'Company__Name' to hue to apply the color palette
    # Ensures bars are not dodged (overlapping)
    # Suppress the legend that is unnecessary in this context

	for index, row in Graph1.iterrows(): 
		bar_width = row['Total Current Amount']
		bar_plot.text(
		bar_width + 10000,  # x-coordinate (right of the bar end), adjust padding here
        index,              # y-coordinate
        f'{row["Total Current Amount"]:.2f}',  # text with 2 decimal places
        color='black',
        ha='left',         # Horizontal alignment
        va='center',
        weight='bold')        # Vertical alignment
	# Set the title and labels
	Maths__Plotting__Graph.title('Total Amount by Company')
	Maths__Plotting__Graph.xlabel('Total Current Amount')
	Maths__Plotting__Graph.ylabel('Company Name')
	# Save the figure as PDF
	Maths__Plotting__Graph.savefig(Pawan__Folder__Path + '01__Total__Asset__Value.png')	
	# Show the plot
	#Maths__Plotting__Graph.show()
	del Graph1
#======================================================================================================================================================================================================
#======================================================================================================================================================================================================
	Graph2 = Pawan__Maha__Dataframe[['Company__Name', 'Total Current Amount', 'Share Group Category']]
	List__Group__Type = Pawan__Maha__Dataframe['Share Group Category'].tolist()
	List__Total__Amount = Pawan__Maha__Dataframe['Total Current Amount'].tolist()
	Total__A = 0.00
	Total__B = 0.00
	Total__T = 0.00
	Total__S = 0.00
	Total__Z = 0.00
	Total__Others = 0.00
	Total__Total = 0.00
	for index, item in enumerate(List__Group__Type):
		if item[0] == "A": 
			List__Group__Type[index] = "A"
			Total__A =  Total__A + List__Total__Amount[index]
			Total__Total = Total__Total + List__Total__Amount[index]
		elif item[0] == "B": 
			List__Group__Type[index] = "B"
			Total__B =  Total__B + List__Total__Amount[index]
			Total__Total = Total__Total + List__Total__Amount[index]
		elif item[0] == "T": 
			List__Group__Type[index] = "T"
			Total__T =  Total__T + List__Total__Amount[index]
			Total__Total = Total__Total + List__Total__Amount[index]
		elif item[0] == "S": 
			List__Group__Type[index] = "S"
			Total__S =  Total__S + List__Total__Amount[index]
			Total__Total = Total__Total + List__Total__Amount[index]
		elif item[0] == "Z": 
			List__Group__Type[index] = "Z"
			Total__Z =  Total__Z + List__Total__Amount[index]
			Total__Total = Total__Total + List__Total__Amount[index]
		else: 
			List__Group__Type[index] = "Others"
			Total__Others =  Total__Others + List__Total__Amount[index]
			Total__Total = Total__Total + List__Total__Amount[index]
	Total__A = ((Total__A/Total__Total) * 100)
	Total__B = ((Total__B/Total__Total) * 100)
	Total__T = ((Total__T/Total__Total) * 100)
	Total__S = ((Total__S/Total__Total) * 100)
	Total__Z = ((Total__Z/Total__Total) * 100)
	Total__Others = ((Total__Others/Total__Total) * 100)
	del List__Total__Amount
	del Graph2
	List__Group__Type = ["Type A", "Type B", "Type T", "Type S","Type Z", "Others"]
	List__Percentage = [Total__A, Total__B, Total__T, Total__S, Total__Z, Total__Others]
	filtered_percentages = [percentage for percentage in List__Percentage if percentage > 0]
	filtered_labels = [label for percentage, label in zip(List__Percentage, List__Group__Type) if percentage > 0]
	Sagar__Nivasam.set(style="whitegrid")
	Maths__Plotting__Graph.figure(figsize=(16, 9))
	palette_color = Sagar__Nivasam.color_palette('bright')
	Maths__Plotting__Graph.pie(filtered_percentages, labels = filtered_labels, colors=palette_color, autopct='%.0f%%', textprops={'weight': 'bold'})
	Maths__Plotting__Graph.title('Percentage (%) of Each Group Type In portfolio')
	# Save the figure as PDF
	Maths__Plotting__Graph.savefig(Pawan__Folder__Path + '02__Percentage__Of__Investment__Per__Share__Category.png')	
	#Maths__Plotting__Graph.show()
#======================================================================================================================================================================================================
#======================================================================================================================================================================================================
	Temp__Dataframe = Pawan__Maha__Dataframe[['Company__Name', 'Profit & Loss Statement']]
	Temp__Dataframe = Temp__Dataframe.sort_values(by='Profit & Loss Statement', ascending=False)
	Temp__Pawan__Company__Name__List = Temp__Dataframe['Company__Name'].tolist()
	Temp__Pawan__Profit__Loss__List = Temp__Dataframe['Profit & Loss Statement'].tolist()
	color_palette = ['green' if v >= 0 else 'red' for v in Temp__Pawan__Profit__Loss__List ]
	Sagar__Nivasam.set(style="whitegrid")
	Maths__Plotting__Graph.figure(figsize=(16, 9))
	Maths__Plotting__Graph.subplots_adjust(left=0.2)
	bars = Maths__Plotting__Graph.barh(Temp__Pawan__Company__Name__List, Temp__Pawan__Profit__Loss__List, color=color_palette)
	Maths__Plotting__Graph.title('Profit and Loss making Shares')
	Maths__Plotting__Graph.xlabel('Profit & Loss')
	Maths__Plotting__Graph.ylabel('Company Name')
	for index, item in enumerate(Temp__Pawan__Profit__Loss__List ):
		if item > 0:  
			Text__Position = item + 1000
			Text__Color = 'darkgreen'
		else: 
			Text__Position = 1000
			Text__Color = 'red'
		Maths__Plotting__Graph.text(Text__Position, index, f'{item:.2f}', color= Text__Color, ha='left', va='center', weight='bold')
	# Save the figure as PDF
	Maths__Plotting__Graph.savefig(Pawan__Folder__Path + '03__Profit__&__Loss__Per__Stock.png')
	#Maths__Plotting__Graph.show()
#======================================================================================================================================================================================================
#======================================================================================================================================================================================================
	Temp__Dataframe = Pawan__Maha__Dataframe[['Company__Name', 'Profit & Loss Percentage']]
	Temp__Dataframe = Temp__Dataframe.sort_values(by='Profit & Loss Percentage', ascending=False)
	Temp__Pawan__Company__Name__List = Temp__Dataframe['Company__Name'].tolist()
	Temp__Percentage__Profit__Loss = Temp__Dataframe['Profit & Loss Percentage'].tolist()
	color_palette = ['green' if v >= 0 else 'red' for v in Temp__Percentage__Profit__Loss]
	Sagar__Nivasam.set(style="whitegrid")
	Maths__Plotting__Graph.figure(figsize=(16, 9))
	Maths__Plotting__Graph.subplots_adjust(left=0.2)
	bars = Maths__Plotting__Graph.barh(Temp__Pawan__Company__Name__List, Temp__Percentage__Profit__Loss, color=color_palette)
	Maths__Plotting__Graph.title('Profit and Loss Percentages')
	Maths__Plotting__Graph.xlabel('Profit & Loss Percentage')
	Maths__Plotting__Graph.ylabel('Company Name')
	for index, item in enumerate(Temp__Percentage__Profit__Loss):
		if item > 0:  
			Text__Position = item + 0.3
			Text__Color = 'darkgreen'
		else: 
			Text__Position = 0.3
			Text__Color = 'red'		
		Maths__Plotting__Graph.text(Text__Position, index, f'{item:.2f}', color= Text__Color, ha='left', va='center', weight='bold')
	# Save the figure as PDF
	Maths__Plotting__Graph.savefig(Pawan__Folder__Path + '04__Profit_Loss_Percentage.png')	
	#Maths__Plotting__Graph.show()
#======================================================================================================================================================================================================
#======================================================================================================================================================================================================
	Pawan__ROE__List = Pawan__Maha__Dataframe['ROE Value'].tolist()
	Tupple__List = list(zip(Pawan__Company__Name__List, Pawan__ROE__List))
	Tupple__List.sort(key=lambda x: x[1], reverse = True)
	T_Pawan__Company__Name__List, T_Pawan__ROE__List = zip(*Tupple__List)
	color_palette = ['green' if v >= 0 else 'red' for v in T_Pawan__ROE__List]
	Sagar__Nivasam.set(style="whitegrid")
	Maths__Plotting__Graph.figure(figsize=(16, 9))
	Maths__Plotting__Graph.subplots_adjust(left=0.2)
	bars = Maths__Plotting__Graph.barh(T_Pawan__Company__Name__List, T_Pawan__ROE__List, color=color_palette)
	Maths__Plotting__Graph.title('ROE Information for All Shares')
	Maths__Plotting__Graph.xlabel('ROE information')
	Maths__Plotting__Graph.ylabel('Company Name')
	for index, item in enumerate(T_Pawan__ROE__List):
		if item >1:  
			Text__Position = item + 1
			Text__Color = 'darkgreen'
		else: 
			Text__Position = 0
			Text__Color = 'red'
		Maths__Plotting__Graph.text(Text__Position, index, f'{item:.2f}', color= Text__Color, ha='left', va='center', weight='bold')
	Maths__Plotting__Graph.savefig(Pawan__Folder__Path + '05__ROE__Information.png')
	#Maths__Plotting__Graph.show()			
#======================================================================================================================================================================================================
#======================================================================================================================================================================================================
	Pawan__EPS__List = Pawan__Maha__Dataframe['EPS Info'].tolist()
	Tupple__List = list(zip(Pawan__Company__Name__List, Pawan__EPS__List))
	Tupple__List.sort(key=lambda x: x[1], reverse = True)
	T_Pawan__Company__Name__List, T_Pawan__EPS__List = zip(*Tupple__List)
	color_palette = ['green' if v >= 50 else 'darkorange' if 20 <= v < 50 else 'red' for v in T_Pawan__EPS__List]
	Sagar__Nivasam.set(style="whitegrid")
	Maths__Plotting__Graph.figure(figsize=(16, 9))
	Maths__Plotting__Graph.subplots_adjust(left=0.2)
	bars = Maths__Plotting__Graph.barh(T_Pawan__Company__Name__List, T_Pawan__EPS__List, color=color_palette)
	Maths__Plotting__Graph.title('EPS Information for All Shares')
	Maths__Plotting__Graph.xlabel('EPS Information: less than 20 (Red), 20 to 50 (Orange) and above 50 (Green)')
	Maths__Plotting__Graph.ylabel('Company Name')
	for index, item in enumerate(T_Pawan__EPS__List):
		if item >50:  
			Text__Position = item + 1
			Text__Color = 'darkgreen'
		elif item > 20 and item < 50:
			Text__Position = item + 1
			Text__Color = 'darkorange'
		else: 
			Text__Position = item + 1
			Text__Color = 'red'
		Maths__Plotting__Graph.text(Text__Position, index, f'{item:.2f}', color= Text__Color, ha='left', va='center', weight='bold')
	Maths__Plotting__Graph.savefig(Pawan__Folder__Path + '06__EPS__Information.png')
	#Maths__Plotting__Graph.show()			
#======================================================================================================================================================================================================
#======================================================================================================================================================================================================
	Pawan__PB__Ratio__List = Pawan__Maha__Dataframe['P/B Ratio'].tolist()
	Tupple__List = list(zip(Pawan__Company__Name__List, Pawan__PB__Ratio__List))
	Tupple__List.sort(key=lambda x: x[1])
	T_Pawan__Company__Name__List, T_Pawan__PB__Ratio__List = zip(*Tupple__List)
	color_palette = ['red' if v >= 100 else 'darkorange' if 30 <= v < 1000 else 'darkgreen' for v in T_Pawan__PB__Ratio__List]
	Sagar__Nivasam.set(style="whitegrid")
	Maths__Plotting__Graph.figure(figsize=(16, 9))
	Maths__Plotting__Graph.subplots_adjust(left=0.2)
	bars = Maths__Plotting__Graph.barh(T_Pawan__Company__Name__List, T_Pawan__PB__Ratio__List, color=color_palette)
	Maths__Plotting__Graph.title('Price to Book Ratio for All Shares')
	Maths__Plotting__Graph.xlabel('P/B Ratio: less than 30 (Green), 30 to 100 (Orange) and above 100 (Red)')
	Maths__Plotting__Graph.ylabel('Company Name')
	for index, item in enumerate(T_Pawan__PB__Ratio__List):
		if item >100:  
			Text__Position = item + 1
			Text__Color = 'red'
		elif item > 30 and item < 100:
			Text__Position = item + 1
			Text__Color = 'darkorange'
		else: 
			Text__Position = item + 1
			Text__Color = 'darkgreen'
		Maths__Plotting__Graph.text(Text__Position, index, f'{item:.2f}', color= Text__Color, ha='left', va='center', weight='bold')
	Maths__Plotting__Graph.savefig(Pawan__Folder__Path + '07__PB__Ratio__Information.png')
	#Maths__Plotting__Graph.show()			
#======================================================================================================================================================================================================
#======================================================================================================================================================================================================
	Pawan__PE__Ratio__List = Pawan__Maha__Dataframe['PE Ratio'].tolist()
	Tupple__List = list(zip(Pawan__Company__Name__List, Pawan__PE__Ratio__List))
	Tupple__List.sort(key=lambda x: x[1])
	T_Pawan__Company__Name__List, T_Pawan__PE__Ratio__List = zip(*Tupple__List)
	color_palette = ['red' if v >= 30 else 'darkorange' if 20 <= v < 30 else 'darkgreen' for v in T_Pawan__PE__Ratio__List]
	Sagar__Nivasam.set(style="whitegrid")
	Maths__Plotting__Graph.figure(figsize=(16, 9))
	Maths__Plotting__Graph.subplots_adjust(left=0.2)
	bars = Maths__Plotting__Graph.barh(T_Pawan__Company__Name__List, T_Pawan__PE__Ratio__List, color=color_palette)
	Maths__Plotting__Graph.title('Price per Equity Ratio for All Shares')
	Maths__Plotting__Graph.xlabel('PE Ratio: less than 20 (Green: Excellent), 20 to 30 (Orange: Average) and above 30 (Red: Caution)')
	Maths__Plotting__Graph.ylabel('Company Name')
	for index, item in enumerate(T_Pawan__PE__Ratio__List):
		if item >100:  
			Text__Position = item + 1
			Text__Color = 'red'
		elif item > 30 and item < 100:
			Text__Position = item + 1
			Text__Color = 'darkorange'
		else: 
			Text__Position = item + 1
			Text__Color = 'darkgreen'
		Maths__Plotting__Graph.text(Text__Position, index, f'{item:.2f}', color= Text__Color, ha='left', va='center', weight='bold')
	Maths__Plotting__Graph.savefig(Pawan__Folder__Path + '08__PE__Ratio__Information.png')
	#Maths__Plotting__Graph.show()			
#======================================================================================================================================================================================================
#======================================================================================================================================================================================================

if __name__ == "__main__":
	Pawan__Generate__Dataframe()



	
