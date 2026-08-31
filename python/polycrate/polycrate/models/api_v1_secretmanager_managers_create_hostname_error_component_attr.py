from typing import Literal

ApiV1SecretmanagerManagersCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_secretmanager_managers_create_hostname_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateHostnameErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
