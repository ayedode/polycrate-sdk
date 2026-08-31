from typing import Literal

ApiV1AlertroutersUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_ALERTROUTERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertroutersUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_alertrouters_update_kind_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateKindErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
