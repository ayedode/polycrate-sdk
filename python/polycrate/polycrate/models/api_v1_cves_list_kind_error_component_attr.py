from typing import Literal

ApiV1CvesListKindErrorComponentAttr = Literal["kind"]

API_V1_CVES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_cves_list_kind_error_component_attr(value: str) -> ApiV1CvesListKindErrorComponentAttr:
    if value in API_V1_CVES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
