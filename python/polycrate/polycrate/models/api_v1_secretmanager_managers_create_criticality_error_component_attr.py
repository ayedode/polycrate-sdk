from typing import Literal

ApiV1SecretmanagerManagersCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_secretmanager_managers_create_criticality_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateCriticalityErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
