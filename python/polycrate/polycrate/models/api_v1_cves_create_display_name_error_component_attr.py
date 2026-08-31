from typing import Literal

ApiV1CvesCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_CVES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateDisplayNameErrorComponentAttr] = {
    "display_name",
}


def check_api_v1_cves_create_display_name_error_component_attr(
    value: str,
) -> ApiV1CvesCreateDisplayNameErrorComponentAttr:
    if value in API_V1_CVES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
