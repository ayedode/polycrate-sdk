from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponentAttr = Literal[
    "api_server_cert_expiry_date"
]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_API_SERVER_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponentAttr
] = {
    "api_server_cert_expiry_date",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_api_server_cert_expiry_date_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_API_SERVER_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_API_SERVER_CERT_EXPIRY_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
