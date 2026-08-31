from typing import Literal

ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ALERTS_ARCHIVE_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_alerts_archive_create_silence_ends_at_error_component_code(
    value: str,
) -> ApiV1AlertsArchiveCreateSilenceEndsAtErrorComponentCode:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_SILENCE_ENDS_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
