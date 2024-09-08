from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class UserPredictModel(models.Model):

    
    Air_temperature_K = models.CharField(max_length=100)
    Process_temperature_K = models.CharField(max_length=100)
    Rotational_speed_rpm = models.CharField(max_length=100)
    Torque_Nm = models.CharField(max_length=100)
    Tool_wear_min = models.CharField(max_length=100)
    Failure_Type = models.CharField(max_length=200)

    

def __str__(self):
    return self.Air_temperature_K, self.Process_temperature_K, self.Rotational_speed_rpm, self.Torque_Nm, self.Tool_wear_min, self.Failure_Type


    
