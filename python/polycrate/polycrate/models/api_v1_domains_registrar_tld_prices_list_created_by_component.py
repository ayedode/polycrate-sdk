from typing import Literal

ApiV1DomainsRegistrarTldPricesListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1DomainsRegistrarTldPricesListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_domains_registrar_tld_prices_list_created_by_component(
    value: str,
) -> ApiV1DomainsRegistrarTldPricesListCreatedByComponent:
    if value in API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
