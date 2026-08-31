from typing import Literal

ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_POPS_PARTIAL_UPDATE_POP_ENDPOINT_REMOTE_ADDRESS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pops_partial_update_pop_endpoint_remote_address_error_component_code(
    value: str,
) -> ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponentCode:
    if value in API_V1_POPS_PARTIAL_UPDATE_POP_ENDPOINT_REMOTE_ADDRESS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_POP_ENDPOINT_REMOTE_ADDRESS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
