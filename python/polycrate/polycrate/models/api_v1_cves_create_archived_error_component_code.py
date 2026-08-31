from typing import Literal

ApiV1CvesCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_CVES_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesCreateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_cves_create_archived_error_component_code(value: str) -> ApiV1CvesCreateArchivedErrorComponentCode:
    if value in API_V1_CVES_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
