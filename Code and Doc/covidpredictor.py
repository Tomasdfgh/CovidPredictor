#This program is just for fun. passing time i guess. Write a program that
#displays the total covid cases and predict the capacity using
#differential equations.


from urllib.request import Request, urlopen
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def display():
    madeByText.set("Made by Thomas Nguyen")
    print(" ")
    country = search_bar.get()
    country = country.lower()
    if country == "":
        return None
    if country.find(" ") > -1:
        country_2 = country[0].capitalize() + country[1:country.find(" ") + 1] + country[country.find(" ") + 1].capitalize() + country[country.find(" ")+2:]
        country = country.replace(" ", "-")
    else:
        country_2 = country[0].capitalize() + country[1:]
    if country == "usa":
        country = "us"
        country_2 = "USA"
    elif country == "vietnam" or country == "viet nam":
        country = "viet-nam"
        country_2 = "Vietnam"
    elif country == "uk":
        country = "uk"
        country_2 = "UK"
    elif country == "uae" or country == "united arab emirates":
        country = "united-arab-emirates"
        country_2 = "UAE"
    try:

####################################    Fetching Data     ####################################

        finder = '<a class="mt_a" href="country/canada/">Canada</a>'
        finder = finder.replace("canada", str(country))
        finder = finder.replace("Canada", str(country_2))

        from urllib.request import Request, urlopen
        url="https://www.worldometers.info/coronavirus/"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode('utf-8')
        web_byte_str = str(web_byte)



        loc_of_country = web_byte_str.find(finder)
        if loc_of_country == -1:
            unknownLabel.place(x = 350, y = 500, anchor = "center")
            return None
        unknownLabel.pack()
        unknownLabel.pack_forget()

