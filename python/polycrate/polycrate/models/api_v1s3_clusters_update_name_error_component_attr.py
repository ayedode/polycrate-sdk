from typing import Literal

ApiV1S3ClustersUpdateNameErrorComponentAttr = Literal["name"]

API_V1S3_CLUSTERS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1s3_clusters_update_name_error_component_attr(value: str) -> ApiV1S3ClustersUpdateNameErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
