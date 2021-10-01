---
title: "[AWS] CLI - S3 Presign URL"
date: 2020-10-01 16:34:00 -0400
categories: aws
---

CLI Command to set S3 Presign URL to the object

```sh
# choose proper region
aws s3 presign s3://bucketname/object --region my-region

# custome expiration time
aws s3 presign s3://bucketname/object --expires-in 300 --region my-region

# If you have setting problem, set proper signature version to generate correct URL for encrypted files
aws configure set default.s3.signature_version s3v4
```