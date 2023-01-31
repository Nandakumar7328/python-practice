def main(startCity,tickets) :
    len_tickets = len(tickets)
    print(len_tickets)
    temp_city = startCity
    visit_city = [startCity]
    for i in range(len_tickets):
        for j,k in tickets.items():
            temp = temp_city == j
            if temp and k not in visit_city:
                visit_city.append(k)
                temp_city = k 
    return visit_city
tickets = {
    "Paris":"Skopje",
    "Zurich":"Amsterdam",
    "Prague":"Zurich",
    "Barcelona":"Berlin",
    "Kiev":"Prague",
    "Skopje":"Paris",
    "Amsterdam":"Barcelona",
    "Berlin":"Kiev",
    "Berlin":"Amsterdam" 
}

city = ["Amsterdam", "Kiev", "Zurich", "Prague", "Berlin", "Barcelona"]
startCity = "Kiev"

result = main(startCity,tickets)
print(" => ".join(result))

