from typing import Literal

ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponentAttr = Literal["ceph_osd_cluster_total_bytes"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_CEPH_OSD_CLUSTER_TOTAL_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponentAttr
] = {
    "ceph_osd_cluster_total_bytes",
}


def check_api_v1s3_clusters_partial_update_ceph_osd_cluster_total_bytes_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_CEPH_OSD_CLUSTER_TOTAL_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_CEPH_OSD_CLUSTER_TOTAL_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
