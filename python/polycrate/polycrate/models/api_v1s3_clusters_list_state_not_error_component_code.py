from typing import Literal

ApiV1S3ClustersListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1S3_CLUSTERS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3ClustersListStateNotErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1s3_clusters_list_state_not_error_component_code(
    value: str,
) -> ApiV1S3ClustersListStateNotErrorComponentCode:
    if value in API_V1S3_CLUSTERS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
