from typing import Literal

ApiV1S3ClustersCreateAliasErrorComponentAttr = Literal["alias"]

API_V1S3_CLUSTERS_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersCreateAliasErrorComponentAttr] = {
    "alias",
}


def check_api_v1s3_clusters_create_alias_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateAliasErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
