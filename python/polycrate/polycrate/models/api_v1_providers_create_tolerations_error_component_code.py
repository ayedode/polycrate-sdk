from typing import Literal

ApiV1ProvidersCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_create_tolerations_error_component_code(
    value: str,
) -> ApiV1ProvidersCreateTolerationsErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
