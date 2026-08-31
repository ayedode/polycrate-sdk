from typing import Literal

ApiV1KubernetesControlplanesUpdateClusterDomainErrorComponentAttr = Literal["cluster_domain"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_CLUSTER_DOMAIN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateClusterDomainErrorComponentAttr
] = {
    "cluster_domain",
}


def check_api_v1_kubernetes_controlplanes_update_cluster_domain_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateClusterDomainErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_CLUSTER_DOMAIN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_CLUSTER_DOMAIN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
