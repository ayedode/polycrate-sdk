from typing import Literal

ApiV1ApmApmstacksListKindErrorComponentAttr = Literal["kind"]

API_V1_APM_APMSTACKS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ApmApmstacksListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_apm_apmstacks_list_kind_error_component_attr(
    value: str,
) -> ApiV1ApmApmstacksListKindErrorComponentAttr:
    if value in API_V1_APM_APMSTACKS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
