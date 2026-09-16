from typing import Literal

ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_GATEWAY_CLASS_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_update_gateway_class_name_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_GATEWAY_CLASS_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_GATEWAY_CLASS_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
