###
1.git 的安装 
2. 获取源代码：
	git clone   https://github.com/Monarsoft/AllTutorialsAreInHTMLFormat.git

3. 创建库

4. 生成公钥 (用于指定的计算机可以以上传)
	ssh-keygen -C "monarsoft@outlook.com" -t rsa

5.
	git config --global user.email "monarsoft@outlook.com"
	git config --global user.name "Monarsoft"

6. 上传代码
..或在命令行上创建一个新的存储库
	echo“＃ - ”>> README.md 
	git init 
	git add README.md 
	git commit -m“first commit” 
	git remote add origin https://github.com/Monarsoft/-.git
	 git push -u origin master

...或从命令行推送现有存储库
	git remote add origin https://github.com/Monarsoft/-.git
	 git push -u origin master

...或从另一个存储库导入代码
您可以使用Subversion，Mercurial或TFS项目中的代码初始化此存储库。