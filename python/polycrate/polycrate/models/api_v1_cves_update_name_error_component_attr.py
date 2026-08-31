from typing import Literal

ApiV1CvesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_CVES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_cves_update_name_error_component_attr(value: str) -> ApiV1CvesUpdateNameErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
