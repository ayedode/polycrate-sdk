from typing import Literal

ApiV1CvesUpdateTitleErrorComponentAttr = Literal["title"]

API_V1_CVES_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateTitleErrorComponentAttr] = {
    "title",
}


def check_api_v1_cves_update_title_error_component_attr(value: str) -> ApiV1CvesUpdateTitleErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
