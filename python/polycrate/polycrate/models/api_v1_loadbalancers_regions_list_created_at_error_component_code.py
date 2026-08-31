from typing import Literal

ApiV1LoadbalancersRegionsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_loadbalancers_regions_list_created_at_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsListCreatedAtErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
