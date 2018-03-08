# Regis Layers Backend

Start webdav:
```
wsgidav --host=0.0.0.0 --port=4202 --root=$PWD/data
```

Start server:
```
python server.py
```

Start and populate MongoDB:
```
docker run --name geovis_mongo --rm -d -p 27017:27017 mongo
python populateLayers.py
```


Needs: `dnf install libcurl-devel` for webdavclient
