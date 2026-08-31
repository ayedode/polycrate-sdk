from typing import Literal

ApiV1AlertroutersUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_update_archived_error_component_code(
    value: str,
) -> ApiV1AlertroutersUpdateArchivedErrorComponentCode:
    if value in API_V1_ALERTROUTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
