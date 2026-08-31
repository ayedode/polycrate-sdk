from typing import Literal

ApiV1CertificatesSyncCreateK8SClusterIdErrorComponentAttr = Literal["k8s_cluster_id"]

API_V1_CERTIFICATES_SYNC_CREATE_K8S_CLUSTER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesSyncCreateK8SClusterIdErrorComponentAttr
] = {
    "k8s_cluster_id",
}


def check_api_v1_certificates_sync_create_k8s_cluster_id_error_component_attr(
    value: str,
) -> ApiV1CertificatesSyncCreateK8SClusterIdErrorComponentAttr:
    if value in API_V1_CERTIFICATES_SYNC_CREATE_K8S_CLUSTER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_SYNC_CREATE_K8S_CLUSTER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
