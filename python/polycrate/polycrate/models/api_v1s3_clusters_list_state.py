from typing import Literal

ApiV1S3ClustersListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1S3_CLUSTERS_LIST_STATE_VALUES: set[ApiV1S3ClustersListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1s3_clusters_list_state(value: str) -> ApiV1S3ClustersListState:
    if value in API_V1S3_CLUSTERS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_STATE_VALUES!r}")
