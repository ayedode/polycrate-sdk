from typing import Literal

ApiV1ApmApmstacksListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_APM_APMSTACKS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmApmstacksListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_apm_apmstacks_list_organizations_error_component_attr(
    value: str,
) -> ApiV1ApmApmstacksListOrganizationsErrorComponentAttr:
    if value in API_V1_APM_APMSTACKS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
