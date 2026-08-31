from typing import Literal

ApiV1SecretmanagerManagersCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_secretmanager_managers_create_display_name_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateDisplayNameErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
