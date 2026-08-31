from typing import Literal

ApiV1PrefixesListRegionErrorComponentAttr = Literal["region"]

API_V1_PREFIXES_LIST_REGION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesListRegionErrorComponentAttr] = {
    "region",
}


def check_api_v1_prefixes_list_region_error_component_attr(value: str) -> ApiV1PrefixesListRegionErrorComponentAttr:
    if value in API_V1_PREFIXES_LIST_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
