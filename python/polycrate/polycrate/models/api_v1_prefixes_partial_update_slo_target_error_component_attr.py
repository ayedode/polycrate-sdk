from typing import Literal

ApiV1PrefixesPartialUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PREFIXES_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesPartialUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_prefixes_partial_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1PrefixesPartialUpdateSloTargetErrorComponentAttr:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
