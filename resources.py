from minio import Minio
from minio.error import ResponseError
from configur import S3_BUCKET, S3_KEY, S3_SECRET
from flask import session

def _get_s3_resource():
    if S3_KEY and S3_SECRET:
        return Minio('play.min.io',
                  access_key='Q3AM3UQ867SPQQA43P2F',
                  secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                  secure=True)
    else:
        return 0


def get_bucket():
    s3_resource = _get_s3_resource()
    if 'bucket' in session:
        bucket = session['bucket']
    else:
        bucket = S3_BUCKET

    return(bucket,s3_resource.list_objects(bucket))

def get_buckets_list():
  minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG')
  return minioClient.list_buckets()
