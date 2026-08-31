from typing import Literal

ApiV1S3ClustersUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1S3_CLUSTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersUpdateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1s3_clusters_update_archived_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateArchivedErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
