import datetime
import haystack
import haystack.indexes
from trans.models import Unit

class UnitIndex(haystack.indexes.RealTimeSearchIndex):
    text = haystack.indexes.CharField(document = True, model_attr = 'source')
    checksum = haystack.indexes.CharField(model_attr = 'checksum')
    fuzzy = haystack.indexes.BooleanField(model_attr = 'fuzzy')
    translated = haystack.indexes.BooleanField(model_attr = 'translated')
    translation = haystack.indexes.IntegerField(model_attr = 'translation__id')
    project = haystack.indexes.IntegerField(model_attr = 'translation__subproject__project__id')
    language = haystack.indexes.IntegerField(model_attr = 'translation__language__id')

haystack.site.register(Unit, UnitIndex)
