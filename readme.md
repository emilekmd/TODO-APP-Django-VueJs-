# Features

## Todo feature

[x] Create a task  
[x] Read all tasks  
[x] Read one task  
[x] Update a task  
[x] Delete a task  

## Account feature

[x] Register (create simple or super rigth account)  
[x] Login  
[x] Logout

# Dev Routs

## Tasks

### Enable `task creation`
>http://127.0.0.1:8000/task/create/  
`input` : [description]  
`outpout` : [task]

### Enable `tasks reading`
>http://127.0.0.1:8000/task/gettasks/  
`input` : []  
`outpout` : [tasks]


### Enable `task reading`
>http://127.0.0.1:8000/task/gettask/  
`input` : [id]  
`outpout` : [task]

### Enable tasks `updating`
>http://127.0.0.1:8000/task/update/  
`input` : [id,new_description]  
`outpout` : [task]

### Enable `tasks deleting`
>http://127.0.0.1:8000/task/delete/  
`input` : [id]  
`outpout` : [ok_status]

## Users

### Enable tasks `create a simple user`
>http://127.0.0.1:8000/account/create_user/  
`input` : [email,first_name,last_name,password]  
`outpout` : [ok_status]

### Enable tasks `create a simple` super user
>http://127.0.0.1:8000/account/create_super_user/  
`input` : [email,first_name,last_name,password]  
`outpout` : [ok_status]


### Enable tasks `login` user
>http://127.0.0.1:8000/account/login/  
`input` : [email,password]  
`outpout` : [bio_data,token]

### Enable tasks `logout` user
>http://127.0.0.1:8000/account/logout/  
`input` : []  need token in the request header  
`outpout` : [ok_status]