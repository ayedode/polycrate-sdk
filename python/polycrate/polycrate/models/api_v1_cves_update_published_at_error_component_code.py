from typing import Literal

ApiV1CvesUpdatePublishedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CVES_UPDATE_PUBLISHED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesUpdatePublishedAtErrorComponentCode] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_cves_update_published_at_error_component_code(
    value: str,
) -> ApiV1CvesUpdatePublishedAtErrorComponentCode:
    if value in API_V1_CVES_UPDATE_PUBLISHED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_PUBLISHED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
