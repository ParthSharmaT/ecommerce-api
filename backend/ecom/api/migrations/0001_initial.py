from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user=CustomUser(
            name="parth",
            email="parthsharma200018@gmail.com",
            is_staff="True",
            is_superuser="True",
            phone="7060626729",
            gender="Male"
        )
        user.set_password("123456789")
        user.save()    
    dependencies=[
        
    ]    
    operations=[
        migrations.RunPython(seed_data)
    ]