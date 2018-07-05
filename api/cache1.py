import json
from django.conf import settings
from tastypie.cache import NoCache
from tastypie.cache import SimpleCache


class JSONCache(NoCache):
    def _load(self):
        data_file = open(settings.TASTYPIE_JSON_CACHE, 'r')
        return json.load(data_file)

    def _save(self, data):
        data_file = open(settings.TASTYPIE_JSON_CACHE, 'w')
        return json.dump(data, data_file)

    def get(self, key):
        data = self._load()
        return data.get(key, None)

    def set(self, key, value, timeout=60):
        data = self._load()
        data[key] = value
        self._save(data)
        
        
        
class NoTransformCache(SimpleCache):

    def cache_control(self):
        control = super(NoTransformCache, self).cache_control()
        control.update({"no_transform": True})
        return control
