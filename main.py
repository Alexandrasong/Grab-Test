import json
import unittest

import requests


class Question1(unittest.TestCase):
    def test1(self):
        self.assertEqual('[1,9],[1,9],[2,8],[3,7]', question1([1, 2, 3, 7, 8, 9, 9, 5], 10))

    def test2(self):
        self.assertEqual('[1,9],[1,9],[2,8],[3,7]',question1_update([1, 2, 3, 7, 8, 9, 9, 5], 10))

class Question2(unittest.TestCase):
    def test1(self):
        result = question2('GuangZhou')['latLng']
        self.assertTrue(str(result['lat']).startswith('23') and str(result['lng']).startswith('113'))

    def test2(self):
        result = question2('GuangZhou', True)['ignoreLatLngInput']
        self.assertTrue(result)

    def test3(self):
        result = question2('GuangZhou', False)['ignoreLatLngInput']
        self.assertTrue(not result)


def question1(list, sum):
    list.sort()
    result = []
    for index in range(len(list)):
        for index2 in range(index, len(list)):
            if index != index2 and list[index] + list[index2] == sum:
                result.append('[%d,%d]' % (list[index], list[index2]))
    return ','.join(result)


def question1_update(list, sum):
    list.sort()
    result = []
    first = 0
    last = len(list) - 1
    s = 0
    while first < last:
        s = list[first] + list[last]
        if s == sum:
            result.append('[%d,%d]' % (list[first], list[last]))
            last = last - 1
        elif s < sum:
            first = first + 1
        else:
            last = last - 1
    return ','.join(result)


key = 'lYrP4vF3Uk5zgTiGGuEzQGwGIVDGuy24'


def question2(location, ignoreLatLngInput=False):
    response = requests.get(
        'https://www.mapquestapi.com/geocoding/v1/address?key=%s&location=%s&ignoreLatLngInput=%s' % (
            key, location, str(ignoreLatLngInput)))
    if response.status_code == 200:
        result = json.loads(response.content.decode(response.apparent_encoding))
        data_result = {}
        if 'results' in result and len(result['results']) > 0 and 'locations' in result['results'][0] and len(
                result['results'][0]['locations']) > 0 and 'latLng' in result['results'][0]['locations'][0]:
            data_result['latLng'] = result['results'][0]['locations'][0]['latLng']
        else:
            raise Exception("NotFound latLng")
        if 'options' in result and 'ignoreLatLngInput' in result['options']:
            data_result['ignoreLatLngInput'] = result['options']['ignoreLatLngInput']
        else:
            raise Exception("NotFound ignoreLatLngInput")
        return data_result
    else:
        raise Exception(response.content.decode(response.apparent_encoding))


if __name__ == '__main__':
    unittest.main()