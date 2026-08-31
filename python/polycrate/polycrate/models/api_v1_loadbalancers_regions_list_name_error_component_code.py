from typing import Literal

ApiV1LoadbalancersRegionsListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_LOADBALANCERS_REGIONS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsListNameErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_loadbalancers_regions_list_name_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsListNameErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
