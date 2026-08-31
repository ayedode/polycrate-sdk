from typing import Literal

ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_API_SERVER_CERT_EXPIRY_DATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_clusters_discover_create_api_server_cert_expiry_date_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_API_SERVER_CERT_EXPIRY_DATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_API_SERVER_CERT_EXPIRY_DATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
