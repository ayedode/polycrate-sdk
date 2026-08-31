from typing import Literal

ApiV1EndpointsReconcileCreateRemoteAddressErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_ENDPOINTS_RECONCILE_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateRemoteAddressErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_endpoints_reconcile_create_remote_address_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateRemoteAddressErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
