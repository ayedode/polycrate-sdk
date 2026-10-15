from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_category_slug import AlertCategorySlug, check_alert_category_slug
from ..models.alert_list_criticality_type_1 import AlertListCriticalityType1, check_alert_list_criticality_type_1
from ..models.alert_list_criticality_type_2_type_1 import (
    AlertListCriticalityType2Type1,
    check_alert_list_criticality_type_2_type_1,
)
from ..models.alert_list_criticality_type_3_type_1 import (
    AlertListCriticalityType3Type1,
    check_alert_list_criticality_type_3_type_1,
)
from ..models.alert_list_effective_criticality_type_1 import (
    AlertListEffectiveCriticalityType1,
    check_alert_list_effective_criticality_type_1,
)
from ..models.alert_list_effective_criticality_type_2_type_1 import (
    AlertListEffectiveCriticalityType2Type1,
    check_alert_list_effective_criticality_type_2_type_1,
)
from ..models.alert_list_effective_criticality_type_3_type_1 import (
    AlertListEffectiveCriticalityType3Type1,
    check_alert_list_effective_criticality_type_3_type_1,
)
from ..models.alert_list_kind import AlertListKind, check_alert_list_kind
from ..models.alert_list_state import AlertListState, check_alert_list_state
from ..models.alert_list_status_type_1 import AlertListStatusType1, check_alert_list_status_type_1
from ..models.alert_list_status_type_2_type_1 import AlertListStatusType2Type1, check_alert_list_status_type_2_type_1
from ..models.alert_list_status_type_3_type_1 import AlertListStatusType3Type1, check_alert_list_status_type_3_type_1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_list_active_condition_instances_item import AlertListActiveConditionInstancesItem
    from ..models.alert_list_created import AlertListCreated
    from ..models.alert_list_organization_type_0 import AlertListOrganizationType0
    from ..models.alert_list_workspace_type_0 import AlertListWorkspaceType0


T = TypeVar("T", bound="AlertList")


