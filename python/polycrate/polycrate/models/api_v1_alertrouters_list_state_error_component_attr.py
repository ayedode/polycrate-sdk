from typing import Literal

ApiV1AlertroutersListStateErrorComponentAttr = Literal["state"]

API_V1_ALERTROUTERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertroutersListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_alertrouters_list_state_error_component_attr(
    value: str,
) -> ApiV1AlertroutersListStateErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
