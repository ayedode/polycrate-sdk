from typing import Literal

ApiV1AlertroutersArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1AlertroutersArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
