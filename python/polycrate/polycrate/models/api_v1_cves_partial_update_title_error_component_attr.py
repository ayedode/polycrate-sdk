from typing import Literal

ApiV1CvesPartialUpdateTitleErrorComponentAttr = Literal["title"]

API_V1_CVES_PARTIAL_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesPartialUpdateTitleErrorComponentAttr] = {
    "title",
}


def check_api_v1_cves_partial_update_title_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateTitleErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
