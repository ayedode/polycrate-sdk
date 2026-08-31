from typing import Literal

ApiV1EndpointsArchiveCreateSpecErrorComponentAttr = Literal["spec"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateSpecErrorComponentAttr
] = {
    "spec",
}


def check_api_v1_endpoints_archive_create_spec_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateSpecErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
