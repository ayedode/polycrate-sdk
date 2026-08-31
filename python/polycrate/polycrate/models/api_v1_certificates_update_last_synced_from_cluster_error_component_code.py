from typing import Literal

ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CERTIFICATES_UPDATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_certificates_update_last_synced_from_cluster_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateLastSyncedFromClusterErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_LAST_SYNCED_FROM_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
