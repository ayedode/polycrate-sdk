from typing import Literal

ApiV1ApmApmstacksListOrganizationsErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_APM_APMSTACKS_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ApmApmstacksListOrganizationsErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_apm_apmstacks_list_organizations_error_component_code(
    value: str,
) -> ApiV1ApmApmstacksListOrganizationsErrorComponentCode:
    if value in API_V1_APM_APMSTACKS_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
