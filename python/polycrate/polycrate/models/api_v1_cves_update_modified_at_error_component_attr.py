from typing import Literal

ApiV1CvesUpdateModifiedAtErrorComponentAttr = Literal["modified_at"]

API_V1_CVES_UPDATE_MODIFIED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateModifiedAtErrorComponentAttr] = {
    "modified_at",
}


def check_api_v1_cves_update_modified_at_error_component_attr(
    value: str,
) -> ApiV1CvesUpdateModifiedAtErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_MODIFIED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_MODIFIED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