@_attrs_define
class AlertList:
    """Basis-Serializer für alle ManagedObject List-Endpoints.

    Liefert die generischen Felder die alle ManagedObjects teilen:
    - id: UUID
    - name: String-Repräsentation des Objects (__str__)
    - state: Object State
    - organization: Organization (id, slug, name)
    - workspace: Workspace (id, name) oder None
    - created: Kombifeld (created_at, created_at_humanized, created_at_display, created_by)

    Subclasses müssen:
    - model in Meta definieren
    - Zusätzliche model-spezifische Felder in Meta.fields hinzufügen

    Usage:
        class K8sClusterListSerializer(ManagedObjectListSerializer):
            class Meta(ManagedObjectListSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectListSerializer.Meta.fields + ['kubernetes_version', 'kind']

        Attributes:
            id (UUID):
            name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
            state (AlertListState): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            labels (Any):
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
                Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
            active_condition_instances (list[AlertListActiveConditionInstancesItem]):
            organization (AlertListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (AlertListWorkspaceType0 | None):
            created (AlertListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (AlertListEffectiveCriticalityType1 | AlertListEffectiveCriticalityType2Type1 |
                AlertListEffectiveCriticalityType3Type1 | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (AlertListKind): * `grafana` - Grafana Alert
                * `generic` - Generic Alert
                * `checkmk` - CheckMK Alert
            status (AlertListStatusType1 | AlertListStatusType2Type1 | AlertListStatusType3Type1 | None): * `firing` -
                Firing
                * `silenced` - Silenced
                * `resolved` - Resolved
                * `pending` - Pending
            criticality (AlertListCriticalityType1 | AlertListCriticalityType2Type1 | AlertListCriticalityType3Type1 |
                None): Criticality level. Null = inherit from workspace, then org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            title (None | str):
            category (AlertCategorySlug | Unset): AlertCategory.name slug (Spec 654/674)
    """

    id: UUID
    name: str
    state: AlertListState
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[AlertListActiveConditionInstancesItem]
    organization: AlertListOrganizationType0 | None
    organization_priority: bool
    workspace: AlertListWorkspaceType0 | None
    created: AlertListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: (
        AlertListEffectiveCriticalityType1
        | AlertListEffectiveCriticalityType2Type1
        | AlertListEffectiveCriticalityType3Type1
        | None
    )
    url: str
    kind: AlertListKind
    status: AlertListStatusType1 | AlertListStatusType2Type1 | AlertListStatusType3Type1 | None
    criticality: AlertListCriticalityType1 | AlertListCriticalityType2Type1 | AlertListCriticalityType3Type1 | None
    title: None | str
    category: AlertCategorySlug | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_list_organization_type_0 import AlertListOrganizationType0  # noqa: PLC0415
        from ..models.alert_list_workspace_type_0 import AlertListWorkspaceType0  # noqa: PLC0415

        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

        conditions = self.conditions

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization: dict[str, Any] | None
        if isinstance(self.organization, AlertListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, AlertListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        kind: str = self.kind

        status: None | str
        if isinstance(self.status, str):
            status = self.status
        elif isinstance(self.status, str):
            status = self.status
        elif isinstance(self.status, str):
            status = self.status
        else:
            status = self.status

        criticality: None | str
        if isinstance(self.criticality, str):
            criticality = self.criticality
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        title: None | str
        title = self.title

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "conditions": conditions,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "workspace": workspace,
                "created": created,
                "archived": archived,
                "reconciliation_running": reconciliation_running,
                "effective_criticality": effective_criticality,
                "url": url,
                "kind": kind,
                "status": status,
                "criticality": criticality,
                "title": title,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_list_active_condition_instances_item import AlertListActiveConditionInstancesItem  # noqa: PLC0415
        from ..models.alert_list_created import AlertListCreated  # noqa: PLC0415
        from ..models.alert_list_organization_type_0 import AlertListOrganizationType0  # noqa: PLC0415
        from ..models.alert_list_workspace_type_0 import AlertListWorkspaceType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_alert_list_state(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = AlertListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> AlertListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = AlertListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> AlertListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = AlertListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = AlertListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(
            data: object,
        ) -> (
            AlertListEffectiveCriticalityType1
            | AlertListEffectiveCriticalityType2Type1
            | AlertListEffectiveCriticalityType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_1 = check_alert_list_effective_criticality_type_1(data)

                return effective_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_2_type_1 = check_alert_list_effective_criticality_type_2_type_1(data)

                return effective_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_3_type_1 = check_alert_list_effective_criticality_type_3_type_1(data)

                return effective_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AlertListEffectiveCriticalityType1
                | AlertListEffectiveCriticalityType2Type1
                | AlertListEffectiveCriticalityType3Type1
                | None,
                data,
            )

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        kind = check_alert_list_kind(d.pop("kind"))

        def _parse_status(
            data: object,
        ) -> AlertListStatusType1 | AlertListStatusType2Type1 | AlertListStatusType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = check_alert_list_status_type_1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = check_alert_list_status_type_2_type_1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = check_alert_list_status_type_3_type_1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertListStatusType1 | AlertListStatusType2Type1 | AlertListStatusType3Type1 | None, data)

        status = _parse_status(d.pop("status"))

        def _parse_criticality(
            data: object,
        ) -> AlertListCriticalityType1 | AlertListCriticalityType2Type1 | AlertListCriticalityType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_alert_list_criticality_type_1(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_2_type_1 = check_alert_list_criticality_type_2_type_1(data)

                return criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_3_type_1 = check_alert_list_criticality_type_3_type_1(data)

                return criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                AlertListCriticalityType1 | AlertListCriticalityType2Type1 | AlertListCriticalityType3Type1 | None, data
            )

        criticality = _parse_criticality(d.pop("criticality"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        _category = d.pop("category", UNSET)
        category: AlertCategorySlug | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_alert_category_slug(_category)

        alert_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            conditions=conditions,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            workspace=workspace,
            created=created,
            archived=archived,
            reconciliation_running=reconciliation_running,
            effective_criticality=effective_criticality,
            url=url,
            kind=kind,
            status=status,
            criticality=criticality,
            title=title,
            category=category,
        )

        alert_list.additional_properties = d
        return alert_list

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
