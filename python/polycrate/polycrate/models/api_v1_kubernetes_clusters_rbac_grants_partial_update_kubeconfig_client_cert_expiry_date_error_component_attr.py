from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponentAttr = Literal[
    "kubeconfig_client_cert_expiry_date"
]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponentAttr
] = {
    "kubeconfig_client_cert_expiry_date",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_kubeconfig_client_cert_expiry_date_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponentAttr:
    if (
        value
        in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
