### Chinese Language
ERPNext Chinese Language Pack，support 13 Version and 14 Version .

#### Installation
cd  frappe-bench

Version 13：
bench get-app --branch master https://gitee.com/phipsoft/zh_chinese_language.git

Version 14：
bench get-app --branch version-14 https://gitee.com/phipsoft/zh_chinese_language.git

bench --site mfg.local install-app zh_chinese_language

bench clear-cache && bench clear-website-cache

sudo supervisorctl restart all

#### Update
cd  frappe-bench

bench update --apps zh_chinese_language --pull --reset

bench clear-cache && bench clear-website-cache

sudo supervisorctl restart all

#### License

MIT


