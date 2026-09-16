from typing import Literal

ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponentAttr = Literal["parent_gateway_section_name"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_SECTION_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponentAttr
] = {
    "parent_gateway_section_name",
}


def check_api_v1_kubernetes_controlplanes_update_parent_gateway_section_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_SECTION_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_SECTION_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
