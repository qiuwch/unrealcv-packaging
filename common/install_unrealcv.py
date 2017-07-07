'''
TODO: Check whether the plugin has been compiled
This is specicifically designed for UnrealCV plugin, which performs some extra checkings
'''

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--uproject', help='The UE4 uproject to install unrealcv')
    parser.add_argument('--unrealcv', help='The root folder of UnrealCV plugin')

    args = parser.parse_args()

    project_folder = os.path.dirname(arg.uproject)

    unrealcv_binary_dir = os.path.join(args.unrealcv, 'Plugins/UnrealCV')
    target_dir = os.path.join

    shutil.copytree(unrealcv_binary_dir, target_dir)
