from django.db import models
import subprocess
from django.utils import timezone

class VPNServer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    countryCode = models.CharField(max_length=10)
    configuration = models.TextField()
    
    def __str__(self):
        return self.name
    

class APIKey(models.Model):
    api_key = models.CharField(max_length=255, unique=True)

    def generate_key(self):
        # Получаем текущее время
        current_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        command = f'RezyH64 hash {current_time}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        self.api_key = result.stdout.strip()

    def save(self, *args, **kwargs):
        if not self.api_key:  # Генерируем ключ, если он не задан
            self.generate_key()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.api_key