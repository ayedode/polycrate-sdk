from typing import Literal

ApiV1AlertroutersCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ALERTROUTERS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertroutersCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_alertrouters_create_kind_error_component_attr(
    value: str,
) -> ApiV1AlertroutersCreateKindErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
