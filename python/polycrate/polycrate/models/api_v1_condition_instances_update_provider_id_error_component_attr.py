from typing import Literal

ApiV1ConditionInstancesUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CONDITION_INSTANCES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_condition_instances_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateProviderIdErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
