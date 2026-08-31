from typing import Literal

ApiV1S3ClustersUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1S3_CLUSTERS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1s3_clusters_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateArchivedAtErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
