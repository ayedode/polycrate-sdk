from typing import Literal

ProviderDetailBsiGrundschutzStatus = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_BSI_GRUNDSCHUTZ_STATUS_VALUES: set[ProviderDetailBsiGrundschutzStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_bsi_grundschutz_status(value: str) -> ProviderDetailBsiGrundschutzStatus:
    if value in PROVIDER_DETAIL_BSI_GRUNDSCHUTZ_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_BSI_GRUNDSCHUTZ_STATUS_VALUES!r}")
