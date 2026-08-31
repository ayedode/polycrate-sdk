from typing import Literal

ApiV1ProvidersCreateCsiControllerBlockErrorComponentAttr = Literal["csi_controller_block"]

API_V1_PROVIDERS_CREATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersCreateCsiControllerBlockErrorComponentAttr
] = {
    "csi_controller_block",
}


def check_api_v1_providers_create_csi_controller_block_error_component_attr(
    value: str,
) -> ApiV1ProvidersCreateCsiControllerBlockErrorComponentAttr:
    if value in API_V1_PROVIDERS_CREATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
