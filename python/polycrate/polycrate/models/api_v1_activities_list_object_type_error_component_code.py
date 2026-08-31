from typing import Literal

ApiV1ActivitiesListObjectTypeErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ACTIVITIES_LIST_OBJECT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ActivitiesListObjectTypeErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_activities_list_object_type_error_component_code(
    value: str,
) -> ApiV1ActivitiesListObjectTypeErrorComponentCode:
    if value in API_V1_ACTIVITIES_LIST_OBJECT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_OBJECT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
