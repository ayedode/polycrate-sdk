from typing import Literal

ApiV1IncidentsUpdateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_INCIDENTS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_incidents_update_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateModifiedByUserErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
