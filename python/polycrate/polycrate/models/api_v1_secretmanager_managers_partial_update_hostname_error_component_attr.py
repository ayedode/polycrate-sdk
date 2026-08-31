from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_secretmanager_managers_partial_update_hostname_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
