from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_secretmanager_managers_partial_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
