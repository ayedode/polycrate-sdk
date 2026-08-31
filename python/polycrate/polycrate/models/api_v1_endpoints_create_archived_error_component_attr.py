from typing import Literal

ApiV1EndpointsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ENDPOINTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsCreateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_endpoints_create_archived_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateArchivedErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
