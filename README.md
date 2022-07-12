### 中文语言包
ERPNext中文语言包，支持13版本和14版本，斐浦软件出品。
此中文语言包，是为ERPNext用户提供一个样例，用户可以自行修改词条；
已收录的词条仅为参考可能会持续更新，非斐浦软件商业项目所用词条。

#### 安装步骤
cd  frappe-bench

13版本：

bench get-app --branch master https://gitee.com/phipsoft/zh_chinese_language.git

14版本：

bench get-app --branch version-14 https://gitee.com/phipsoft/zh_chinese_language.git

bench --site mfg.local install-app zh_chinese_language

bench clear-cache && bench clear-website-cache

sudo supervisorctl restart all

#### 升级步骤

cd  frappe-bench

bench update --apps zh_chinese_language --pull --reset

bench clear-cache && bench clear-website-cache

sudo supervisorctl restart all

#### 使用方法

大家可以先Fork这个仓库，安装后，自行修改，修改词条后Upload自己的仓库，这样升级就是自己最新修改的；

修改方法：

1）Python词条：可以修改zh.csv文件；

2）JS词条：可以修改translation.js文件；

如果本地有修改，在系统升级前建议先上传，否则系统升级后就丢失了；

#### 许可

MIT