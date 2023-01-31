def intro():
    name=input("Enter name: ")
    people=int(input("Enter no of people: "))
    foodtype=input("Veg or non-veg: ")
    budget=int(input("Enter budget: "))
    dessert=input("Do u want dessert or not? ")

intro()


menu = [
{"name":"Plain Sandwich","price":	175, "category": "snacks"},
{"name":"Grilled Sandwich","price":	175, "category": "snacks"},
{"name":"Club Sandwich","price":	175, "category": "snacks"},

{"name":"Russian Salad / Maccroni","price":	119},

{"name":"Veg. Burger","price":	72},

{"name":"Pasta Spicy Tomato / Classical Cheese","price":	190},
{"name":"Pasta in Twin Sauce	","price":190},

{"name":"Plain Cheese Pizza	","price":190},
{"name":"Capsicum, Onion Pizza","price":	210},
{"name":"Tomato, Onion Pizza","price":	210},
{"name":"Capsicum, Onion, Mashroom Pizza	","price":250},
{"name":"Jain Spl. Pizza	","price":250},
{"name":"Tandoori Pizza","price":	250},
{"name":"Super Veggie Pizza(Double Cheese)	","price":265},

{"name":"Hot & Sour 	","price":109},
{"name":"Lemon & Coriander","price":	109},
{"name":"Veg. Noodle Soup","price":	109},
{"name":"Sweet Corn","price":	109},
{"name":"Veg. Munchow","price":	109},
{"name":"Veg. Clear Soup	","price":109},

{"name":"Spring Roll","price":	145},
{"name":"Chilly Paneer Dry ","price":	195},
{"name":"Veg. Manchurian Dry","price": 	153},
{"name":"Potatoes in Honey & Chilly","price": 	175},
{"name":"Fried Vegetables in Salt & Papper","price": 	190},
{"name":"Crispy Spinach & Baby - Corn","price":	198},
{"name":"Chilly Mushroom Dry ","price":	193},

{"name":"Veg Chopsouey","price":	195},
{"name":"Chilly Paneer Gravy ","price":	205},
{"name":"Manchurian Gravy","price":	175},
{"name":"Sweet & Sour Veg","price":	175},
{"name":"Mix. Veg. in Hot Garlic Sauce","price":	185},
{"name":"Shreded Potatoes in Hot Garlic Sauce","price": 195},


{"name":"Veg Hakka Noodles","price":	145},
{"name":"Chilli Garlic Noodles ","price":	145},
{"name":"Pan Fried Noodles	","price":225},
{"name":"Gravy Noodles","price":	225},

{"name":"Veg. Fried Rice","price":	165},
{"name":"Chilly Garlic Rice","price":	165},

{"name":"Pav Bhaji","price":	140},
{"name":"Jain Pav Bhaji","price":	155},
{"name":"Bombay Vada Pav","price":	102},
{"name":"Extra Pav","price":	35},

{"name":"Dahi Bhalla / Dahi Papri","price":	90},
{"name":"Dahi Bhalla Papri","price":	90},
{"name":" Gappa (6 pcs.)","price":	68},
{"name":"Gol Gappa Water Extra For Packing","price":	25},

{"name":"Tandoori Paneer Tikka","price":	220},
{"name":"Malai Paneer Tikka","price":	220},
{"name":"Soya Tandoori Tikka","price": 	175},
{"name":"Tandoori Aloo","price":	179},
{"name":"Punjabi Soya Chap","price":	179},
{"name":"Hare-Bhare Kabab","price":	162},
{"name":"Dahi ke Kabab","price":	179},
{"name":"Platter","price":	325},

{"name":"Shahi Paneer","price":	210},
{"name":"Kadhai Paneer","price": 	210},
{"name":"Paneer Butter Masala","price": 	210},
{"name":"Mushroom Masala","price": 	215},
{"name":"Malai Kofta","price":	210},

{"name":"Dal Makhani","price":	192},
{"name":"Yellow Dal","price":	141},
{"name":"Rajma ","price":	141},
{"name":"Chole ","price":	141},

{"name":"Tandoori Roti","price":	30},
{"name":"Roomali Roti","price":	17},
{"name":"Butter Roti","price":	36},
{"name":"Plain Naan","price":	43},
{"name":"Butter Naan","price":	58},
{"name":"Garlic Naan Butter","price":	60},
{"name":"Tawa Parantha","price":	53},
{"name":"Laccha Parantha","price":	53},
{"name":"Pudina Parantha","price":	53},
{"name":"Stuffed Kulcha (Aloo)","price":	65},
{"name":"Stuffed Kulcha (Paneer)","price":	65},
{"name":"Stuffed Kulcha (Onion)","price":	65},
{"name":"Papad","price":	15},

{"name":"Steam Rice","price":	161},
{"name":"Soya Dum Biryani","price": 	220},
{"name":"Veg. Pulao","price":	161},
{"name":"Mix Veg. Pulao","price":	161},
{"name":"Jeera Pulao	","price":161},
{"name":"Matka Biryani With Raita","price": 	220},
{"name":"Hyderabadi Biryani","price": 	220},
{"name":"Plain Raita	","price":102},
{"name":"Boondi Raita","price":	102},
{"name":"Mix. Veg. Raita","price":	102},
{"name":"Jeera Raita","price":	102},
{"name":"Pineapple Raita","price":	102},

{"name":"Gulab Jamun","price":	60},
{"name":"Halwa (Seasonal)","price":	60},

{"name":"Thali Special	(Dal Makhani, Seasonal Veg., Shahi Paneer, Bread, Rice, Raita, Papad & One Dessert.)","price":   280},

{"name":"Roomali Roti with Paneer Tikka Masala","price":	250},
{"name":"Rogan Soya Chap with Roomali Roti","price":	250},

{"name":"Rice Idli","price":	81},
{"name":"Sambhar Vada","price":	85},
{"name":"Dahi Vada","price":	81},

{"name":"Dosa (Butter)","price":	125},
{"name":"Onion Dosa (Butter)","price":	136},
{"name":"Paper Dosa","price":	130},
{"name":"Mysore Dosa","price":	123},
{"name":"Rawa Dosa","price":	119},
{"name":"Onion Rawa Dosa","price":	136},

{"name":"Dosa (Butter)","price":	145},
{"name":"Onion Dosa (Butter)","price":	156},
{"name":"Paper Dosa","price":	150},
{"name":"Myscore Dosa","price":	143},
{"name":"Rawa Dosa","price":	156},
{"name":"Onion Rawa Dosa","price":	171},

{"name":"Onion Uttapam","price":	155},
{"name":"Tomato Uttapam","price":	155},
{"name":"Mix Veg Uttapam","price":	155},


{"name":"Sambhar Rice","price":	132},
{"name":"Curd Rice","price":	132},

{"name":"Fruit Punch","price":	150},
{"name":"Red Sea","price":	150},
{"name":"Virgin Colada","price":	150},
{"name":"Love Valley","price":	150},
{"name":"Pomi Twist","price":	150},
{"name":"Ginger Fizz","price":	150},
{"name":"Italian Smooch","price":	150},
{"name":"Devils Kiss","price":	150},
{"name":"Blue Lagoon","price":	150},
{"name":"Fresh Mint Mojito","price":	150},
{"name":"Kiwi Smoothie","price":	150},
{"name":"Virgin Guava","price":	150},
{"name":"Litchi Smoothie","price":	150},
{"name":"Peach Apricot","price":	150},
{"name":"Blue Berry Smoothie","price":	150},
{"name":"Green Hayland","price":	150},
{"name":"White Rosy","price":	150},
{"name":"Watermelon Mojito","price":	150},

{"name":"Vanilla/Strawberry","price":	51},
{"name":"Tutti Fruti	","price":60},
{"name":"Pineapple","price":	60},
{"name":"Chocolate","price":	60},
{"name":"Butter Scotch","price":	60},
{"name":"Kaju Kishmish","price":	60},
{"name":"Vanilla Chocochips","price":	60},
{"name":"Mango","price":	60},
{"name":"Anjeer Honey","price":	60},
{"name":"Chocolate Almond Fudge","price":	60},
{"name":"Kesar Pista","price":	60},
{"name":"Black Currant","price":	60},

{"name":"Hot Choclate Fudge","price":	165},
{"name":"Fruit Salad Sundae","price":	165},

{"name":"Lime Ice / Orange","price":	119},
{"name":"Golden Glow / Strawberry","price":	119},

{"name":"Vanilla","price":	128},
{"name":"Mango","price":	128},
{"name":"Pineapple","price":	128},
{"name":"Chocolate / Coffee","price":	128},
{"name":"Kesar Pista","price":	128},
{"name":"Butter Scotch","price":	128},

{"name":"Tea","price":	40},
{"name":"Coffee Mocachino","price":	51},
{"name":"Coffee Americano (Black)","price":	55},
{"name":"Coffee Espresso","price":	60},
{"name":"Ice Tea (Lemon)","price":	51},
{"name":"Coffee Cappuccino","price":	51},
{"name":"Espresso (Black)","price":	55},
{"name":"Cold-Coffee (Frappe)","price":	70},

{"name":"Cola / Orange / Lemon","price":	55},
{"name":"Diet Pepsi","price":	55},
{"name":"Fresh Lime Soda Sweet / Salt","price":	60},
{"name":"Mineral Water","price":	55},
{"name":"Fresh lime Water Sweet / Salt","price":	60}]


def display_menu(menu):
    for item in menu:
        print(f"{item['name']} - ₹{item['price']:.2f}")

def place_order(menu):
    order = []
    total = 0
    while True:
        item = input("Enter the name of the item you would like to order, or 'done' to finish: ")
        if item.lower() == "done":
            break
        else:
            match = next((x for x in menu if x["name"].lower() == item.lower()), None)
            if match:
                order.append(match["name"])
                total += match["price"]
            else:
                print("Invalid item. Please try again.")
    return order, total


if __name__ == "__main__":
    display_menu(menu)
    order, total = place_order(menu)
    print("Order: ", order)
    print("Total: ₹" + str(total))