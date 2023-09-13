#!/bin/sh

curl -D- -X POST
-H "Authorization: Bearer YOUR_TOKEN"
-H "X-Atlassian-Token: nocheck"
-H "Content-Type: multipart/form-data"
-F "file=@/path/to/attachment.txt"
-F "comment=This is my comment"
"https://your-jira-domain.atlassian.net/rest/api/2/issue/ISSUE-123/comment"
