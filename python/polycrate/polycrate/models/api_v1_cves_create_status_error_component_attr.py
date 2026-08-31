from typing import Literal

ApiV1CvesCreateStatusErrorComponentAttr = Literal["status"]

API_V1_CVES_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_cves_create_status_error_component_attr(value: str) -> ApiV1CvesCreateStatusErrorComponentAttr:
    if value in API_V1_CVES_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
