from typing import Literal

ApiV1EndpointsArchiveCreatePopEndpointErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsArchiveCreatePopEndpointErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_archive_create_pop_endpoint_error_component_code(
    value: str,
) -> ApiV1EndpointsArchiveCreatePopEndpointErrorComponentCode:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
