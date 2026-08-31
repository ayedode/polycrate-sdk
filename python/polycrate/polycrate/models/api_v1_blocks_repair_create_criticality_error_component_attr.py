from typing import Literal

ApiV1BlocksRepairCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCKS_REPAIR_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_blocks_repair_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
