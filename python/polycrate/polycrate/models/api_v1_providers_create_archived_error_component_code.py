from typing import Literal

ApiV1ProvidersCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersCreateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_providers_create_archived_error_component_code(
    value: str,
) -> ApiV1ProvidersCreateArchivedErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
