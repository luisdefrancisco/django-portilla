# Handling Errors: try-except-finally

#print("10"+10)

try:
    print('10'+10)
except IOError:
    print("You have an input-output exception")
    print("did you check permissions?")
except TypeError: #Sabemos que es ese error porque lo hemos intentado antes
    print("wrong typeError!")
except:
    print("Hey you've got an error")
finally:
    print("Finally block runs ALWAYS, ERROR OR NOT ERROR")

######## IMPORTANT ###########
#### Si no sabemos el error, dejamos solo except:
# Los errores se acumulan de arriba a abajo
# A veces se utiliza ELSE en vez de FINALLY