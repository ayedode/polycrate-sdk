from typing import Literal

ApiV1AlertroutersListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_ALERTROUTERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertroutersListStateNotErrorComponentAttr] = {
    "state_not",
}


def check_api_v1_alertrouters_list_state_not_error_component_attr(
    value: str,
) -> ApiV1AlertroutersListStateNotErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
