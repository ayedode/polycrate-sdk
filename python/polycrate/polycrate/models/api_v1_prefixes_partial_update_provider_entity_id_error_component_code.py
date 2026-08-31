from typing import Literal

ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PREFIXES_PARTIAL_UPDATE_PROVIDER_ENTITY_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_prefixes_partial_update_provider_entity_id_error_component_code(
    value: str,
) -> ApiV1PrefixesPartialUpdateProviderEntityIdErrorComponentCode:
    if value in API_V1_PREFIXES_PARTIAL_UPDATE_PROVIDER_ENTITY_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_PARTIAL_UPDATE_PROVIDER_ENTITY_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
