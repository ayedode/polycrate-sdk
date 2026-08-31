from typing import Literal

ApiV1DatasourcesPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_DATASOURCES_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_datasources_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
