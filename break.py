key_location= "chair"
location= ["sofa", "garage", "chair", "tabel", "closet"]
for loc in location:
    if loc==key_location:
        print("key found at", loc)
        break
    else:
            print("key not found at", loc)