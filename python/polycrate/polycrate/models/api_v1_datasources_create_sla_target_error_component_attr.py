from typing import Literal

ApiV1DatasourcesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_DATASOURCES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_datasources_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1DatasourcesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_DATASOURCES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
