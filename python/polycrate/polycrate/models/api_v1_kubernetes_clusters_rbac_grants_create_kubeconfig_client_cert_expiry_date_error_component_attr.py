from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponentAttr = Literal[
    "kubeconfig_client_cert_expiry_date"
]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponentAttr
] = {
    "kubeconfig_client_cert_expiry_date",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_kubeconfig_client_cert_expiry_date_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponentAttr:
    if (
        value
        in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_KUBECONFIG_CLIENT_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
