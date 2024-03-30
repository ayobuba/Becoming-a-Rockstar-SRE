import os


def remove_from_path(path_to_remove):
    # Get the current PATH environment variable
    paths = os.environ.get('PATH', '').split(':')

    # Remove the specified path
    if path_to_remove in paths:
        paths.remove(path_to_remove)

    # Set the PATH environment variable
    os.environ['PATH'] = ':'.join(paths)


# Removing the supplied paths
google_cloud_binaries = [
    "/Users/ryu/google-cloud-sdk/bin/gke-gcloud-auth-plugin",
    "/Users/ryu/google-cloud-sdk/bin/git-credential-gcloud.sh",
    "/Users/ryu/google-cloud-sdk/bin/dev_appserver.py",
    "/Users/ryu/google-cloud-sdk/bin/anthoscli",
    "/Users/ryu/google-cloud-sdk/bin/java_dev_appserver.sh",
    "/Users/ryu/google-cloud-sdk/bin/gcloud",
    "/Users/ryu/google-cloud-sdk/bin/bq",
    "/Users/ryu/google-cloud-sdk/bin/gsutil",
    "/Users/ryu/google-cloud-sdk/bin/docker-credential-gcloud",
]

for binary in google_cloud_binaries:
    remove_from_path(binary)