####################################    Data Analysis     ####################################

        total_cases = " "
        new_cases = " "
        total_deaths = " "
        new_deaths = " "
        recovered = " "
        active_cases = " "
        critical_con = " "
        total_test = " "
        population = " "
        temp = " "
        empty = "                           "

                    #=========================Total Cases=========================#

        analysable_data = web_byte_str[loc_of_country:loc_of_country + 2000]
        removable_chunk = str(finder)
        analysable_data = analysable_data.replace(str(removable_chunk), "")
        removable_chunk = '</td>'
        analysable_data = analysable_data.replace(str(removable_chunk), "")
        removable_chunk = '<td style="font-weight: bold; text-align:right">'
        analysable_data = analysable_data.replace(str(removable_chunk), "")
        for i in range(2,len(analysable_data)):
            if analysable_data[i] != "n":
                total_cases += analysable_data[i]
            else:
                break
        total_cases = total_cases[1:len(total_cases)-1]
        total_cases_cover_text = Label(root, text = empty)
        total_cases_text = Label(root, text = total_cases)
        total_cases_cover_text.place(x = 120,y = 150, anchor = "w")
        total_cases_text.place(x = 120, y = 150, anchor = "w")
        print("total cases: " + str(total_cases))
                    #==========================New Cases==========================#
        
        removable_chunk = '<td style="font-weight: bold; text-align:right;background-color:#FFEEAA;">'
        analysable_data = analysable_data.replace(str(removable_chunk), "")
        removable_chunk = '\n' + str(total_cases) + '\n'
        analysable_data = analysable_data.replace(str(removable_chunk), "")
        removable_chunk = '<td style="font-weight: bold; text-align:right;">'
        analysable_data = analysable_data.replace(str(removable_chunk), "")
        analysable_data = analysable_data.replace(str(total_cases), "")
        for i in range(4,len(analysable_data)):
            if analysable_data[i] != "n":
                new_cases += analysable_data[i]
            else:
                break
            
        new_cases = new_cases[1:len(new_cases)-1]
        new_cases_cover_text = Label(root, text = empty)
        new_cases_text = Label(root, text = new_cases)
        new_cases_cover_text.place(x = 120, y = 175, anchor = "w")
        new_cases_text.place(x = 120, y = 175, anchor = "w")
        print("New Cases: " + str(new_cases))
                    #=======================Total Deaths :(========================#
        
        analysable_data = analysable_data.replace(str(new_cases), "")
        for i in range(6,len(analysable_data)):
            if analysable_data[i] != "n":
                total_deaths += analysable_data[i]
            else:
                break
        total_deaths = total_deaths[1:len(total_deaths)-1]
        total_deaths_cover_text = Label(root, text = empty)
        total_deaths_cover_text.place(x = 120, y = 200, anchor = "w")
        total_deaths_text = Label(root, text = total_deaths)
        total_deaths_text.place(x = 120, y = 200, anchor = "w")
        print("Total Deaths: " + str(total_deaths))
                    #========================New Deaths :(==========================#

        analysable_data = analysable_data.replace(str(total_deaths), "")
        removable_chunk = '<td style="font-weight: bold;'
        analysable_data = analysable_data.replace(str(removable_chunk), "")
        removable_chunk = '                                    text-align:right;background-color:red; color:white">'
        analysable_data = analysable_data.replace(str(removable_chunk), "")
        for i in range(11,len(analysable_data)):
            if analysable_data[i] != "n":
                new_deaths += analysable_data[i]
            else:
                break
        new_deaths = new_deaths.replace(" ", "")
        new_deaths = new_deaths.replace("\\", "")
        if new_deaths == "text-alig":
            new_deaths = " "
        new_deaths_text_cover = Label(root, text = empty)
        new_deaths_text_cover.place(x = 120, y = 225, anchor = "w")
        new_deaths_text = Label(root, text = new_deaths)
        new_deaths_text.place(x = 120, y = 225, anchor = "w")
        print("New Deaths: " + str(new_deaths))
                    #===========================Recovered===========================#

        analysable_data = analysable_data.replace(str(new_deaths), "")
        removable_chunk = 'text-align:right;">'
        analysable_data = analysable_data.replace(str(removable_chunk), "")
        for i in range(12,len(analysable_data)):
            if analysable_data[i] != "t":
                recovered += analysable_data[i]
            else:
                break
        recovered = recovered.replace(" ", "")
        recovered = recovered.replace('\\', "")
        recovered = recovered.replace("n", "")
        recovered = recovered.replace("<", "")
        analysable_data = analysable_data.replace(str(recovered), "")
        if recovered == "N/AN/A":
            recovered = "N/A"
        recovered_text_cover = Label(root, text = empty)
        recovered_text_cover.place(x = 120, y = 250, anchor = "w")
        recovered_text = Label(root,text = recovered)
        recovered_text.place(x = 120, y = 250, anchor = "w")
        print("Recovered: " + str(recovered))
                    #==========================Active Cases==========================#

        analysable_data = analysable_data.replace(" ", "")
        analysable_data = analysable_data.replace("+", "")
        if analysable_data.find('text-align:right;background-color:#c8e6c9;color:#000">') > -1:
            removable_chunk = 'text-align:right;background-color:#c8e6c9;color:#000">'
            for i in range(analysable_data.find(removable_chunk) + len(removable_chunk),len(analysable_data)):
                if analysable_data[i] != "n":
                    temp += analysable_data[i]
                else:
                    break
            analysable_data = analysable_data.replace(str(removable_chunk), "")
            temp = temp.replace(" ", "")
            temp = temp.replace("\\", "")
            analysable_data = analysable_data.replace(str(temp), "")

            analysable_data = analysable_data.replace(str(temp), "")
            temp = " "
        if analysable_data.find('</td>\n<td style="font-weight: bold; text-align:right;background-color:#c8e6c9; color:#000">') > -1:
            removable_chunk = 'text-align:right;background-color:#c8e6c9;color:#000">'
            for i in range(analysable_data.find(removable_chunk) + len(removable_chunk),len(analysable_data)):
                if analysable_data[i] != "n":
                    temp += analysable_data[i]
                else:
                    break
            analysable_data = analysable_data.replace(str(removable_chunk), "")
            temp = temp.replace(" ", "")
            temp = temp.replace("\\", "")
            analysable_data = analysable_data.replace(str(temp), "")

            analysable_data = analysable_data.replace(str(temp), "")
            temp = " "
        analysable_data = analysable_data.replace('bold;">', "")
        removable_chunk = '<tdstyle="text-align:right;font-weight:'
        for i in range(analysable_data.find(removable_chunk) + len(removable_chunk),len(analysable_data)):
            if analysable_data[i] != "n":
                active_cases += analysable_data[i]
            else:
                break  
        active_cases = active_cases.replace(" ", "")
        active_cases = active_cases.replace("\\", "")
        active_cases = active_cases.replace("n", "")
        active_cases_text_cover = Label(root, text = empty)
        active_cases_text_cover.place(x = 120, y = 275, anchor = "w")
        active_cases_text = Label(root, text = active_cases)
        active_cases_text.place(x =120, y = 275, anchor = "w")
        print("Active Cases: " + str(active_cases))
        analysable_data = analysable_data.replace(str(active_cases), "")
                    #=======================Critical Condition=======================#

        analysable_data = analysable_data.replace(str(removable_chunk), "")
        for i in range(18,len(analysable_data)):
            if analysable_data[i] != "n":
                critical_con += analysable_data[i]
            else:
                break
        critical_con = critical_con[1:len(critical_con)-1]
        critical_con_text_cover = Label(root, text =empty)
        critical_con_text_cover.place(x = 120, y = 300, anchor = "w")
        critical_con_text = Label(root, text = critical_con)
        critical_con_text.place(x =120, y = 300, anchor = "w")
        print("Critical Conditions: " + str(critical_con))
                    #===========================Total Test===========================#

        analysable_data = analysable_data.replace(str(critical_con), "")
        
        for i in range(22,len(analysable_data)):
            if analysable_data[i] != "n":
                temp += analysable_data[i]
            else:
                break
        temp = temp[1:len(temp)-1]
        analysable_data = analysable_data.replace(str(temp), "")
        temp = " "
        for i in range(24,len(analysable_data)):
            if analysable_data[i] != "n":
                temp += analysable_data[i]
            else:
                break
        temp = temp[1:len(temp)-1]
        analysable_data = analysable_data.replace(str(temp), "")
        for i in range(26,len(analysable_data)):
            if analysable_data[i] != "n":
                total_test += analysable_data[i]
            else:
                break
        total_test = total_test[1:len(total_test)-1]
        total_test_cover_text = Label(root, text = empty)
        total_test_cover_text.place(x = 120, y = 325, anchor = "w")
        total_test_text = Label(root, text = total_test)
        total_test_text.place(x = 120, y = 325, anchor = "w")
        print("Total conducted Tests: " + str(total_test))
        analysable_data = analysable_data.replace(str(total_test), "")
                    #===========================Population===========================#
        
        removable_chunk = '<ahref="/world-population/canada-population/">'
        removable_chunk = removable_chunk.replace("canada", str(country))
        for i in range(analysable_data.find(removable_chunk) + len(removable_chunk),len(analysable_data)):
            if analysable_data[i] != "n":
                population += analysable_data[i]
            else:
                break
        population = population.replace(" ", "")
        population = population.replace("<", "")
        population = population.replace("a", "")
        population = population.replace(">", "")
        population = population.replace("/", "")
        population = population.replace("\\", "")
        population_cover_text = Label(root, text = empty)
        population_cover_text.place(x = 120, y = 350, anchor = "w")
        population_text = Label(root, text = population)
        population_text.place(x = 120, y = 350, anchor = "w")
        print("Population: " + str(population))

        
                    #===========================Prediction===========================#
        # here is the formula I am going to use to predict:
        # total_cases = population + (active_cases - population )*2.71 ** (-bt)
        # solve for b, then plug it back in to find total_cases at each t alright game on
        try:
            total_cases = int(total_cases.replace(",",""))
            population = int(population.replace(",",""))
            active_cases = int(active_cases.replace(",",""))
        except:
            madeByText.set("Data is Missing, not enought to predict a model")

        b = - np.log((total_cases - population)/(active_cases - population))
        

        x = 100*[0]
        y = 100*[0]
        t = 0

        for i in range(len(y)):
            x[i] = t
            y[i] = population + (active_cases - population )* (2.71 ** (-b * t))
            t += 1

        fig = plt.Figure(figsize = (4,3), dpi = 100)
        fig.suptitle('New cases vs. Days in the Future',fontsize = 10)
        
        plt.xlabel('Cases')
        plt.ylabel('Days')
        fig.add_subplot(111).plot(x,y)

        chart = FigureCanvasTkAgg(fig, master = root)
        chart.get_tk_widget().place(x = 450, y = 300, anchor = "center")
        
    except:
        unknownLabel.place(x = 350, y = 500, anchor = "center")
        return None

