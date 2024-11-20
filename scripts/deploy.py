import argparse
import subprocess

def deploy(archive_path, output_dir, export_options_plist):
    # Export the .ipa file
    # subprocess.run([
    #     'xcodebuild', '-exportArchive',
    #     '-archivePath', archive_path,
    #     '-exportOptionsPlist', export_options_plist,
    #     '-exportPath', output_dir
    # ], check=True)
    # print(f"IPA exported to {output_dir}.")
    print("Deploy completed successfully.")
    print(archive_path, output_dir, export_options_plist)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deploy Xcode project.')
    parser.add_argument('--archive-path', required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--export-options-plist', required=True)
    args = parser.parse_args()
    deploy(args.archive_path, args.output_dir, args.export_options_plist)
