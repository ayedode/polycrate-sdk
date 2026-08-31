from typing import Literal

ApiV1ActivitiesListKindErrorComponentAttr = Literal["kind"]

API_V1_ACTIVITIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActivitiesListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_activities_list_kind_error_component_attr(value: str) -> ApiV1ActivitiesListKindErrorComponentAttr:
    if value in API_V1_ACTIVITIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
