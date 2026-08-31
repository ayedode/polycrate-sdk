from typing import Literal

ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponentCode = Literal[
    "invalid_choice", "invalid_list", "invalid_pk_value"
]

API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_loadbalancers_regions_list_created_by_users_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
