from typing import Literal

ApiV1EndpointsCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ENDPOINTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsCreateProviderErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_endpoints_create_provider_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateProviderErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
