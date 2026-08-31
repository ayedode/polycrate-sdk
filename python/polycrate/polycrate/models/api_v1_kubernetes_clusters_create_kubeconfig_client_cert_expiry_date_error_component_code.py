from typing import Literal

ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_KUBERNETES_CLUSTERS_CREATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_clusters_create_kubeconfig_client_cert_expiry_date_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreateKubeconfigClientCertExpiryDateErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
