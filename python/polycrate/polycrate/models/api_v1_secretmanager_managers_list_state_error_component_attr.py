from typing import Literal

ApiV1SecretmanagerManagersListStateErrorComponentAttr = Literal["state"]

API_V1_SECRETMANAGER_MANAGERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_secretmanager_managers_list_state_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersListStateErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
