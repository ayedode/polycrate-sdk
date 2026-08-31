from typing import Literal

ApiV1CertificatesCreateLastSyncedFromClusterErrorComponentAttr = Literal["last_synced_from_cluster"]

API_V1_CERTIFICATES_CREATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesCreateLastSyncedFromClusterErrorComponentAttr
] = {
    "last_synced_from_cluster",
}


def check_api_v1_certificates_create_last_synced_from_cluster_error_component_attr(
    value: str,
) -> ApiV1CertificatesCreateLastSyncedFromClusterErrorComponentAttr:
    if value in API_V1_CERTIFICATES_CREATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
