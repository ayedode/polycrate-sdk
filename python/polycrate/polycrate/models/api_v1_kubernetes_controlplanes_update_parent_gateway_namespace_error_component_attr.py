from typing import Literal

ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponentAttr = Literal["parent_gateway_namespace"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponentAttr
] = {
    "parent_gateway_namespace",
}


def check_api_v1_kubernetes_controlplanes_update_parent_gateway_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
