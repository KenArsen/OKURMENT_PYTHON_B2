city_1 = "Astana"
city_2 = "Almaty"

result = (
    (city_1 < city_2 or city_2 == "almaty") 
    and (city_1 != city_2)
)
print(result)

city_1 = "Astana"
city_2 = "Almaty"
result_2 = (
    (
        city_1 + city_2 == "AlmatyAstana" 
        and len(city_2 + "123") == 9
    )
    or (
        city_1 in city_2
    )
)
