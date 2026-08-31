from typing import Literal

ApiV1IncidentsArchiveCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_INCIDENTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_incidents_archive_create_scope_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateScopeErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
