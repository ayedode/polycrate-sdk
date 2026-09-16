from typing import Literal

ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_SECTION_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_update_parent_gateway_section_name_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_SECTION_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_SECTION_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
