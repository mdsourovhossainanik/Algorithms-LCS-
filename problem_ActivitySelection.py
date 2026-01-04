def Activities_selection(Event_name,start_time, finish_time,bujet,maximum_bujet,Profit):
    n=len(start_time)
    items=[(Event_name[i] ,start_time[i], finish_time[i],bujet[i],Profit[i]) for i in range(n)]
    print(items)
    sort_item =sorted(items,key=lambda item:item[4],reverse=True)
    print(sort_item)
   
    selcected_Event=[]
    
    Last_finished_time=0
    Total_profit=0
    for activitis_name,start_time,finish_time,bujet,Profit in  sort_item:
        if start_time>=Last_finished_time :
            if maximum_bujet>=bujet:
                maximum_bujet-=bujet
                Total_profit+=Profit
                selcected_Event.append((Event_name,start_time,finish_time,bujet,Profit))
                Last_finished_time=finish_time
            
        
    return selcected_Event,len(selcected_Event),Total_profit
 


maximum_bujet=int(input("Total_bujet of Project:"))
Event_no=int(input("Number of event:"))
Event_name=[]
start_time=[]
finish_time=[]
bujet=[]
Profit=[]
for i in range(Event_no):
    print(f"\n{i+1} Event->")
    Event_name.append(input("Enter Event name ( A/B/C): "))
    s,f,b,p=map(float,input("Enter Starting_and_Finishing time_Bujet_profit=").split())
    start_time.append(s)
    finish_time.append(f)
    bujet.append(b)
    Profit.append(p)
    
    
 
selcected_Event,total_selected,Total_profit= Activities_selection(Event_name,start_time,finish_time,bujet,maximum_bujet,Profit)  
print("selected Event=")    
for name, start, finish,bujet,Profit in selcected_Event:
    print(f"{name}:({start},{finish},{bujet},{Profit})")
print("Total selected Event=", total_selected) 
print("Total profit=", Total_profit) 
 


 