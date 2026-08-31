from typing import Literal

ApiV1SecretmanagerManagersCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_secretmanager_managers_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateTolerationsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
