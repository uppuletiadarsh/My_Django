from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20,unique=True)
    ename = models.CharField(max_length=20)
    salary = models.IntegerField(max_length=20)

    """<table>
                <tr>
                    <th>Eid</th>
                    <th><input type="number" name="eid"></th>
                </tr>
                <tr>
                    <th>Ename</th>
                    <th><input type="text" name="ename"></th>
                </tr>
                <tr>
                    <th>Sal</th>
                    <th><input type="number" name="sal"></th>
                </tr>
                <tr>
                    <th colspan="2"><input type="submit" name="Register"></th>
                </tr>
            </table>"""
