from typing import Literal

ApiV1ProvidersUpdateCsiControllerBlockErrorComponentAttr = Literal["csi_controller_block"]

API_V1_PROVIDERS_UPDATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersUpdateCsiControllerBlockErrorComponentAttr
] = {
    "csi_controller_block",
}


def check_api_v1_providers_update_csi_controller_block_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateCsiControllerBlockErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_CSI_CONTROLLER_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
