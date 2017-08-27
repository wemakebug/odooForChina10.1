# odooForChina10.1
# ubuntu

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

`pip install -r requires.txt -i https://pypi.douban.com/simple`

这里在安装的时候 `python-ldap`这个库可能会出错
先执行这个

```
sudo apt-get install python-dev libldap2-dev libsasl2-dev libssl-dev
sudo pip install python-ldap
```
然后在重新执行上面那条命令

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

补充：
[nginx + uwsgi部署odoo服务](https://suadminwen.github.io/nginx-+-uwsgi%E9%83%A8%E7%BD%B2odoo%E6%9C%8D%E5%8A%A1)
[nginx+uwsgi实现负载均衡](https://suadminwen.github.io/nginx+uwsgi%E5%AE%9E%E7%8E%B0%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1)
