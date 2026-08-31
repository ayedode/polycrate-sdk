from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.renewal_mode_enum import RenewalModeEnum, check_renewal_mode_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_zone_simple import DNSZoneSimple
    from ..models.domain_list_active_condition_instances_item import DomainListActiveConditionInstancesItem
    from ..models.domain_list_created import DomainListCreated
    from ..models.domain_list_organization_type_0 import DomainListOrganizationType0
    from ..models.domain_list_workspace_type_0 import DomainListWorkspaceType0
    from ..models.domain_registrar_simple import DomainRegistrarSimple


T = TypeVar("T", bound="DomainList")


@_attrs_define
class DomainList:
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
            active_condition_instances (list[DomainListActiveConditionInstancesItem]):
            organization (DomainListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (DomainListWorkspaceType0 | None):
            created (DomainListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            registrar (DomainRegistrarSimple):
            dns_zone (DNSZoneSimple):
            provider_status (None | str | Unset): Raw domain status string as returned by the registrar.
            renewal_mode (RenewalModeEnum | Unset): * `AUTORENEW` - Auto Renew — domain renews automatically
                * `AUTODELETE` - Auto Delete — domain deleted at expiry
            expiry_date (datetime.datetime | None | Unset): Domain expiry / renewal date.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[DomainListActiveConditionInstancesItem]
    organization: DomainListOrganizationType0 | None
    organization_priority: bool
    workspace: DomainListWorkspaceType0 | None
    created: DomainListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    registrar: DomainRegistrarSimple
    dns_zone: DNSZoneSimple
    provider_status: None | str | Unset = UNSET
    renewal_mode: RenewalModeEnum | Unset = UNSET
    expiry_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_list_organization_type_0 import DomainListOrganizationType0
        from ..models.domain_list_workspace_type_0 import DomainListWorkspaceType0

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
        if isinstance(self.organization, DomainListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, DomainListWorkspaceType0):
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

        registrar = self.registrar.to_dict()

        dns_zone = self.dns_zone.to_dict()

        provider_status: None | str | Unset
        if isinstance(self.provider_status, Unset):
            provider_status = UNSET
        else:
            provider_status = self.provider_status

        renewal_mode: str | Unset = UNSET
        if not isinstance(self.renewal_mode, Unset):
            renewal_mode = self.renewal_mode

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.datetime):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

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
                "registrar": registrar,
                "dns_zone": dns_zone,
            }
        )
        if provider_status is not UNSET:
            field_dict["provider_status"] = provider_status
        if renewal_mode is not UNSET:
            field_dict["renewal_mode"] = renewal_mode
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_zone_simple import DNSZoneSimple
        from ..models.domain_list_active_condition_instances_item import DomainListActiveConditionInstancesItem
        from ..models.domain_list_created import DomainListCreated
        from ..models.domain_list_organization_type_0 import DomainListOrganizationType0
        from ..models.domain_list_workspace_type_0 import DomainListWorkspaceType0
        from ..models.domain_registrar_simple import DomainRegistrarSimple

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
            active_condition_instances_item = DomainListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> DomainListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = DomainListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> DomainListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = DomainListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = DomainListCreated.from_dict(d.pop("created"))

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

        registrar = DomainRegistrarSimple.from_dict(d.pop("registrar"))

        dns_zone = DNSZoneSimple.from_dict(d.pop("dns_zone"))

        def _parse_provider_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_status = _parse_provider_status(d.pop("provider_status", UNSET))

        _renewal_mode = d.pop("renewal_mode", UNSET)
        renewal_mode: RenewalModeEnum | Unset
        if isinstance(_renewal_mode, Unset):
            renewal_mode = UNSET
        else:
            renewal_mode = check_renewal_mode_enum(_renewal_mode)

        def _parse_expiry_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        domain_list = cls(
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
            registrar=registrar,
            dns_zone=dns_zone,
            provider_status=provider_status,
            renewal_mode=renewal_mode,
            expiry_date=expiry_date,
        )

        domain_list.additional_properties = d
        return domain_list

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
