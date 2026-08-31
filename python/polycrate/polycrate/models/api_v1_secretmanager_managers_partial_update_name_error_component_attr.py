from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_secretmanager_managers_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateNameErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
