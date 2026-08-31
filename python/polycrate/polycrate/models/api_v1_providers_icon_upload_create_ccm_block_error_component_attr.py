from typing import Literal

ApiV1ProvidersIconUploadCreateCcmBlockErrorComponentAttr = Literal["ccm_block"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_CCM_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateCcmBlockErrorComponentAttr
] = {
    "ccm_block",
}


def check_api_v1_providers_icon_upload_create_ccm_block_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateCcmBlockErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_CCM_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_CCM_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
