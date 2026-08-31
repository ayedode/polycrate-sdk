from typing import Literal

ApiV1PrefixesUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PREFIXES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesUpdateSlaTargetErrorComponentAttr] = {
    "sla_target",
}


def check_api_v1_prefixes_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1PrefixesUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_PREFIXES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
