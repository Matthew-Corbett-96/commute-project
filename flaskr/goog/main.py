from google.cloud import storage


def getBucket():
    client = storage.Client()
    client.get_bucket("commute-project")
