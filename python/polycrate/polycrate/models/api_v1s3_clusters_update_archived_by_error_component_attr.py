from typing import Literal

ApiV1S3ClustersUpdateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1S3_CLUSTERS_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1s3_clusters_update_archived_by_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateArchivedByErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
