from typing import Literal

ApiV1S3ClustersCreateActiveErrorComponentAttr = Literal["active"]

API_V1S3_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersCreateActiveErrorComponentAttr] = {
    "active",
}


def check_api_v1s3_clusters_create_active_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateActiveErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
