from typing import Literal

ApiV1CertificatesSyncCreateK8SClusterIdErrorComponentCode = Literal["invalid", "max_string_length", "null", "required"]

API_V1_CERTIFICATES_SYNC_CREATE_K8S_CLUSTER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesSyncCreateK8SClusterIdErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "null",
    "required",
}


def check_api_v1_certificates_sync_create_k8s_cluster_id_error_component_code(
    value: str,
) -> ApiV1CertificatesSyncCreateK8SClusterIdErrorComponentCode:
    if value in API_V1_CERTIFICATES_SYNC_CREATE_K8S_CLUSTER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_SYNC_CREATE_K8S_CLUSTER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
