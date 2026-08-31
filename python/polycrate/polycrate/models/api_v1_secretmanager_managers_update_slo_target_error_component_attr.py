from typing import Literal

ApiV1SecretmanagerManagersUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_secretmanager_managers_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateSloTargetErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
