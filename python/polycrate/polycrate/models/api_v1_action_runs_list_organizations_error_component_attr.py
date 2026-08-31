from typing import Literal

ApiV1ActionRunsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_ACTION_RUNS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ActionRunsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_action_runs_list_organizations_error_component_attr(
    value: str,
) -> ApiV1ActionRunsListOrganizationsErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
