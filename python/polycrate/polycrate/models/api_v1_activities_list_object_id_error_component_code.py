from typing import Literal

ApiV1ActivitiesListObjectIdErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ACTIVITIES_LIST_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ActivitiesListObjectIdErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_activities_list_object_id_error_component_code(
    value: str,
) -> ApiV1ActivitiesListObjectIdErrorComponentCode:
    if value in API_V1_ACTIVITIES_LIST_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
