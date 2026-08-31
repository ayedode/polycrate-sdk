from typing import Literal

ApiV1ApmApmstacksListSearchErrorComponentAttr = Literal["search"]

API_V1_APM_APMSTACKS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ApmApmstacksListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_apm_apmstacks_list_search_error_component_attr(
    value: str,
) -> ApiV1ApmApmstacksListSearchErrorComponentAttr:
    if value in API_V1_APM_APMSTACKS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
