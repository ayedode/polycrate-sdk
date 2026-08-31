from typing import Literal

ApiV1S3ClustersArchiveCreateAliasErrorComponentAttr = Literal["alias"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateAliasErrorComponentAttr
] = {
    "alias",
}


def check_api_v1s3_clusters_archive_create_alias_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateAliasErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
