from typing import Literal

ApiV1S3ClustersUpdateManagedByContentTypeErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1S3_CLUSTERS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdateManagedByContentTypeErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1s3_clusters_update_managed_by_content_type_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateManagedByContentTypeErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
