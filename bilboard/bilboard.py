import billboard

def get_no_one():
    
    chart = billboard.ChartData('hot-100')
    prev = ""
    current =  chart[0]

    while chart.previousDate:
        
        if current.title == prev.title and prev.title  == current.title:
            prev = current
            chart = billboard.ChartData('hot-100', chart.previousDate)
            current = chart[0] 
            continue
        else:
            print current
            print "number of weeks: ", current.weeks
            print "" 
        prev = current
        chart = billboard.ChartData('hot-100', chart.previousDate)
        current = chart[0] 


def get_longest_no_one():
    
    chart = billboard.ChartData('hot-100')
    prev = ""
    current =  chart[0]
    top = 0
    current_top = ""

    while chart.previousDate:
         
        if current.title == prev.title and prev.title  == current.title:
            prev = current
            chart = billboard.ChartData('hot-100', chart.previousDate)
            current = chart[0] 
            continue

        elif(current.weeks > top):
            top = current.weeks
            current_top = current
            prev = current
            chart = billboard.ChartData('hot-100', chart.previousDate)
            current = chart[0] 
        else:
            prev = current
            chart = billboard.ChartData('hot-100', chart.previousDate)
            current = chart[0] 

    print current_top, "Weeks: ", top

#def test():
#    chart = billboard.ChartData('hot-100', "1994-05-18", fetch=True)
#    print chart

#get_no_one()

def get_all():
    
    all_charts = []    
    year  = 1954
    day   = 01
    month = 01

    while(year < 2018):
        
        while(month <= 12):
            
            while(day <= 28):
                    
                    all_charts.append(billboard.ChartData(hot-100))
        


def test():

    chart = billboard.ChartData('hot-100')
    while chart.previousDate:
        chart = billboard.ChartData('hot-100', chart.previousDate)



test()