####################################    GUI Builder     ######################################

root = Tk()
root.geometry("700x550")
root.title("Covid-19 Watch and Predictor")

unknownText = StringVar()
unknownText.set('''
You have either entered this country incorrectly,
or this country is not in the record. Try again!
''')
unknownLabel = Label(root, textvariable = unknownText)

titleText = StringVar()
titleText.set("Covid-19 Watch and Predictor")

welcomeLabel = Label(root, textvariable = titleText)
welcomeLabel.place (x = 350, y = 10, anchor = "center")

madeByText = StringVar()
madeByText.set("Made by Thomas Nguyen")

madeByLabel = Label(root, textvariable = madeByText)
madeByLabel.place (x = 350, y = 540, anchor = "center")

search_up_label = Label(root, text = "Search up a country: ")
search_up_label.place(x = 0, y = 40, anchor = "w")

search_bar = Entry(root, width = 30)
search_bar.place(x = 100, y = 70, anchor = "center")

search_button = Button(root, text = "Search",command = display)
search_button.place(x = 30, y = 110, anchor = "center")

total_cases_label = Label(root, text = "Total Cases: ")
total_cases_label.place(x = 35, y = 150, anchor = "center")

new_cases_label = Label(root, text = "New Cases: " )
new_cases_label.place(x = 35, y = 175, anchor = "center")

total_deaths_label = Label(root, text = "Total Deaths: ")
total_deaths_label.place(x = 38, y = 200, anchor = "center")

new_deaths_label = Label(root, text = "New Deaths: ")
new_deaths_label.place(x = 37, y = 225, anchor = "center")

recovered_label = Label(root, text = "Recovered: ")
recovered_label.place(x = 35, y = 250, anchor = "center")

active_cases_label = Label(root, text = "Active Cases: ")
active_cases_label.place(x = 40, y = 275, anchor = "center")

crit_con_label = Label(root, text = "Critical Condition: ")
crit_con_label.place(x = 53, y = 300, anchor = "center")

total_test_label = Label(root, text = "Total Test: ")
total_test_label.place(x = 33, y = 325, anchor = "center")

population_label = Label(root, text = "Population: ")
population_label.place(x = 37, y = 350, anchor = "center")

predicted_model_label = Label(root, text = "Predicted Model of Active Cases: ")
predicted_model_label.place(x = 345, y = 120, anchor = "center")

root.mainloop()
