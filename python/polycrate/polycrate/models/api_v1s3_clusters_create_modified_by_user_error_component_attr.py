from typing import Literal

ApiV1S3ClustersCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1S3_CLUSTERS_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1s3_clusters_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateModifiedByUserErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
