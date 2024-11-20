import argparse
import subprocess

def test(development_id, project_path, scheme):
    # # Add your testing commands here
    print("Running tests...")
    # Example: Run unit tests
    subprocess.run([
        'xcodebuild', 'test',
        '-project', project_path,
        '-scheme', scheme,
        f'DEVELOPMENT_TEAM={development_id}'
    ], check=True)
    print("Tests executed successfully.")
    print(development_id, project_path, scheme)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run tests for Xcode project.')
    parser.add_argument('--development-id', required=True)
    parser.add_argument('--project-path', required=True)
    parser.add_argument('--scheme', required=True)
    args = parser.parse_args()
    test(args.development_id, args.project_path, args.scheme)
