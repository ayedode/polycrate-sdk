from typing import Literal

ApiV1ApmApmstacksListCreatedByUsersErrorComponentAttr = Literal["created_by_users"]

API_V1_APM_APMSTACKS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmApmstacksListCreatedByUsersErrorComponentAttr
] = {
    "created_by_users",
}


def check_api_v1_apm_apmstacks_list_created_by_users_error_component_attr(
    value: str,
) -> ApiV1ApmApmstacksListCreatedByUsersErrorComponentAttr:
    if value in API_V1_APM_APMSTACKS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
