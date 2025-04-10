# Django Rest Framework (DRF):  

## Serializers:
* Will work very similar to forms and ModelForms   
1. serialization
2. deserialization
3. validations

## Serialization:
* The process of converting complex data types(model instances, qs) into python native data types(like dict) is called Serialization. The advantage is converting to json is very easy.
```py
emp = Employee.objects.get(id=1)
eserializer = EmployeeSerializer(emp)
eserializer.data

from rest_framework.renders import JSONRenderer
json_data = JSONRenderer().render(eserializer.data)
```  
#### How to serialize queryset:
```py
qs = Employee.objects.all()
eserializer = EmployeeSerializer(qs, many=True)
eserializer.data

json_data = JSONRender().render(eserializer.data)
```

## Deserialization:
* The process of coverting python native data types into databse supported complex types is called deserialization.

* Converting json data to python native data type:

```py
import io
from rest_framework.parser import JSONParser
stream=io.BytesIO(json_data)
pdata=JSONParser().parser(stream)
```

* By deserialization we have to convert python data to db supported complex type:
```py
serializer = EmployeeSerializer(data=pdata)
serializer.is_valid()
serializer.validated_data
```


## Use Case of SErialization and Deserialization:
1. Partner application wants all employee records in json format qs--->python native data type -->json data (JSONRenderer().render())
2. Partner application sending json data to create a new employee json data--->python native data type(JSONParser().parser()) python native data type--->database supposed complex form(Deserialization)


