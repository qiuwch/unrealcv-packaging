import os, json, argparse, platform
def parse_unrealcv_version(unrealcv_folder='./unrealcv'):
    plugin_descriptor = os.path.join(unrealcv_folder, 'UnrealCV.uplugin')
    with open(plugin_descriptor) as f:
        description = json.load(f)
    plugin_version = description['VersionName']
    return plugin_version

def parse_ue4_version(ue4_folder=os.environ['UE4']):
    version_file = os.path.join(ue4_folder, 'Engine/Build/Build.version')
    with open(version_file) as f:
        v = json.load(f)
    ue4_version = '%s.%s' % (v['MajorVersion'], v['MinorVersion']) # PathVersion is not neccessary
    return ue4_version

def parse_platform():
    return platform.system() 

if __name__ == '__main__':
    unrealcv_version = parse_unrealcv_version() 
    ue4_version = parse_ue4_version()
    info = dict(
        unrealcv_version = unrealcv_version,
        ue4_version = ue4_version,
        platform = parse_platform(),
    )
    info_keys = ','.join(info.keys())

    parser = argparse.ArgumentParser()
    format_help = '''The information to be included in the string, available options are %s
    An example is "{ue4_version}-{unrealcv_version}''' % info_keys
    parser.add_argument('--format', required=True, help = format_help) 
    args = parser.parse_args()

    print(args.format.format(**info))
