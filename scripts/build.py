import argparse
import os
import subprocess

def build(development_id, code_sign_pass, project_path, scheme, output_dir):
    # Unlock the keychain
    # subprocess.run(['security', 'unlock-keychain', '-p', code_sign_pass], check=True)
    
    # Clean and build the project
    subprocess.run(['xcodebuild', 'clean', '-project', project_path, '-scheme', scheme, '-configuration', 'Release'], check=True)
    subprocess.run([
        'xcodebuild', 'archive',
        '-project', project_path,
        '-scheme', scheme,
        '-archivePath', f'{output_dir}/YourApp.xcarchive',
        f'DEVELOPMENT_TEAM={development_id}'
    ], check=True)
    print("Build completed successfully.")
    print(development_id, code_sign_pass, project_path, scheme, output_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build Xcode project.')
    parser.add_argument('--development-id', required=True)
    parser.add_argument('--code-sign-pass', required=True)
    parser.add_argument('--project-path', required=True)
    parser.add_argument('--scheme', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    build(args.development_id, args.code_sign_pass, args.project_path, args.scheme, args.output_dir)
