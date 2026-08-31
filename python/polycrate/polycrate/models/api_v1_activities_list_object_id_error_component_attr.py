from typing import Literal

ApiV1ActivitiesListObjectIdErrorComponentAttr = Literal["object_id"]

API_V1_ACTIVITIES_LIST_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActivitiesListObjectIdErrorComponentAttr] = {
    "object_id",
}


def check_api_v1_activities_list_object_id_error_component_attr(
    value: str,
) -> ApiV1ActivitiesListObjectIdErrorComponentAttr:
    if value in API_V1_ACTIVITIES_LIST_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
