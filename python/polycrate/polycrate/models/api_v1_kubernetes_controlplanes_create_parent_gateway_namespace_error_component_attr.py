from typing import Literal

ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponentAttr = Literal["parent_gateway_namespace"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponentAttr
] = {
    "parent_gateway_namespace",
}


def check_api_v1_kubernetes_controlplanes_create_parent_gateway_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
