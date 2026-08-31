from typing import Literal

ApiV1ConditionInstancesPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_condition_instances_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateProviderErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
