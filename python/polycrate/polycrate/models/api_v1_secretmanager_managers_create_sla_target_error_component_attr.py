from typing import Literal

ApiV1SecretmanagerManagersCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_secretmanager_managers_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateSlaTargetErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
