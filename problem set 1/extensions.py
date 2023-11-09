file = (input("File name: ")).lower().strip()
file = file.split(".")[1]

match file:
    case "gif" | "jpg" | "jpeg" | "png":
        print("image/" + file)
    case "pdf" | "zip":
        print("application/" + file)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")