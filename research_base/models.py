from django.db import models
from django.urls import reverse
import uuid


class Research(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    area_name = models.CharField(max_length=200)
    area = models.JSONField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('research', kwargs={'id': self.id})

    def get_station_count(self):
        return self.stations.count()

    class Meta:
        ordering = ["-create_time"]


class Station(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    coords = models.JSONField()
    depth = models.FloatField()
    date = models.DateTimeField()
    research = models.ForeignKey('Research', on_delete=models.CASCADE, related_name='stations')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('station', kwargs={'id': self.id})

    def get_sample_count(self):
        return self.samples.count()

    def get_coords(self):
        pass


class Sample(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    horizont =models.FloatField()
    time = models.DateTimeField()
    station = models.ForeignKey('Station', on_delete=models.CASCADE, related_name='samples')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.time} {self.time}"

    def get_absolute_url(self):
        return reverse('sample', kwargs={'id': self.id})

    def get_cell_count(self):
        return sum([cell.count for cell in self.cells.all()])

    


class Cell(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='cells')
    form = models.ForeignKey('Form', on_delete=models.CASCADE, related_name='cells')
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE, related_name='cells')
    count = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('cell', kwargs={'id': self.id})

    def __str__(self):
        return f"{self.type.name} - {self.form.name}"


class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name =  models.CharField(max_length=50)
    formula_V = models.CharField(max_length=50)
    formula_P = models.CharField(max_length=50)
    parameters_V = models.CharField(max_length=50)
    parameters_P = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"




class Cell_params(models.Model):
    cell = models.ForeignKey('Cell', on_delete=models.CASCADE, related_name='parameters')
    name = models.CharField(max_length=10)
    value = models.FloatField()

    def __str__(self):
        return f"{self.name}"