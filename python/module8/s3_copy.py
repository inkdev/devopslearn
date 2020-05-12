import boto3


def copy_file_bucket(bucket_src,bucket_dst):
    s3 = boto3.resource('s3')

    bucketlist = [bucket.name for bucket in s3.buckets.all()]

    if bucket_dst not in bucketlist:
        s3.create_bucket(Bucket=bucket_dst)
        bucket_dst = s3.Bucket(bucket_dst)
        bucket_dst = bucket_dst.name

    bucket_dst = s3.Bucket(bucket_dst)
    for src in bucket_src:
        src = s3.Bucket(src)
        for file in src.objects.all():
            src_file = {'Bucket': file.bucket_name, 'Key': file.key}
            bucket_dst.copy(src_file, file.key)

#copy_file_bucket(['bogdanov-300320', 'bogdanov-310320'], 'bogdanov1052020')
