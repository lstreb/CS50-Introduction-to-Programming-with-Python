fruit = input("Item: ").lower()

match fruit:
    case "apple":
        print("Calories: 130")

    case "banana":
        print("Calories: 110")

    case "pear" | "sweet cherries":
        print(100)

    case "grapes" | "kiwifruit":
        print(90)

    case "orange" | "watermelon":
        print(80)

    case "plums":
        print(70)

    case "grapefruit" | "nectarine" | "peach":
        print(60)

    case "avocado" | "cantaloupe" | "honeydew melon" | "pineapple" | "strawberries" | "tangerine":
        print(50)

    case "lime":
        print(20)

    case "lemon":
        print(15)
    
    case _:
        print("Invalid")
