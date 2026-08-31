from typing import Literal

ApiV1BlocksRepairCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_BLOCKS_REPAIR_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_blocks_repair_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
