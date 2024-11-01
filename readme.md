# Features

## Todo feature

[x] Create a task  
[x] Read all tasks  
[x] Read one task  
[x] Update a task  
[x] Delete a task  

[x] create a cathegorie
[x] update a cathegorie
[x] delete a cathegorie

[] sort task by ['creation_date']

## Account feature

[x] Register (create simple or super rigth account)  
[x] Login  
[x] Logout

# Dev Routs

## Tasks

### Enable `task creation`
>http://127.0.0.1:8000/todo/createtask/  
`input` : [description]  
`outpout` : [task]

### Enable `tasks reading`
>http://127.0.0.1:8000/todo/gettasks/  
`input` : []  
`outpout` : [tasks]


### Enable `task reading`
>http://127.0.0.1:8000/todo/gettask/  
`input` : [id]  
`outpout` : [task]

### Enable tasks `updating`
>http://127.0.0.1:8000/todo/updatetask/  
`input` : [id,new_description]  
`outpout` : [task]

### Enable `cathegorie creating`
>http://127.0.0.1:8000/todo/createcathegorie/  
`input` : [name]  
`outpout` : []

### Enable `tasks updating`
>http://127.0.0.1:8000/todo/updatecathegorie/  
`input` : [old_name,new_name]  
`outpout` : []

### Enable `tasks deleting`
>http://127.0.0.1:8000/todo/deletecathegorie/  
`input` : [id]  
`outpout` : []

## Users

### Enable tasks `create a simple user`
>http://127.0.0.1:8000/account/create_user/  
`input` : [email,first_name,last_name,password]  
`outpout` : []

### Enable tasks `create a simple` super user
>http://127.0.0.1:8000/account/create_super_user/  
`input` : [email,first_name,last_name,password]  
`outpout` : []


### Enable tasks `login` user
>http://127.0.0.1:8000/account/login/  
`input` : [email,password]  
`outpout` : [bio_data,token]

### Enable tasks `logout` user
>http://127.0.0.1:8000/account/logout/  
`input` : []  need token in the request header  
`outpout` : []