from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateClusterDomainErrorComponentAttr = Literal["cluster_domain"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_CLUSTER_DOMAIN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateClusterDomainErrorComponentAttr
] = {
    "cluster_domain",
}


def check_api_v1_kubernetes_controlplanes_partial_update_cluster_domain_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateClusterDomainErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_CLUSTER_DOMAIN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_CLUSTER_DOMAIN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
