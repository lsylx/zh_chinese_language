### 中文语言包
ERPNext中文语言包，支持13版本和14版本，斐浦软件出品。

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

#### 许可

MIT