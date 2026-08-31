from typing import Literal

ApiV1ProvidersCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PROVIDERS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_providers_create_criticality_error_component_code(
    value: str,
) -> ApiV1ProvidersCreateCriticalityErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
