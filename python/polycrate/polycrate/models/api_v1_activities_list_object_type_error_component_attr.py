from typing import Literal

ApiV1ActivitiesListObjectTypeErrorComponentAttr = Literal["object_type"]

API_V1_ACTIVITIES_LIST_OBJECT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActivitiesListObjectTypeErrorComponentAttr] = {
    "object_type",
}


def check_api_v1_activities_list_object_type_error_component_attr(
    value: str,
) -> ApiV1ActivitiesListObjectTypeErrorComponentAttr:
    if value in API_V1_ACTIVITIES_LIST_OBJECT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_OBJECT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
