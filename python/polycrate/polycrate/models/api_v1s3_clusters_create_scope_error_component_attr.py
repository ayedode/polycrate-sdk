from typing import Literal

ApiV1S3ClustersCreateScopeErrorComponentAttr = Literal["scope"]

API_V1S3_CLUSTERS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersCreateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1s3_clusters_create_scope_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateScopeErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
