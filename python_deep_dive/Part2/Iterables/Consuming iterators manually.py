from collections import namedtuple

s = 'I sleep all night, and I work all day'

iter_s = iter(s)

print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))

cars = []

with open('cars.csv') as file:
    row_index = 0
    for line in file:
        # print(line, end='')
        if row_index == 0:
            # headers row
            headers = line.strip('\n').split(';')
            Car = namedtuple('Car', headers)
            print('headers', headers)
        elif row_index == 1:
            # data type row
            data_types = line.strip('\n').split(';')
            print('types', data_types)
        else:
            # data row
            data = line.strip('\n').split(';')
            car = Car(*data)
            cars.append(car)
            print(data)
        row_index += 1


def cast(data_type, value):
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'INT':
        return int(value)
    else:
        return str(value)


def cast_row(data_types, data_row):
    return [cast(data_type, value)
            for data_type, value in zip(data_types, data_row)]


with open('cars.csv') as file:
    row_index = 0
    for line in file:
        # print(line, end='')
        if row_index == 0:
            # headers row
            headers = line.strip('\n').split(';')
            Car = namedtuple('Car', headers)
            print('headers', headers)
        elif row_index == 1:
            # data type row
            data_types = line.strip('\n').split(';')
            print('types', data_types)
        else:
            # data row
            data = line.strip('\n').split(';')
            data = cast_row(data_types, data)
            car = Car(*data)
            cars.append(car)
            print(data)
        row_index += 1

cars = []
with open('cars.csv') as file:
    file_iter = iter(file)
    headers = next(file_iter).strip('\n').split(';')
    Car = namedtuple('Car', headers)
    data_types = next(file_iter).strip('\n').split(';')
    for line in file_iter:
        data = line.strip('\n').split(';')
        data = cast_row(data_types, data)
        car = Car(*data)
        cars.append(car)

# COMPREHENSION APPROACH
with open('cars.csv') as file:
    file_iter = iter(file)
    headers = next(file_iter).strip('\n').split(';')
    Car = namedtuple('Car', headers)
    data_types = next(file_iter).strip('\n').split(';')
    cars_data = [cast_row(data_types, line.strip('\n').split(';'))
                 for line in file_iter]
    cars = [Car(*data) for car in cars_data]
