import os
import tempfile
import json
import argparse


def work_w_dict(dct, key_name, value):
    if key_name not in dct:
        dct[key_name] = [value]
    else:
        dct[key_name] = dct[key_name] + [value]


def to_json(dct):
    return json.dumps(dct)


def from_json(file_name):
    with open(file_name, 'r') as file:
        f = file.readline()
        if f != '':
            return json.loads(f)
        else:
            return {}


def search(key, dct):
    if key in dct:
        return ', '.join(dct[key])
    else:
        return


def main():

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    with open(storage_path, 'w'):
        if os.path.isfile('storage.data'):
            data = from_json('storage.data')
        else:
            data = {}
        parser = argparse.ArgumentParser()
        parser.add_argument("-key", "--key", dest='key_name')
        parser.add_argument("-val", "--val", dest='value')
        args = parser.parse_args()
        if args.value:
            with open('storage.data', 'w') as new_data:
                work_w_dict(data, args.key_name, args.value)
                new_data.write(to_json(data))
        else:
            print(search(args.key_name, data))


if __name__ == '__main__':
    main()