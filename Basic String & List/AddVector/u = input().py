u = input()
v = input()

mod_u = u[1:9]
mod_v = v[1:9]

ux, uy, uz = mod_u.split(", ")
list_u = [float(ux), float(uy), float(uz)]
vx, vy, vz = mod_v.split(", ")
list_v = [float(vx), float(vy), float(vz)]

ux, uy, uz = list_u
vx, vy, vz = list_v

sum =[ux+vx, uy+vy, uz+vz]

print(u,"+",v,"=",sum)