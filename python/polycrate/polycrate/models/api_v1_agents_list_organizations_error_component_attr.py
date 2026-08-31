from typing import Literal

ApiV1AgentsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_AGENTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AgentsListOrganizationsErrorComponentAttr] = {
    "organizations",
}


def check_api_v1_agents_list_organizations_error_component_attr(
    value: str,
) -> ApiV1AgentsListOrganizationsErrorComponentAttr:
    if value in API_V1_AGENTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
