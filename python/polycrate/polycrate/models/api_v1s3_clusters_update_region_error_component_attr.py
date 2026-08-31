from typing import Literal

ApiV1S3ClustersUpdateRegionErrorComponentAttr = Literal["region"]

API_V1S3_CLUSTERS_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersUpdateRegionErrorComponentAttr] = {
    "region",
}


def check_api_v1s3_clusters_update_region_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateRegionErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
