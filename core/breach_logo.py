  #!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import sys # System.
import time # The Time.
import core.colors as colors # We all love a splash of color.
import core.mods as mods # So we can let people modify it easier!

# Main logo.
def breach_logo():
    mods.clear_screen()
    print(colors.bcolors.BLINK + colors.bcolors.RED + '''
                     &&##BBBBB##&&                                              
               &##GJ!^:::.....:::^~!7JP& &                                      
            BY!:.:^7J5?:...............^YB??P#                                  
         &5~. .......^JB7................7#~ :~JG&                              
        Y^ ............!&?^~~~^^::........5B... .^?G                            
      B~ .......:^!JY555G&#555PPPP5YJ7~:. 7 :.......~Y#                         
     P:......:!YGG5J!^::.^5Y...::^^!?Y5557P5..........:J#                       
    G......:J#&5!:.........GJ ........:Y&  G?^......... :5                      
   &^ ....7# P^........:^~~YG~~^:.... Y ?5#   G7:..:......BGB                   
   B7?7~.?  Y.......~JG#&      &#BPJ7^7&^.:~?5B #Y^.......5B:J&                 
   !:^~7J& B.... :JB                  G&J......^7PBY^.....P&: :Y                
  &:... ?  #???7?#                 #5?~?&^...^!~:.:?P?...:&B... ^G              
  #.....5  #:..7                 P!:....BG:..7  &BY~:YP: J 7......?             
  #:....G  &^. !               P~.....:.:GG^..Y     B7GB7 G:...... Y            
   ~....G   Y .^&            &7......:::..?PJ~.!P&    &  PB B5~....Y            
   J .. 5    !  Y           B^ ...::::::::..7BBY7?5B&&BY~.^5#  ~...^P           
   #:...!    &7  5         G. .:::....:::::?#&5!!7!!~^...:..:!5!.:...?#         
    5 ...G     5: J       #!7?JJJJJ?7~:..:P P^........:::::::..:::::..:5        
     J . ^&     &5~!P&    G?#^:::::^!?J?^Y 5..:::::::::::::::::::::::...!B      
      Y.  ~&       #PG&  Y:.#7.:::::..:~?  !.:::...:::::::::::::::::::....J     
       G^  ^B           J ..Y&~.:::::::.^& G:...:~^...:::.:::.::::::::...:^~G   
        &J: .5         G....:P ?:..:::::.?& B!..B &G?:..^JYJ??!:.:::::...7&5^&  
          &Y^ ~G       7 ....:J#BJ~:...::.~P  G7P    #J~#Y^.:^YB5~..:.....^#B   
             G7:!P     ~....::.:!Y55J7~:....~Y& &      B?!JJ~..^5#P!....  :#    
               &GYYG&  ? ....:::..:^!?5P5?^...:J&    #?:...~5Y^..:?557^!?5#     
                   &&  &~ .....:::::...:!YGP?:. ^G  B^ ....:7B#:  .~P           
                        &J^.......::::::..:!5BY: .G Y ....!#  &7?5B             
                          &P?~:.........::...^5B? ^ &7... 5                     
                              &BPJ7!^:.........~B5.G  P~. .5                    
                                    &#BPY7^. ....55P    G7. ~B                  
                                           B5!.   Y       #J  J                 
                                              #Y^  5        B: #                
                                                 P~.B        YJ                 
                                                   5?        &                  
                                                    &                           
                      ____   .___  .____      .      ___  __  __
                      /   \  /   \ /         /|    .'   \ |   | 
                      |,_-<  |__-' |__.     /  \   |      |___| 
                      |    ` |  \  |       /---'\  |      |   | 
                      `----' /   \ /----/,'      \  `.__, /   / 
  ''' + colors.bcolors.ENDC + colors.bcolors.ENDC)
time.sleep(2)  # Change load times by changing this!
mods.clear_screen()  # Runs the clear screen mod.
def display_notice():
  print(f'''
#                                 {colors.bcolors.RED}(♥{colors.bcolors.ENDC} v 2.5.0 {colors.bcolors.RED}♥){colors.bcolors.ENDC}
#
#  Lead & Developer:                 {colors.bcolors.RED}Shepherd{colors.bcolors.ENDC}
#  Main repository : {colors.bcolors.UNDERLINE}https://github.com/ItsJustShepherd/Shepherd-Project{colors.bcolors.ENDC}
#  
#  {colors.bcolors.BOLD}NOTICE:{colors.bcolors.ENDC} {colors.bcolors.BLINK}Onus is on the user for using within the remits of the law.{colors.bcolors.ENDC}
#  (The developers nor open source framework developers are responsible for any actions performed by the end user){colors.bcolors.ENDC}
''')