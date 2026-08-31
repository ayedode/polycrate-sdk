from typing import Literal

ApiV1AlertroutersArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_alertrouters_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1AlertroutersArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
