from typing import Literal

ApiV1S3ClustersPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1s3_clusters_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1S3ClustersPartialUpdateLabelsErrorComponentCode:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
