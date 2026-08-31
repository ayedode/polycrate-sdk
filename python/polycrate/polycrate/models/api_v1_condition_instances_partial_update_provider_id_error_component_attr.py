from typing import Literal

ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_condition_instances_partial_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
