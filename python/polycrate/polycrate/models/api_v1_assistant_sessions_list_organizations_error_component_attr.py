from typing import Literal

ApiV1AssistantSessionsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_ASSISTANT_SESSIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_assistant_sessions_list_organizations_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsListOrganizationsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
