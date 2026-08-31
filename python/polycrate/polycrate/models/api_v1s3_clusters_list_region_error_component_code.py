from typing import Literal

ApiV1S3ClustersListRegionErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1S3_CLUSTERS_LIST_REGION_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3ClustersListRegionErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1s3_clusters_list_region_error_component_code(value: str) -> ApiV1S3ClustersListRegionErrorComponentCode:
    if value in API_V1S3_CLUSTERS_LIST_REGION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_REGION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
