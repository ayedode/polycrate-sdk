from typing import Literal

ApiV1ProvidersPartialUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PROVIDERS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_providers_partial_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateSloTargetErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
