from typing import Literal

AgentListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

AGENT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[AgentListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_agent_list_effective_criticality_type_3_type_1(value: str) -> AgentListEffectiveCriticalityType3Type1:
    if value in AGENT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AGENT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
