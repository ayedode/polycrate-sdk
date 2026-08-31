from typing import Literal

ApiV1KubernetesClustersPartialUpdateCredentialErrorComponentAttr = Literal["credential"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_kubernetes_clusters_partial_update_credential_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateCredentialErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
