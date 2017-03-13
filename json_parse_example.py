
def sample2():
    import json, requests, pprint

    url = 'http://maps.googleapis.com/maps/api/directions/json?'

    params = dict(
        origin='Chicago,IL',
        destination='Los+Angeles,CA',
        waypoints='Joplin,MO|Oklahoma+City,OK',
        sensor='false'
    )

    data = requests.get(url=url, params=params)
    binary = data.content
    output = json.loads(binary)

    print 'data.content:', binary
    print 'json.loads(binary):', output

    # test to see if the request was valid
    #print output['status']

    # output all of the results
    #pprint.pprint(output)

    # step-by-step directions
    for route in output['routes']:
            for leg in route['legs']:
                for step in leg['steps']:
                    print step['html_instructions']

def sample1():
    import json

    json_input = '{ "one": 1, "two": { "list": [ {"item":"A"},{"item":"B"} ] } }'

    try:
        decoded = json.loads(json_input)

        # pretty printing of json-formatted string
        print 'json.dumps: ', json.dumps(decoded, sort_keys=True, indent=4)

        print "JSON parsing example: decode['one'] = ", decoded['one']
        print "Complex JSON parsing example: ", decoded['two']['list'][1]['item']

    except (ValueError, KeyError, TypeError):
        print "JSON format error"


sample2()
