from typing import Literal

LbiV2LoadBalancingType = Literal["ConsistentHash", "LeastRequest", "Random", "RoundRobin"]

LBI_V2_LOAD_BALANCING_TYPE_VALUES: set[LbiV2LoadBalancingType] = {
    "ConsistentHash",
    "LeastRequest",
    "Random",
    "RoundRobin",
}


def check_lbi_v2_load_balancing_type(value: str) -> LbiV2LoadBalancingType:
    if value in LBI_V2_LOAD_BALANCING_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_LOAD_BALANCING_TYPE_VALUES!r}")
