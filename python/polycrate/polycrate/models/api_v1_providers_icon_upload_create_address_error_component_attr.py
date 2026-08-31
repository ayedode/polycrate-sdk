from typing import Literal

ApiV1ProvidersIconUploadCreateAddressErrorComponentAttr = Literal["address"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateAddressErrorComponentAttr
] = {
    "address",
}


def check_api_v1_providers_icon_upload_create_address_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateAddressErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
