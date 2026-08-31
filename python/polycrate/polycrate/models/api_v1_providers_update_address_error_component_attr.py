from typing import Literal

ApiV1ProvidersUpdateAddressErrorComponentAttr = Literal["address"]

API_V1_PROVIDERS_UPDATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersUpdateAddressErrorComponentAttr] = {
    "address",
}


def check_api_v1_providers_update_address_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateAddressErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
