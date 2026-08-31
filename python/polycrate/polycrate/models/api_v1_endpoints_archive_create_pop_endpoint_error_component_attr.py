from typing import Literal

ApiV1EndpointsArchiveCreatePopEndpointErrorComponentAttr = Literal["pop_endpoint"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreatePopEndpointErrorComponentAttr
] = {
    "pop_endpoint",
}


def check_api_v1_endpoints_archive_create_pop_endpoint_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreatePopEndpointErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_POP_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
