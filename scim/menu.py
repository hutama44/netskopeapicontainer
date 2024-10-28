import scim_put 
import scim_get_u
import scim_delete
import scim_delete_dom
import scim_get_g
import scim_put_group
import scim_update_group
import privateapp
import get_pub_id
import uba_uci

menu = {}
menu['1']="Crear Usuario" 
menu['2']="Leer Usuario"
menu['3']="Borrar Usuario"
menu['4']="Borrado Masivo"
menu['5']="Leer Grupo"
menu['6']="Crear Grupo"
menu['7']="Actualizar Grupo"
menu['8']="Cargar Aplicaciones Privadas"
menu['9']="Leer Publisher ID"
menu['10']="Leer UCI de Usuario"
menu['0']="Salir"
while True: 
    options=menu.keys()
    for entry in options: 
      print(entry, menu[entry])

    selection=int(input("Bienvenido, ¿qué deseas realizar?:")) 
    if selection ==1: 
      scim_put.main()
    elif selection == 2: 
      scim_get_u.main()
    elif selection == 3:
      scim_delete.main() 
    elif selection == 4:
      scim_delete_dom.main() 
    elif selection == 5:
      scim_get_g.main() 
    elif selection == 6:
      scim_put_group.main() 
    elif selection == 7:
      scim_update_group.main() 
    elif selection == 8:
      privateapp.main() 
    elif selection == 9:
      get_pub_id.main() 
    elif selection == 10:
      uba_uci.main() 
    elif selection == 0: 
      break
    else: 
      print ("Opción no aceptada")
