from typing import Literal

ApiV1AlertsListCategoryItem = Literal[
    "application.customer",
    "availability.http",
    "backup.velero",
    "cluster.node",
    "data.cnpg",
    "data.mariadb",
    "data.mongodb",
    "data.replication",
    "gitops.flux",
    "observability.metrics",
    "platform.test",
    "security.access",
    "security.secrets",
    "storage.volume",
    "unknown",
    "workload.pod",
]

API_V1_ALERTS_LIST_CATEGORY_ITEM_VALUES: set[ApiV1AlertsListCategoryItem] = {
    "application.customer",
    "availability.http",
    "backup.velero",
    "cluster.node",
    "data.cnpg",
    "data.mariadb",
    "data.mongodb",
    "data.replication",
    "gitops.flux",
    "observability.metrics",
    "platform.test",
    "security.access",
    "security.secrets",
    "storage.volume",
    "unknown",
    "workload.pod",
}


def check_api_v1_alerts_list_category_item(value: str) -> ApiV1AlertsListCategoryItem:
    if value in API_V1_ALERTS_LIST_CATEGORY_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_CATEGORY_ITEM_VALUES!r}")
