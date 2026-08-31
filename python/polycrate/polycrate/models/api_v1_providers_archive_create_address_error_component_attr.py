from typing import Literal

ApiV1ProvidersArchiveCreateAddressErrorComponentAttr = Literal["address"]

API_V1_PROVIDERS_ARCHIVE_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersArchiveCreateAddressErrorComponentAttr
] = {
    "address",
}


def check_api_v1_providers_archive_create_address_error_component_attr(
    value: str,
) -> ApiV1ProvidersArchiveCreateAddressErrorComponentAttr:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
