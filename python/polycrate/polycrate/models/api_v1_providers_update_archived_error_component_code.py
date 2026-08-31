from typing import Literal

ApiV1ProvidersUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersUpdateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_providers_update_archived_error_component_code(
    value: str,
) -> ApiV1ProvidersUpdateArchivedErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
