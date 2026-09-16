from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cost_statement_status_enum import CostStatementStatusEnum, check_cost_statement_status_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_statement_list_active_condition_instances_item import (
        CostStatementListActiveConditionInstancesItem,
    )
    from ..models.cost_statement_list_created import CostStatementListCreated
    from ..models.cost_statement_list_organization_type_0 import CostStatementListOrganizationType0
    from ..models.cost_statement_list_workspace_type_0 import CostStatementListWorkspaceType0


T = TypeVar("T", bound="CostStatementList")


@_attrs_define
class CostStatementList:
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
            state (LastStateEnum): * `OK` - Ok
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
            active_condition_instances (list[CostStatementListActiveConditionInstancesItem]):
            organization (CostStatementListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (CostStatementListWorkspaceType0 | None):
            created (CostStatementListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            period_start (datetime.datetime):
            period_end (datetime.datetime):
            status (CostStatementStatusEnum | Unset): * `draft` - Draft
                * `final` - Final
                * `voided` - Voided
            total_net (str | Unset):
            currency (str | Unset):
            is_manual (bool | Unset):
            generated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[CostStatementListActiveConditionInstancesItem]
    organization: CostStatementListOrganizationType0 | None
    organization_priority: bool
    workspace: CostStatementListWorkspaceType0 | None
    created: CostStatementListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    period_start: datetime.datetime
    period_end: datetime.datetime
    status: CostStatementStatusEnum | Unset = UNSET
    total_net: str | Unset = UNSET
    currency: str | Unset = UNSET
    is_manual: bool | Unset = UNSET
    generated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cost_statement_list_organization_type_0 import CostStatementListOrganizationType0  # noqa: PLC0415
        from ..models.cost_statement_list_workspace_type_0 import CostStatementListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, CostStatementListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, CostStatementListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        total_net = self.total_net

        currency = self.currency

        is_manual = self.is_manual

        generated_at: None | str | Unset
        if isinstance(self.generated_at, Unset):
            generated_at = UNSET
        elif isinstance(self.generated_at, datetime.datetime):
            generated_at = self.generated_at.isoformat()
        else:
            generated_at = self.generated_at

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
                "period_start": period_start,
                "period_end": period_end,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if total_net is not UNSET:
            field_dict["total_net"] = total_net
        if currency is not UNSET:
            field_dict["currency"] = currency
        if is_manual is not UNSET:
            field_dict["is_manual"] = is_manual
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_statement_list_active_condition_instances_item import (
            CostStatementListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.cost_statement_list_created import CostStatementListCreated  # noqa: PLC0415
        from ..models.cost_statement_list_organization_type_0 import CostStatementListOrganizationType0  # noqa: PLC0415
        from ..models.cost_statement_list_workspace_type_0 import CostStatementListWorkspaceType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = CostStatementListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> CostStatementListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = CostStatementListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostStatementListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> CostStatementListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = CostStatementListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostStatementListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = CostStatementListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(data: object) -> EffectiveCriticalityEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_0 = check_effective_criticality_enum(data)

                return effective_criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EffectiveCriticalityEnum | None, data)

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        period_start = datetime.datetime.fromisoformat(d.pop("period_start"))

        period_end = datetime.datetime.fromisoformat(d.pop("period_end"))

        _status = d.pop("status", UNSET)
        status: CostStatementStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_cost_statement_status_enum(_status)

        total_net = d.pop("total_net", UNSET)

        currency = d.pop("currency", UNSET)

        is_manual = d.pop("is_manual", UNSET)

        def _parse_generated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                generated_at_type_0 = datetime.datetime.fromisoformat(data)

                return generated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        generated_at = _parse_generated_at(d.pop("generated_at", UNSET))

        cost_statement_list = cls(
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
            period_start=period_start,
            period_end=period_end,
            status=status,
            total_net=total_net,
            currency=currency,
            is_manual=is_manual,
            generated_at=generated_at,
        )

        cost_statement_list.additional_properties = d
        return cost_statement_list

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
