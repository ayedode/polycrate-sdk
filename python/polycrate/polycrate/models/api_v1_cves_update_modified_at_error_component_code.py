from typing import Literal

ApiV1CvesUpdateModifiedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CVES_UPDATE_MODIFIED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesUpdateModifiedAtErrorComponentCode] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_cves_update_modified_at_error_component_code(
    value: str,
) -> ApiV1CvesUpdateModifiedAtErrorComponentCode:
    if value in API_V1_CVES_UPDATE_MODIFIED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_MODIFIED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
