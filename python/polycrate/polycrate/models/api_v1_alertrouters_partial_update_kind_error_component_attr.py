from typing import Literal

ApiV1AlertroutersPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_alertrouters_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1AlertroutersPartialUpdateKindErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
