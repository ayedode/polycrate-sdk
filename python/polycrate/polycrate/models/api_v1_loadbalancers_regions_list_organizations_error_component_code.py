from typing import Literal

ApiV1LoadbalancersRegionsListOrganizationsErrorComponentCode = Literal[
    "invalid_choice", "invalid_list", "invalid_pk_value"
]

API_V1_LOADBALANCERS_REGIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsListOrganizationsErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_loadbalancers_regions_list_organizations_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsListOrganizationsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
