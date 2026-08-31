from typing import Literal

ApiV1IncidentsPartialUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_INCIDENTS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_incidents_partial_update_scope_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateScopeErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
