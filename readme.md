# Features

## Todo feature

[x] Create a task  
[x] Read all tasks
[x] Read one task  
[x] Update a task  
[x] Delete a task  

## Account feature

[x] create simple user
[x] create super user
[] Register
[] Login  
[] Logout  

# Dev Routs

### Enable task creation
>http://127.0.0.1:8000/task/create/  
`input` : [description]  
`outpout` : [task]

### Enable tasks reading
>http://127.0.0.1:8000/task/gettasks/  
`input` : []  
`outpout` : [tasks]


### Enable task reading
>http://127.0.0.1:8000/task/gettask/  
`input` : [id]  
`outpout` : [task]

### Enable tasks updating
>http://127.0.0.1:8000/task/update/  
`input` : [id,new_description]  
`outpout` : [task]

### Enable tasks deleting
>http://127.0.0.1:8000/task/delete/  
`input` : [id]  
`outpout` : [ok_status]