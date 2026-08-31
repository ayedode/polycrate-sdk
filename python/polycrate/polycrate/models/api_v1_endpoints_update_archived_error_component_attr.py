from typing import Literal

ApiV1EndpointsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ENDPOINTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsUpdateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_endpoints_update_archived_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateArchivedErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
