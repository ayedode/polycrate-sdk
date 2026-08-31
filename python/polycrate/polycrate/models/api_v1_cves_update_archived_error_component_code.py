from typing import Literal

ApiV1CvesUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_CVES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesUpdateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_cves_update_archived_error_component_code(value: str) -> ApiV1CvesUpdateArchivedErrorComponentCode:
    if value in API_V1_CVES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
