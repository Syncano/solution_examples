import datetime

import syncano
from syncano.models.base import Object

config = {
    "class_name": "archivable",
    "instance_name": "archiving_solution",
    "time_unit": "minutes",
    "interval": 2,
    "api_key": "YOUR_API_KEY"
}

# default values would be updated from codebox CONFIG
config.update(CONFIG)

# Make connection to Syncano
syncano.connect(api_key=config["api_key"])

now = datetime.datetime.now()
date_to_archive = now - datetime.timedelta(**{config['time_unit']: config['interval']})

objects = Object.please.list(
    class_name=config["class_name"],
    instance_name=config["instance_name"]
).filter(deleted=True, updated_at__lte=date_to_archive)

print 'Archiving objects of class %s' % config["class_name"]

deleted = 0
for o in objects:
    o.delete()
    deleted += 1

print 'Removed %s objects, done!' % deleted
