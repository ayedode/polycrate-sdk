from typing import Literal

ApiV1S3ClustersArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1s3_clusters_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
