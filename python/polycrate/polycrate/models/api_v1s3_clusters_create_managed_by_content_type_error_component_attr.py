from typing import Literal

ApiV1S3ClustersCreateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1S3_CLUSTERS_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1s3_clusters_create_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateManagedByContentTypeErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
