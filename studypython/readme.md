代码要放在含有.idea的文件夹中，然后在CMD上运行
git需下载本地客户端
官网下载：https://git-scm.com/downloads
新建文件夹，把代码包放进去，打开文件夹，看到有 .dea字样代表可以在本层使用git命令
打开CMD
第一次使用提示输入用户名和密码
git config --golbal user.name "账户名"
git config --golbal user.email "邮箱"
git init #c初始化本地仓库
git add *#tianjia suoyou wenjian
git commit -m "你的描述"
git remote add origin https://github.com/账户名/仓库名.git
git pull #先拉取一次
git push -u origin master#推送到远程仓库，出错的话用强制推送git push -u  -f origin master

更新操作：
git status
git add *
git commit -m "描述”
git pull
git push origin master


新建文件夹，进去后CMD
git clone 地址
难学哦