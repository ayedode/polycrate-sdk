from typing import Literal

ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponentAttr = Literal["last_synced_from_cluster"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponentAttr
] = {
    "last_synced_from_cluster",
}


def check_api_v1_certificates_partial_update_last_synced_from_cluster_error_component_attr(
    value: str,
) -> ApiV1CertificatesPartialUpdateLastSyncedFromClusterErrorComponentAttr:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
