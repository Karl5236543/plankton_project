from django.db import models
from django.urls import reverse
import uuid


class Research(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    area_name = models.CharField(max_length=200)
    area = models.JSONField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    THEAD = [
        ("create_time", "время создания"),
        ("name", "название"),
        ("area_name", "название раёна"),
        ("count", "количество станций")
    ]

    @staticmethod
    def get_field_name(title):
        return [row[0] for row in Research.THEAD if row[1] == title][0]
    
    @staticmethod
    def get_thead():
        return [row[1] for row in Research.THEAD]

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('research', kwargs={'id': self.id})

    def get_edit_url(self):
        return reverse('research_edit', kwargs={'id': self.id})

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

    THEAD = [
        ("create_time", "время создания"),
        ("name", "название"),
        ("depth", "глубина"),
        ("date", "время прибытия"),
        ("count", "количество образцов")
    ]

    @staticmethod
    def get_field_name(title):
        return [row[0] for row in Station.THEAD if row[1] == title][0]
    
    @staticmethod
    def get_thead():
        return [row[1] for row in Station.THEAD]

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('station', kwargs={'id': self.id})

    def get_edit_url(self):
        return reverse('station_edit', kwargs={'id': self.id})

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

    THEAD = [
        ("create_time", "время создания"),
        ("horizont", "горизонт"),
        ("time", "время сбора"),
        ("count", "количество клеток")
    ]

    @staticmethod
    def get_field_name(title):
        return [row[0] for row in Sample.THEAD if row[1] == title][0]
    
    @staticmethod
    def get_thead():
        return [row[1] for row in Sample.THEAD]

    def __str__(self):
        return f"{self.time} {self.time}"

    def get_absolute_url(self):
        return reverse('sample', kwargs={'id': self.id})

    def get_edit_url(self):
        return reverse('sample_edit', kwargs={'id': self.id})

    def get_cell_count(self):
        return sum([cell.count for cell in self.cells.all()])

    def get_cell_count_with_type(self, type_id):
        return sum([cell.count for cell in self.cells.filter(type_id=type_id)])

    


class Cell(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='cells')
    form = models.ForeignKey('Form', on_delete=models.CASCADE, related_name='cells')
    sample = models.ForeignKey('Sample', on_delete=models.CASCADE, related_name='cells')
    count = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)


    THEAD = [
        ("create_time", "время создания"),
        ("type", "тип"),
        ("form", "форма"),
        ("count", "количество"),
        ("V", "V"),
        ("P", "P"),
    ]

    @staticmethod
    def get_field_name(title):
        return [row[0] for row in Cell.THEAD if row[1] == title][0]
    
    @staticmethod
    def get_thead():
        return [row[1] for row in Cell.THEAD]

    def get_absolute_url(self):
        return reverse('cell', kwargs={'id': self.id})

    def get_edit_url(self):
        return reverse('cell_edit', kwargs={'id': self.id})

    def get_report_url(self):
        return reverse('cell_report', kwargs={'id': self.id})

    def __str__(self):
        return f"{self.type.name} - {self.form.name}"


class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name =  models.CharField(max_length=50)
    formula_V = models.CharField(max_length=50)
    formula_P = models.CharField(max_length=50)
    parameters_V = models.CharField(max_length=50)
    parameters_P = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='form/%Y/%m/%d/', default='form/default.png')

    def get_parameters_V(self):
        return self.parameters_V.split(',')

    def get_parameters_P(self):
        return self.parameters_P.split(',')


    def __str__(self):
        return f"{self.name}"


class Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"




class Cell_params(models.Model):
    FORMULA = (
        ('V', 'Volume'),
        ('P', 'Perimeter'),
    )
    cell = models.ForeignKey('Cell', on_delete=models.CASCADE, related_name='parameters')
    name = models.CharField(max_length=10)
    value = models.FloatField()
    formula = models.CharField(max_length=1,
                                      choices=FORMULA,
                                      default='V')

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('cell', kwargs={'id': self.id})