---
title: Security Features
keywords: overview
sidebar: mydoc_sidebar
permalink: features.html
---

Dow Jones Hammer can identify and report the following issues:

|Name                                                              |Description                                            |Default Alert Trigger                                                           |
|------------------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------------------------------|
|[S3 ACL Public Access](playbook1_s3_public_buckets_acl.html)      |Detects publicly accessible by ACL S3 buckets          |Any of the S3 buckets is worldwide accessible by ACL                            |
|[Insecure Services](playbook2_insecure_services.html)             |Detects groups with worldwide open ports from the list |Any of security groups allows unrestricted access to the ports defined in the configuration file|
|[IAM User Inactive Keys](playbook3_inactive_user_keys.html)       |Detects unused for N days access keys                  |Any of access keys is not used for the timeframe defined in the configuration file              |
|[IAM User Keys Rotation](playbook4_keysrotation.html)             |Detects the lack of access keys rotation for N days    |Any of access keys was created earlier than the timeframe defined in the configuration file     |
|[S3 Policy Public Access](playbook5_s3_public_buckets_policy.html)|Detects publicly accessible by policy S3 buckets       |Any of the S3 buckets is worldwide accessible by policy                         |
|[CloudTrail Logging Issues](playbook6_cloudtrail.html)            |Detects CloudTrail logging status and permission issues|Any of AWS regions does not have CloudTrail logging enabled or has access issues|
|[EBS Unencrypted Volumes](playbook7_ebs_unencrypted_volumes.html) |Detects not encrypted at rest EBS volumes              |Any of the EBS volumes is not encrypted at rest                                 |
|[EBS Public Snapshots](playbook8_ebs_snapshots_public.html)       |Detects publicly accessible EBS snapshots              |Any one of EBS snapshots is worldwide accessible                                |
|[RDS Public Snapshots](playbook9_rds_snapshots_public.html)       |Detects publicly accessible RDS snapshots              |Any one of RDS snapshots is worldwide accessible                                |
|[SQS Policy Public Access](playbook10_sqs_public_policy.html)     |Detects publicly accessible SQS policy                 |Any of SQS queues is worldwide accessible by policy                             |
|[S3 Unencrypted Buckets](playbook11_s3_unencryption.html)         |Detects not encrypted at reset S3 buckets              |Any of S3 bucket is not encrypted at rest                                       |
|[RDS Unencrypted instances](playbook12_rds_unencryption.html)     |Detects not encrypted at rest RDS instances            |Any one of RDS instances is not encrypted at reset                              |
|[AMIs public access](playbook13_amis_public_access.html)     |Detects publicly accessible AMIs            |Any one of AMI is worldwide accessible                             |
|[Redshift Unencrypted Clusters](playbook15_redshift_unencryption.html)     |Detects Redshift unencrypted cluster issues   |Any one of Redshift cluster is not encrypted at rest                              |
|[Redshift Public Access Clusters](playbook16_redshift_public_clusters.html)     |Detects Redshift publicly accessible cluster isues |Any one of Redshift cluster publicly accessible                  |
|[Redshift Logging Issues](playbook17_redshift_audit_logging.html)     |Detects Redshift logging issues            |Any one of Redshift cluster logging is not enabled                              |
|[ECS Logging](playbook18_ecs_logging.html)     |Detects ECS task definition's logging issues   |Any one of ECS task definition's logging enabled or not                              |
|[ECS Privileged Access](playbook19_ecs_privileged_access.html)     |Detects ECS task definition's privileged access issues |Any one of ECS task definition have privileged access enabled or not                  |
|[ECS External Image Source](playbook20_ecs_external_image_source.html)     |Detects ECS task definitions image source issues  |Any one of ECS image source is external or internal                              |
|[Elasticsearch Domain Encryption Issues](playbook21_elasticsearch_unencryption.html)     |Detects Elasticsearch domains encryption issues            |Any one of Elasticsearch Domain unencryption issue                        |
|[Elasticsearch Domain Public Access Issues](playbook22_elasticsearch_public_access.html)     |Detects Elasticsearch domain public access issues      |Any one of Elasticsearch Domain public access issue |
|[Elasticsearch Domain Logging Issues](playbook23_elasticsearch_logging.html)     |Detects Elasticsearch domains logging issues            |Any one of Elasticsearch Domain logging issue                        |

Dow Jones Hammer can perform remediation for all issues [except](remediation_backup_rollback.html#1-overview) **EBS Unencrypted volumes**, **CloudTrail Logging Issues**, **RDS Unencrypted instances** **ECS Logging**, **ECS Privileged Access**, **ECS External Image Source**, **Redshift Audit Logging** and **Elasticsearch Domain Encryption Issues**.

