def cylinder_volume(radius, heigh):
    print("radous:", radius)
    print("height:", heigh)
    volume=3.14*(radius**2)*heigh
    return volume
r=5
h=10
print(cylinder_volume(h, r))