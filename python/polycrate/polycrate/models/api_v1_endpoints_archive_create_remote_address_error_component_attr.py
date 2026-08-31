from typing import Literal

ApiV1EndpointsArchiveCreateRemoteAddressErrorComponentAttr = Literal["remote_address"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateRemoteAddressErrorComponentAttr
] = {
    "remote_address",
}


def check_api_v1_endpoints_archive_create_remote_address_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateRemoteAddressErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
