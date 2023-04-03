from django.contrib.auth.models import User

adm = User.objects.filter(username='admin')
adm.delete()
usr = User.objects.create_superuser('admin' 'sofya140202@mail.ru' 'password')
usr.save()
