from typing import Literal

ApiV1CredentialsDiscoverCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_CREDENTIALS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsDiscoverCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_credentials_discover_create_criticality_error_component_code(
    value: str,
) -> ApiV1CredentialsDiscoverCreateCriticalityErrorComponentCode:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
