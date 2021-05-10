"""
    Class defining the drivers for pg backup
    local driver: provides the backup locally
    s3 driver: Uses an S3 bucket for the backup
"""

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)