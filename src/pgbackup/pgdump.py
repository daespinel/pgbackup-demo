import subprocess
import sys

# dump = pgdump.dump('postgres://user:passwd@ip:80/sample')
def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {error}")
        sys.exit(1)

def dump_file_name(url, timestamp=None):
    db_name = url.split('/')[-1]
    db_name = db_name.split('?')[0]
    if timestamp:
        return f"{db_name}--{timestamp}.sql"
    else:
        return f"{db_name}.sql"


        