
def _func(param_self, x):
    return param_self.x + x

class Scheduler(object):
    def check(self, node):
       return

    def run(self, node):
       return

    # ....

class RabbitMQ(object):
   def __init__(self, x):
       # _func is treated as DATA member of X instead of a formal method definition.
       self._scheduler = Scheduler()
       self.nodes = [MQNode(), MQNode()]
       self.x = x

       self._scheduler.check(self.nodes[0])
       self._scheduler.run(self.nodes[0])

       # Composition is a way to encapsulate behavior in a delegate object as opposed using
       # inheritance.
       f.func()


import abc

class Transformation(object):
    @abc.abstractmethod
    def execute(self, dataset):
       pass

class X(Transformation):
     # ...
     pass

class Y(Transformation):
     # ...
     pass

class Dataset(object):
    def transform(self, transformation):
         transformation.execute(self)
 

transformation = Mock()
d = Dataset()
d.transform(transformation)
transformation.execute.assert_called_once_with(d)

class BodyMeasurements(object):
    def __init__(self, height, weight):
       self.height = height
       self.weight = weight

    def density(self):
       return self.weight / self.height


class Person(object):
    def __init__(self, body_measurements, address, id):
        self.id = id
        self.address = address
        self.body_measurements = body_measurements

    def profile(self):
        return {
           "density": self.body_measurements.density(),
        }

from unittest import TestCase, Mock

class TestPerson(TestCase):
    def test_profile(self):
        p = Person(...)

        with Mock.do_the_mocking(p, "body_measurements") as m:
            p.profile()
            m.density.assert_called_once()

       

