#%%
values = 1,2,3,4,5,6 # tuple
x, y, *z = values    # z artık bir listedir
print(x,y,z)
# %%
# Identity operator = is
x = y = [1,2,3] # x ve y aynı referansı tutar
z = [1,2,3]     # z aynı değerlere sahip olsa da farklı adrestedir

print(x==y) # == değerleri kontrol eder
print(x==z)
print(x is y) # is referanslarının eşitliğini kontrol eder
print(x is not y)
print(x is z)
# %%
