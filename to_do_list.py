high_priority = []
medium_priority= []
low_priority = []
to_do_list =[
  high_priority,
  medium_priority,
  low_priority
]

def pretty_print():
    for row in to_do_list:
        for item in row:
            print('|'.join(f'{x :^15}' for x in item))
            print('---------------------------')


#Menu
while True:
  menu = input('Choose an option \n(add, view, remove,edit,close) \n> ').strip().lower()

  if menu == 'add':
    while True:
      task = input('Enter the item: ').strip().capitalize()
      due_date = input('When is due?: ').strip()
      priority = input('Enter prioty level (high / medium / low): ').strip().lower()
      if priority == 'high':
        high_priority.append([task,due_date,priority])
      elif priority == 'medium':
        medium_priority.append([task,due_date,priority])
      elif priority == 'low':
        low_priority.append([task,due_date,priority])

      add_again = input('Do you want to add another item(yes/no)? \n>  ')
      if add_again == 'yes':
        continue
      elif add_again == 'no':
        break
    

  if menu == 'view':
    while True:
      view_scope = input('Enter the view scope. \n(view all / view priority level) \n> ').lower().strip()
      if view_scope == 'view all':
        pretty_print()
        break
      elif view_scope == 'view priority level':
        view_priority = input('Enter priority level. (high / medium / low) \n> ').lower().strip()
        
        if view_priority == 'high':
          for item in high_priority:
            print('|'.join(f'{x :^15}' for x in item))
  
        elif view_priority == 'medium':
          for item in medium_priority:
            print('|'.join(f'{x :^15}' for x in item))
  
        elif view_priority == 'low':
          for item in low_priority:
            print('|'.join(f'{x :^15}' for x in item))
        
        else: 
          print('INVALID OPTION. CHOOSE BETWEEN HIGH/MEDIUM/LOW')
          continue
        break
      else: 
        print('INVALID OPTION. CHOOSE BETWEEN VIEW ALL/VIEW PRIORITY')
        continue


  elif menu == 'edit':
    pretty_print()
    while True:
        to_be_changed = input('Enter the distinct item to change: ').strip().capitalize()
        found = False
        for row in range(len(to_do_list)):
            for item in range(len(to_do_list[row])):
                if to_do_list[row][item][0].capitalize() == to_be_changed:
                    to_change_to = input(f'Change {to_be_changed} to: ').strip().capitalize()
                    new_due_date = input(f'Change due date for {to_change_to} to: ').strip().capitalize()
                    new_priority_level = input(f'Change the priority level for {to_change_to} which is due on {new_due_date} (high/medium/low): ').strip().capitalize()
                    
                    # Remove the task from the current list
                    task_to_move = to_do_list[row][item]
                    to_do_list[row].remove(task_to_move)
                    
                    # Determine the new priority list
                    if new_priority_level == 'high':
                        high_priority.append([to_change_to, new_due_date, new_priority_level])
                    elif new_priority_level == 'medium':
                        medium_priority.append([to_change_to, new_due_date, new_priority_level])
                    elif new_priority_level == 'low':
                        low_priority.append([to_change_to, new_due_date, new_priority_level])
                    else:
                        print('INVALID PRIORITY LEVEL. CHOOSE BETWEEN HIGH/MEDIUM/LOW')
                        break
                    
                    found = True
                    pretty_print()
                    break
        if found:
            break
        if not found:
            print('INVALID OPTION. CHECK THE SPELLING.')



  elif menu == 'remove':
    pretty_print()
    while True:
        to_remove = input('Enter the item to be removed: ').strip()
        found = False
        for row in to_do_list:
            for item in row:
                if item[0] == to_remove:
                    row.remove(item)
                    found = True
                    break
            if found:
                break
        if found:
            print(f'{to_remove} has been removed.')
            break
        else:
            print('INVALID OPTION. CHECK THE SPELLING')

  elif menu =='close':
    print('Goodbye!')
    break
