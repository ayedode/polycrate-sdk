from typing import Literal

ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_loadbalancers_regions_list_created_by_component_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
