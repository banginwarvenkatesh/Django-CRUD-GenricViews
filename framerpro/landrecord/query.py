from .models import LandRec

s = LandRec.objects.all().count()
print(s)