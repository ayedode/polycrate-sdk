from typing import Literal

ApiV1SecretmanagerManagersUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_secretmanager_managers_update_criticality_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateCriticalityErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
