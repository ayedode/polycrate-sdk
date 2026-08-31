from typing import Literal

ApiV1AgentsListOrganizationsErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_AGENTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AgentsListOrganizationsErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_agents_list_organizations_error_component_code(
    value: str,
) -> ApiV1AgentsListOrganizationsErrorComponentCode:
    if value in API_V1_AGENTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
