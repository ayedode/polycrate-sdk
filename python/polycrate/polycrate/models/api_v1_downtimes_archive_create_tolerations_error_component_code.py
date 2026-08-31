from typing import Literal

ApiV1DowntimesArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_downtimes_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1DowntimesArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
