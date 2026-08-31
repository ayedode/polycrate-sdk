from typing import Literal

ApiV1S3ClustersCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1S3_CLUSTERS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1s3_clusters_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateArchivedByErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
