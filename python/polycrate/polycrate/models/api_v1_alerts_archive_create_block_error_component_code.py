from typing import Literal

ApiV1AlertsArchiveCreateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ALERTS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsArchiveCreateBlockErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_alerts_archive_create_block_error_component_code(
    value: str,
) -> ApiV1AlertsArchiveCreateBlockErrorComponentCode:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
