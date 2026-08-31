from typing import Literal

ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponentAttr = Literal[
    "kubeconfig_client_cert_expiry_date"
]

API_V1_KUBERNETES_CLUSTERS_UPDATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponentAttr
] = {
    "kubeconfig_client_cert_expiry_date",
}


def check_api_v1_kubernetes_clusters_update_kubeconfig_client_cert_expiry_date_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateKubeconfigClientCertExpiryDateErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
