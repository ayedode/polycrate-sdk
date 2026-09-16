from typing import Literal

ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_create_parent_gateway_namespace_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
