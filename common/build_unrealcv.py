import subprocess, os, argparse, platform

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', help='Output folder of compiled plugin')

    args = parser.parse_args()
    output_folder = args.output

    unrealcv_folder = os.environ.get('UnrealCV')
    unrealcv_descriptor = os.path.join(unrealcv_folder, 'UnrealCV.uplugin')

    UE4 = os.environ.get('UE4')

    system_name = platform.system()
    if system_name == 'Linux':
        UAT_Script = os.path.join(UE4, 'Engine/Build/BatchFiles/RunUAT.sh')
        platform_name = 'Linux'
    elif system_name == 'Darwin':
        pass
    elif system_name == 'Windows': # ??
        UAT_Script = os.path.join(UE4, 'Engine\\Build\\BatchFiles\\RunUAT.bat')
        platform_name = 'Win64'
    else:
        print('The system %s can not be supported' % system_name)

    abs_unrealcv_descriptor = os.path.abspath(unrealcv_descriptor)
    abs_output_folder = os.path.abspath(output_folder)

    subprocess.call([
        UAT_Script, 'BuildPlugin',
        '-plugin=%s' % abs_unrealcv_descriptor,
        '-package=%s' % abs_output_folder,
        '-rocket', '-targetplatforms=%s' % platform_name
    ], cwd = unrealcv_folder)
