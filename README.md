# autoweb
2gb memory 
安装pip sudo apt-get install pip
安装git sudo apt-get install git，https://www.cnblogs.com/zhcncn/p/4030078.html
安装 selenium: sudo pip install selenium
安装 chromedriver: https://blog.csdn.net/pangtouyu_qy/article/details/80282795
安装 chrome : sudo apt-get update, https://blog.csdn.net/sdujava2011/article/details/50880663
安装python 库，  sudo pip install XXX
运行test.sh

#git
为GitHub上的Repository提交修改
（1）git clone已存在GitHub上的Repository。（在新建的~/MyTestFolder目录中）

git clone https://github.com/zhchnchn/ZhchnchnTest.git
（2）修改一个文件，然后提交

vim README.md
git status
git add README.md
git status
git commit -m "Edit by WorkUbuntu 1204"
git status
git remote add origin https://github.com/zhchnchn/ZhchnchnTest.git
这时会报错误：

fatal: remote origin already exists.

解决办法【3】：

$ git remote rm origin
然后再次执行 git remote add origin https://github.com/zhchnchn/ZhchnchnTest.git

（3）之后，需要将修改push到GitHub上

git push -u origin master
