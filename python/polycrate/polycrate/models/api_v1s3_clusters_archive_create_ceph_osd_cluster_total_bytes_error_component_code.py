from typing import Literal

ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_CEPH_OSD_CLUSTER_TOTAL_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1s3_clusters_archive_create_ceph_osd_cluster_total_bytes_error_component_code(
    value: str,
) -> ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponentCode:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_CEPH_OSD_CLUSTER_TOTAL_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_CEPH_OSD_CLUSTER_TOTAL_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
