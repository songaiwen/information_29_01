"""
权限问题:1.开启服务端,使用sudo mongod --auth, 然后客户端使用mongo开启的时候没有警告
        2.此时是查询不了数据库的,需要先创建用户,切换到admin使用use admin 然后创建新用户
        3.db.createUser({user : "python", pwd : "123456", roles : ["root"]})
            用户名:python, 密码:123456, 拥有root权限
        4.如果 MongoDB 开启了权限模式，并且某一个数据库没有任何用户时，可以不用认证权限并创建一个用户，但是当继续创建第二个用户时，会返回错误，若想继续创建用户则必须认证登录。
        5.认证登录到python用户（第一次创建的用户）
            db.auth("python","123456") 返回1表示验证成功
            查看当前认证登录的用户信息
            show users
            {
                "_id" : "admin.python",
                "user" : "python",
                "db" : "admin",
                "roles" : [
                    {
                        "role" : "root",
                        "db" : "admin"
                    }
                ]
            }
        6.认证成功以后,可以继续创建第二个用户
        db.createUser({user : "songyuxi", pwd : "123456", roles : [{role : "read", db : "db_01"}, {role : "readWrite", db : "db_02"}]})
        用户名：songyuxi，密码：123456，角色权限：[对db_01 拥有读权限，对db_02拥有读/写权限]
        show users
        {
            "_id" : "admin.songyuxi",
            "user" : "songyuxi",
            "db" : "admin",
            "roles" : [
                {
                    "role" : "read",
                    "db" : "db_01"
                },
                {
                    "role" : "readWrite",
                    "db" : "db_02"
                }
            ]
        }

        7.查看当前数据库下所有的用户信息
        db.system.users.find()
        8.认证登陆到songyuxi用户
        db.auth("songyuxi", "123456")
        9.切换到数据库db_01 读操作没有问题
        10. 注意点:如果此时需要认证到python用户下的话,需要先db查看一下此时并没有在admin模式下,所以认证失败
            需要use  admin到里面,然后再登陆python用户

        11.在拥有root权限的python用户里面删除其他用户
        db.dropUser("songyuxi") 返回true

        12.也可以把自己删除
        db.dropUser("python")

"""
#1.查看mongoDB里面所有的数据库
