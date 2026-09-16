from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponentAttr = Literal["parent_gateway_namespace"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponentAttr
] = {
    "parent_gateway_namespace",
}


def check_api_v1_kubernetes_controlplanes_partial_update_parent_gateway_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
