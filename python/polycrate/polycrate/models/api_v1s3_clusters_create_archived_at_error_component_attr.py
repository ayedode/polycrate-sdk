from typing import Literal

ApiV1S3ClustersCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1S3_CLUSTERS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1s3_clusters_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateArchivedAtErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
