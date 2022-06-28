#!/bin/bash
#
#thanks for go-dork, use this tool for gg dork
#

## general
ex_domain1=""
ex_domain2=""

all_dork=(
"site:$1 inurl:callback_url -site:$ex_domain1 -site:$ex_domain2"
"site:$1 intitle:\"test\" -site:$ex_domain1 -site:$ex_domain2"
"inurl:https://trello.com AND intext:@$1"
"inurl:https://trello.com AND intext:$1"
"inurl:jira AND inurl:$1"
"site:$1 intitle:\"index of\""
## filetypes
"site:$1 filetype:wsdl"
"site:$1 DB_USERNAME filetype:env"
"site:$1 DB_PASSWORD filetype:env"
"site:$1 allintext:password filetype:log"
"site:$1 allintext:username filetype:log"
"site:$1 inurl:wsdl"
"site:$1 ext:svc inurl:wsdl"
"site:$1 filetype:doc"
"site:$1 filetype:docx"
"site:$1 filetype:xls"
"site:$1 filetype:xlsx"
"site:$1 filetype:ppt"
"site:$1 filetype:pptx"
"site:$1 filetype:mdb"
"site:$1 filetype:pdf"
"site:$1 filetype:sql"
"site:$1 filetype:txt"
"site:$1 filetype:rtf"
"site:$1 filetype:csv"
"site:$1 filetype:xml"
"site:$1 filetype:conf"
"site:$1 filetype:dat"
"site:$1 filetype:ini"
"site:$1 index of:id_rsa id_rsa.pub"
## public
"site:github.com \"$1\" \"Authorization\""
"site:pastebin.com \"$1\" \"Authorization\""
"site:pastebin.com \"$1\""
"site:github.com \"$1\""
"site:gitlab.com \"$1\""
## login pages
"site:$1 inurl:admin -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:login -site:$ex_domain1 -site:$ex_domain2" 
"site:$1 inurl:adminlogin -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:cplogin -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:weblogin -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:quicklogin -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:wp-admin -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:wp-login -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:portal -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:userportal -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:loginpanel -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:memberlogin -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:remote -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:dashboard -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:auth -site:$ex_domain1 -site:$ex_domain2"
"site:$1 inurl:exchange -site:$ex_domain1 -site:$ex_domain2"
)

/usr/local/bin/figlet -f /path_to_font/figlet-fonts/3d.flf "GG DORK"
#exit 0

if [ -z "$1" ]
	then 
		echo "please add domain, ex: example.com"
		exit 0
fi

for i in ${!all_dork[@]}; do
	go-dork -s -q "${all_dork[$i]}"
	sleep 5
done
