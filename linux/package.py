import argparse, subprocess, os, platform


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--uproject', help='Project to package')
    parser.add_argument('--output_folder', help='Folder to put packaged binary')

    args = parser.parse_args()

    abs_project_path = os.path.abspath(args.uproject)
    abs_output_folder = os.path.abspath(args.output_folder)
    UE4 = os.environ.get('UE4')

    if not UE4:
        print("The environment variable UE4 can not be found")
        sys.exit(-1)

    system_name = platform.system()
    if system_name == 'Linux':
        UAT_Script = os.path.join(UE4, 'Engine/Build/BatchFiles/RunUAT.sh')
        platform_name = 'Linux'
    elif system_name == 'Darwin':
        pass
    elif system_name == 'Windows': # ??
        UAT_Script = os.path.join(UE4, 'Engine\\Build\\BatchFiles\\RunUAT.bat')
        BuildScript = os.path.join(UE4, 'Engine\\Build\\BatchFiles\\Build.bat')
        platform_name = 'Win64'
        project_name = os.path.basename(args.uproject).replace('.uproject', '')

        subprocess.call([
            BuildScript, '%sEditor' % project_name,
            'Win64', 'Development', args.uproject, '-waitmutex'
        ])
    else:
        print('The system %s can not be supported' % system_name)

    subprocess.call([
        UAT_Script, 'BuildCookRun',
        '-project=%s' % abs_project_path,
        '-archivedirectory=%s' % abs_output_folder,
        '-platform=%s' % platform_name,
        '-clientconfig=Development',
        '-noP4', '-allmaps', '-stage', '-pak', '-archive', '-cook', '-build'
    ])
