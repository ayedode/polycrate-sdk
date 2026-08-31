from typing import Literal

ApiV1S3ClustersListScope = Literal["system", "user"]

API_V1S3_CLUSTERS_LIST_SCOPE_VALUES: set[ApiV1S3ClustersListScope] = {
    "system",
    "user",
}


def check_api_v1s3_clusters_list_scope(value: str) -> ApiV1S3ClustersListScope:
    if value in API_V1S3_CLUSTERS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_SCOPE_VALUES!r}")
