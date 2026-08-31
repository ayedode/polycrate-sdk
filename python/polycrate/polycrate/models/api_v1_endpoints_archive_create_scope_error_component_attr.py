from typing import Literal

ApiV1EndpointsArchiveCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_endpoints_archive_create_scope_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateScopeErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
