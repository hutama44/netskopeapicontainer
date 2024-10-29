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
import scim_delete_group
import scim_update_rm_group
import ucidemo

menu = {}
menu['1']="SCIM - Crear Usuario" 
menu['2']="SCIM - Leer Usuario"
menu['3']="SCIM - Borrar Usuario"
menu['4']="SCIM - Borrado Masivo"
menu['5']="SCIM - Leer Grupo"
menu['6']="SCIM - Crear Grupo"
menu['7']="SCIM - Actualizar Grupo"
menu['8']="SCIM - Borrar Grupo"
menu['9']="SCIM - Borrar Usuario de Grupo"
menu['10']="ZTNA - Cargar Aplicaciones Privadas"
menu['11']="ZTNA - Leer Publisher ID"
menu['12']="UEBA - Leer UCI de Usuario"
menu['13']="UEBA - UCI Demo"
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
      scim_delete_group.main() 
    elif selection == 9:
      scim_update_rm_group.main() 
    elif selection == 10:
      privateapp.main() 
    elif selection == 11:
      get_pub_id.main() 
    elif selection == 12:
      uba_uci.main() 
    elif selection == 13:
      ucidemo.main() 
    elif selection == 0: 
      break
    else: 
      print ("Opción no aceptada")
