from typing import Literal

ApiV1AlertsArchiveCreateSilenceUrlErrorComponentAttr = Literal["silence_url"]

API_V1_ALERTS_ARCHIVE_CREATE_SILENCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsArchiveCreateSilenceUrlErrorComponentAttr
] = {
    "silence_url",
}


def check_api_v1_alerts_archive_create_silence_url_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreateSilenceUrlErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_SILENCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_SILENCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
