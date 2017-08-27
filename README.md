# odooForChina10.1
#

ubuntu
## 1、配置数据库

### 1）安装postgresql

  选定版本大于9.0
  命令：
```
sudo apt install postgresql

sudo apt install postgresql-server-dev-9.5
```

### 2)创建postgresql用户

`sudo su postgres`

`psql`

执行语句，创建root超级用户：

`CREATE ROLE root superuser;`

使用`\du`查询创建结果

修改root用户登录权限
  
`ALTER ROLE root login;`

### 3)安装使用的包

进入root用户
到目录 odoo.egg-info/下执行一下命令：

`pip install -r requires.txt`

## 2、安装这个东东

``` 
sudo apt install npm
sudo apt install node-less
sudo apt install nodejs-legacy
```

## 3、正确的打开方式

`python setup.py build`
`python setup.py install`

## 4、其他的的东西懒得写，自己总结去吧
