import jsonschema, argparse, json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json',
        # default='./tasks/Linux_UE414/unrealcv.json',
        default='./tasks/Linux_UE414/zoo.json',
        help = 'The task file to validate')
    parser.add_argument('--schema', default='./task.schema', help='The schema file to define a task')

    args = parser.parse_args()

    # json_text = open(args.json).read()
    # schema_text = open(args.schema).read()
    json_obj = json.load(open(args.json))
    schema_obj = json.load(open(args.schema))


    jsonschema.validate(json_obj, schema_obj)

    print("Successfully validate %s with %s" % (args.json, args.schema))
