from typing import Literal

ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponentAttr = Literal["last_synced_from_cluster"]

API_V1_CERTIFICATES_ARCHIVE_CREATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponentAttr
] = {
    "last_synced_from_cluster",
}


def check_api_v1_certificates_archive_create_last_synced_from_cluster_error_component_attr(
    value: str,
) -> ApiV1CertificatesArchiveCreateLastSyncedFromClusterErrorComponentAttr:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
