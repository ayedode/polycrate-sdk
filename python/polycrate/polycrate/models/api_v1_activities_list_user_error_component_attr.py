from typing import Literal

ApiV1ActivitiesListUserErrorComponentAttr = Literal["user"]

API_V1_ACTIVITIES_LIST_USER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActivitiesListUserErrorComponentAttr] = {
    "user",
}


def check_api_v1_activities_list_user_error_component_attr(value: str) -> ApiV1ActivitiesListUserErrorComponentAttr:
    if value in API_V1_ACTIVITIES_LIST_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
