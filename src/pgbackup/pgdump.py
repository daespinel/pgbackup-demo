import subprocess
import sys

# dump = pgdump.dump('postgres://user:passwd@ip:80/sample')
def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {error}")
        sys.exit(1)

        