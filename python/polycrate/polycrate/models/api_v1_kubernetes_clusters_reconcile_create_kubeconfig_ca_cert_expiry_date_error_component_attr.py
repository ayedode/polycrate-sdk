from typing import Literal

ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponentAttr = Literal[
    "kubeconfig_ca_cert_expiry_date"
]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_KUBECONFIG_CA_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponentAttr
] = {
    "kubeconfig_ca_cert_expiry_date",
}


def check_api_v1_kubernetes_clusters_reconcile_create_kubeconfig_ca_cert_expiry_date_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateKubeconfigCaCertExpiryDateErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_KUBECONFIG_CA_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_KUBECONFIG_CA_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
