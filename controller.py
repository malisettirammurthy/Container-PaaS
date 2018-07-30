import sys, random
from threading import Thread
import docker
client = docker.from_env()

try:
    customer_image_name = sys.argv[1]
except Exception as emsg:
    print("Exception > " + str(emsg))
    sys.exit(2)

def poll_logs():
    pass

def poll_events(client = None):
    if not client:
        return
    events = client.events()
    for event in events:
        print("EVENT - " + str(event))
    events.close()

events_thread = Thread(target=poll_events, args=(client,))
events_thread.start()
"""
prev_images = client.images.list()
for i in prev_images:
    if i.attrs.has_key('RepoTags') and customer_image_name in i.attrs['RepoTags']:
        print("image already exists!!! so breaking")
        break
else:
    client.images.pull(customer_image_name)
"""
try:
    client.images.pull(customer_image_name)
except Exception as emsg:
    print("Exception > Image pull failed.. >" + str(emsg))
    sys.exit(2)


container_name = "c{0}".format(random.randint(1,101))
#container = client.containers.run(customer_image_name, entrypoint="/data/script.sh", detach = True, name = container_name)
#for line in container.logs(stream=True):
#    print(line.strip())

container = client.containers.run(customer_image_name, detach = True, name = container_name)
print(container)
print("Created container - {0}".format(container_name))


exit_code, cmd_output = container.exec_run("/data/script.sh", stream=True)
for line in cmd_output:
    print(line)
print("code - {0}".format(exit_code))
#events_thread._stop()
print("completed script execution")

container.stop()
print("Container stop issued..")






