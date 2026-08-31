from typing import Literal

ApiV1CvesListStatusErrorComponentAttr = Literal["status"]

API_V1_CVES_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesListStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_cves_list_status_error_component_attr(value: str) -> ApiV1CvesListStatusErrorComponentAttr:
    if value in API_V1_CVES_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
