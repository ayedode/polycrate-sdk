from typing import Literal

ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_secretmanager_managers_update_display_name_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
