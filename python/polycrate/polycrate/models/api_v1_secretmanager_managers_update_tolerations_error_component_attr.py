from typing import Literal

ApiV1SecretmanagerManagersUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_secretmanager_managers_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateTolerationsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
